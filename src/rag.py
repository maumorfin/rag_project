from __future__ import annotations
from langchain_community.chat_models import ChatOllama
from langchain_core.vectorstores import VectorStore
from langchain_core.documents import Document
from .config import DEFAULT_LLM_MODEL
from .indexing import build_dense_retriever, build_bm25_retriever
from .hybrid import hybrid_retrieve
from typing import Any, Dict, List, Literal

def answer_with_rag(
    query: str,
    vs: VectorStore,
    model_name: str = DEFAULT_LLM_MODEL,
    k: int = 3,
) -> Dict[str, Any]:
    """
    Einfacher RAG-Helper:
    - holt k relevante Chunks aus dem Vectorstore
    - baut einen Kontext
    - ruft ein lokales LLM (Ollama) auf
    - gibt Antwort + Quellen zurück
    """
    retriever = vs.as_retriever(search_kwargs={"k": k})
    docs = retriever.invoke(query)

    if not docs:
        return {
            "answer": "Im Index wurden keine passenden Dokumente gefunden.",
            "sources": [],
        }

    # Kontext aus den gefundenen Chunks bauen
    context_blocks: List[str] = []
    for d in docs:
        src = d.metadata.get("source")
        page = d.metadata.get("page")
        context_blocks.append(
            f"[Quelle: {src}, Seite {page}]\n{d.page_content}"
        )

    context = "\n\n".join(context_blocks)

    prompt = f"""
Du bist ein Experte für technische Normen.

Nutze AUSSCHLIESSLICH den folgenden Kontext, um die Frage zu beantworten.
Wenn die Antwort NICHT im Kontext steht, antworte GENAU mit:
"Die Information ist im bereitgestellten Dokument nicht enthalten."

KONTEXT:
{context}

FRAGE:
{query}

ANTWORT (auf Deutsch, sachlich, präzise, höchstens 5 Sätze):
"""

    llm = ChatOllama(model=model_name, temperature=0.1)
    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": [
            {
                "source": d.metadata.get("source"),
                "page": d.metadata.get("page"),
                "filepath": d.metadata.get("filepath"),
            }
            for d in docs
        ],
    }

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
) -> Dict[str, Any]:
    """
    RAG-Pipeline mit wählbarem Retrieval-Modus:
    - mode="dense"  → Dense Retrieval (Chroma)
    - mode="bm25"   → BM25 Retrieval
    - mode="hybrid" → BM25 + Dense (Hybrid Retrieval)
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

    # Kontext bauen (gleiches Schema wie in answer_with_rag)
    context_blocks: List[str] = []
    for d in docs:
        src = d.metadata.get("source")
        page = d.metadata.get("page")
        context_blocks.append(
            f"[Quelle: {src}, Seite {page}]\n{d.page_content}"
        )

    context = "\n\n".join(context_blocks)

    prompt = f"""
Du bist ein Experte für technische Normen.

Nutze AUSSCHLIESSLICH den folgenden Kontext, um die Frage zu beantworten.
Wenn die Antwort NICHT im Kontext steht, antworte GENAU mit:
"Die Information ist im bereitgestellten Dokument nicht enthalten."

KONTEXT:
{context}

FRAGE:
{query}

ANTWORT (auf Deutsch, sachlich, präzise, höchstens 5 Sätze):
"""

    llm = ChatOllama(model=model_name, temperature=0.1)
    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": [
            {
                "source": d.metadata.get("source"),
                "page": d.metadata.get("page"),
                "filepath": d.metadata.get("filepath"),
            }
            for d in docs
        ],
    }

def answer_with_rag_hybrid(
    query: str,
    model_name: str = DEFAULT_LLM_MODEL,
    k: int = 3,
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
) -> Dict[str, Any]:
    """
    RAG-Pipeline mit Hybrid Retrieval (BM25 + Dense):
    - nutzt hybrid_retrieve()
    - baut Kontext aus den Top-k Dokumenten
    - ruft lokales LLM (Ollama) auf
    """

    # 1) Hybrid Retrieval
    docs: List[Document] = hybrid_retrieve(
        query=query,
        k=k,
        weights=(0.5, 0.5),
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    if not docs:
        return {
            "answer": "Im Index wurden keine passenden Dokumente gefunden.",
            "sources": [],
        }

    # 2) Kontext bauen
    context_blocks: List[str] = []
    for d in docs:
        src = d.metadata.get("source")
        page = d.metadata.get("page")
        context_blocks.append(
            f"[Quelle: {src}, Seite {page}]\n{d.page_content}"
        )

    context = "\n\n".join(context_blocks)

    # 3) Prompt
    prompt = f"""
Du bist ein Experte für technische Normen.

Nutze AUSSCHLIESSLICH den folgenden Kontext, um die Frage zu beantworten.
Wenn die Antwort NICHT im Kontext steht, antworte GENAU mit:
"Die Information ist im bereitgestellten Dokument nicht enthalten."

KONTEXT:
{context}

FRAGE:
{query}

ANTWORT (auf Deutsch, sachlich, präzise, höchstens 5 Sätze):
"""

    # 4) LLM
    llm = ChatOllama(model=model_name, temperature=0.1)
    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": [
            {
                "source": d.metadata.get("source"),
                "page": d.metadata.get("page"),
                "filepath": d.metadata.get("filepath"),
            }
            for d in docs
        ],
    }
