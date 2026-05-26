from __future__ import annotations

import hashlib
import logging
from functools import lru_cache
from typing import Any, Dict, List, Literal

from langchain_community.chat_models import ChatOllama
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore

from .config import DEFAULT_LLM_MODEL, PROMPT_VERSION
from .hybrid import hybrid_retrieve
from .indexing import build_dense_retriever, build_bm25_retriever
from .reranking import rerank_documents

logger = logging.getLogger(__name__)

DEFAULT_RERANKER_MODEL = "BAAI/bge-reranker-v2-m3"


def _build_rag_prompt_llama(context: str, query: str) -> str:
    """Prompt used for the llama3.1:8b evaluation."""
    return f"""
Du bist ein Experte fuer Schienenfahrzeugtechnik.

Beantworte die Frage ausschliesslich auf Basis des bereitgestellten Kontexts.
Erfinde keine Informationen und nutze kein externes Wissen.

Antworte nach diesen Regeln:
1. Wenn die Antwort klar im Kontext enthalten ist, gib eine praezise Antwort.
   - Bei "Warum"- oder "Wie"-Fragen: erklaere den Mechanismus, nicht nur das Ergebnis.
   - Bei tabellarischen Werten: uebernimm Werte exakt. Falls eine Tabellenzeile
     fragmentiert oder unvollstaendig ist, nenne die lesbaren Werte und kennzeichne
     fehlende Eintraege explizit als unvollstaendig – gib aber vorhandene Werte trotzdem an.
2. Wenn die Antwort nicht direkt enthalten ist, aber relevante Hinweise vorliegen:
   - nenne die relevanten Hinweise,
   - kennzeichne die Aussage als unsicher/indirekt ableitbar.
3. Wenn keine relevante Information vorhanden ist, antworte genau mit:
   "Die Information ist im bereitgestellten Dokument nicht enthalten."

Wenn der Kontext Informationen aus mehreren Quellen enthaelt und die Frage
einen Vergleich oder Bezug zwischen diesen impliziert, strukturiere die Antwort
nach Quellen (z.B. "Laut Peche: ... / Laut DZSF-Bericht: ...").

Formatierung:
- Fasse zusammen statt aufzuzaehlen.
- Maximal 5 Saetze (bei Tabellenwerten oder Mehrquellen-Antworten bis zu 6).
- Nenne am Ende nur die relevanteste Quelle.

KONTEXT:
{context}

FRAGE:
{query}

ANTWORT (auf Deutsch, sachlich, praezise):
"""


def _build_rag_prompt_mistral(context: str, query: str) -> str:
    """Prompt used for the mistral-nemo evaluation."""
    return f"""Du bist ein Experte fuer Schienenfahrzeugtechnik.

### KONTEXT ###
{context}

### FRAGE ###
{query}

### ANTWORT ###
Beantworte auf Deutsch, ausschliesslich auf Basis des Kontexts oben.

1. Ist die Antwort direkt enthalten: antworte praezise.
   Bei Tabellenzeilen: vorhandene Werte nennen, fehlende als unvollstaendig kennzeichnen.

2. Fragt die Frage nach einem Grund oder Mechanismus: erklaere den Zusammenhang,
   nicht nur das Ergebnis.

3. Liefert der Kontext nur indirekte Hinweise: nenne sie und kennzeichne
   die Aussage als indirekt ableitbar.

4. Sind mehrere Dokumente relevant: strukturiere nach Quellen:
   "Laut [Quelle A]: ... / Laut [Quelle B]: ..."

5. Ist keine relevante Information vorhanden: antworte NUR mit:
   "Die Information ist im bereitgestellten Dokument nicht enthalten."
   Keine Ableitungen, keine Vermutungen.

6. Liefert der Kontext einen klaren Anknuepfungspunkt zu allgemeinem Fachwissen:
   du darfst dieses Wissen erwaehnen, aber kennzeichne es als Hintergrundwissen.

Maximal 4 Saetze. Nenne am Ende die relevanteste Quelle: [Dateiname], Seite [X]

"""


def _build_rag_prompt(context: str, query: str) -> str:
    if PROMPT_VERSION == "mistral":
        return _build_rag_prompt_mistral(context, query)
    return _build_rag_prompt_llama(context, query)

@lru_cache(maxsize=4)
def get_llm(model_name: str = DEFAULT_LLM_MODEL, temperature: float = 0.1) -> ChatOllama:
    """Create and cache the Ollama client per model/temperature combination."""
    return ChatOllama(model=model_name, temperature=temperature)


def _build_context(docs: List[Document]) -> str:
    """Build a prompt context block from retrieved documents."""
    context_blocks: List[str] = []
    for d in docs:
        src = d.metadata.get("source")
        page = d.metadata.get("page")
        context_blocks.append(
            f"[Quelle: {src}, Seite {page}]\n{d.page_content}"
        )

    return "\n\n".join(context_blocks)


def _format_sources(docs: List[Document]) -> List[Dict[str, Any]]:
    """Return the source metadata for the retrieved documents."""
    return [
        {
            "source": d.metadata.get("source"),
            "page": d.metadata.get("page"),
            "filepath": d.metadata.get("filepath"),
        }
        for d in docs
    ]


def debug_retrieval(query: str, vs: VectorStore, k: int = 3) -> None:
    """
    Kleiner Helper, um im Notebook zu prüfen,
    welche Chunks für eine Query gefunden werden.
    """
    retriever = vs.as_retriever(search_kwargs={"k": k})
    docs = retriever.invoke(query)

    print("Anzahl gefundener Dokumente:", len(docs))
    for i, d in enumerate(docs):
        print(f"\n--- Doc {i} ---")
        print("Source:", d.metadata.get("source"))
        print("Page:", d.metadata.get("page"))
        print(d.page_content[:400], "...")


def get_docs_for_query(
    query: str,
    mode: Literal["dense", "bm25", "hybrid"] = "dense",
    k: int = 3,
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
) -> List[Document]:
    """
    Holt Dokumente für eine Query je nach Retrieval-Modus:
    - dense  → Chroma / Embeddings
    - bm25   → BM25Retriever
    - hybrid → BM25 + Dense (eigene Rank-Fusion)
    """
    if mode == "dense":
        dense = build_dense_retriever(k=k)
        docs = dense.invoke(query)

    elif mode == "bm25":
        bm25 = build_bm25_retriever(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            k=k,
        )
        docs = bm25.invoke(query)

    elif mode == "hybrid":
        docs = hybrid_retrieve(
            query=query,
            k=k,
            weights=(0.5, 0.5),
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )
    else:
        raise ValueError(f"Unbekannter mode: {mode}")

    # 1) Exakte Duplikate per Content-Hash entfernen
    seen: set[str] = set()
    unique_docs: List[Document] = []
    for doc in docs:
        h = hashlib.md5(doc.page_content.encode("utf-8")).hexdigest()
        if h not in seen:
            seen.add(h)
            unique_docs.append(doc)

    # 2) Überlappende Chunks entfernen: kürzeren Chunk weglassen wenn sein Text
    #    vollständig in einem längeren Chunk enthalten ist (chunk_overlap Artefakt)
    texts = [d.page_content for d in unique_docs]
    keep = [True] * len(unique_docs)
    for i in range(len(unique_docs)):
        for j in range(len(unique_docs)):
            if i == j or not keep[i]:
                continue
            if texts[i] in texts[j] and len(texts[i]) < len(texts[j]):
                keep[i] = False
                break
    return [d for d, k in zip(unique_docs, keep) if k]

def answer_with_rag_mode(
    query: str,
    mode: Literal["dense", "bm25", "hybrid"] = "dense",
    model_name: str = DEFAULT_LLM_MODEL,
    k: int = 3,
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
    use_reranker: bool = False,
    rerank_top_n: int | None = None,
    reranker_model: str = DEFAULT_RERANKER_MODEL,
) -> Dict[str, Any]:
    """
    RAG-Pipeline mit wählbarem Retrieval-Modus:
    - mode="dense"  → Dense Retrieval (Chroma)
    - mode="bm25"   → BM25 Retrieval
    - mode="hybrid" → BM25 + Dense (Hybrid Retrieval)
    - optionales Reranking der Kandidaten nach dem Retrieval
    """
    docs = get_docs_for_query(
        query=query,
        mode=mode,
        k=k,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    if not docs:
        return {
            "answer": "Im Index wurden keine passenden Dokumente gefunden.",
            "sources": [],
        }

    if use_reranker:
        target_top_n = rerank_top_n or k
        docs = rerank_documents(
            query=query,
            docs=docs,
            top_n=target_top_n,
            model_name=reranker_model,
        )

    context = _build_context(docs)
    prompt = _build_rag_prompt(context=context, query=query)

    llm = get_llm(model_name=model_name, temperature=0.1)
    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": _format_sources(docs),
    }
