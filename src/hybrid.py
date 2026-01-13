from __future__ import annotations
from typing import List, Tuple, Dict

from collections import defaultdict
from langchain_core.documents import Document

from .indexing import build_dense_retriever, build_bm25_retriever


def hybrid_retrieve(
    query: str,
    k: int = 10,
    weights: Tuple[float, float] = (0.5, 0.5),
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
) -> List[Document]:
    """
    Führt ein einfaches Hybrid-Retrieval aus:
    - BM25 + Dense (Chroma)
    - Rank-Fusion auf Basis der Rangplätze
    - gibt die Top-k Dokumente zurück

    weights = (w_bm25, w_dense)
    """

    # 1) Retriever bauen
    dense = build_dense_retriever(k=k)
    bm25 = build_bm25_retriever(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        k=k,
    )

    # 2) Kandidaten holen
    bm25_docs = bm25.invoke(query)
    dense_docs = dense.invoke(query)

    scores = defaultdict(float)
    doc_map: dict[Tuple[str, int, str], Document] = {}

    def add_scores(docs: List[Document], weight: float):
        for rank, doc in enumerate(docs):
            key = (
                doc.metadata.get("source"),
                doc.metadata.get("page"),
                doc.page_content,
            )
            doc_map[key] = doc
            # Reciprocal Rank Fusion-artiges Scoring
            scores[key] += weight / (rank + 1)

    # 3) Scores aus BM25 + Dense kombinieren
    w_bm25, w_dense = weights
    add_scores(bm25_docs, w_bm25)
    add_scores(dense_docs, w_dense)

    # 4) Nach Score sortieren und Top-k zurückgeben
    sorted_keys = sorted(scores.keys(), key=lambda k_: scores[k_], reverse=True)
    top_keys = sorted_keys[:k]
    top_docs = [doc_map[k_] for k_ in top_keys]

    return top_docs
