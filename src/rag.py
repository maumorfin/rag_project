from __future__ import annotations
from functools import lru_cache
from langchain_community.chat_models import ChatOllama
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore
from .config import DEFAULT_LLM_MODEL
from .indexing import build_dense_retriever, build_bm25_retriever
from .hybrid import hybrid_retrieve
from typing import Any, Dict, List, Literal

DEFAULT_RERANKER_MODEL = "BAAI/bge-reranker-v2-m3"


def _build_rag_prompt(context: str, query: str) -> str:
    """Shared prompt for all RAG answer functions."""
    return f"""
Du bist ein Experte fuer Schienenfahrzeugtechnik.

Beantworte die Frage ausschliesslich auf Basis des bereitgestellten Kontexts.
Erfinde keine Informationen und nutze kein externes Wissen.

Antworte nach diesen Regeln:
1. Wenn die Antwort klar im Kontext enthalten ist, gib eine praezise Antwort.
2. Wenn die Antwort nicht direkt enthalten ist, aber es relevante Hinweise im Kontext gibt, dann:
   - nenne die relevanten Hinweise aus dem Kontext,
   - kennzeichne die Aussage ausdruecklich als unsicher/indirekt ableitbar.
3. Wenn keine relevante Information im Kontext enthalten ist, antworte genau mit:
   "Die Information ist im bereitgestellten Dokument nicht enthalten."

Wenn tabellarische Werte abgefragt werden, uebernimm Werte und Bezeichnungen so exakt wie moeglich aus dem Kontext.
Wenn eine Zuordnung (z. B. eine konkrete Tabellenzeile) nicht eindeutig lesbar ist, gib eine Warnung aus und nenne keine unsicheren Werte als gesichert.

KONTEXT:
{context}

FRAGE:
{query}

ANTWORT (auf Deutsch, sachlich, praezise, hoechstens 6 Saetze):
"""

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

    return docs

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
        from .reranking import rerank_documents

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
