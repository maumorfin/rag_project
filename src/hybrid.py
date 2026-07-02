from __future__ import annotations
from typing import List, Tuple
import hashlib

from collections import defaultdict
from langchain_core.documents import Document

from .indexing import build_dense_retriever, build_bm25_retriever


# Implementierungansatz mit KI-Unterstützung optimiert (Claude Code, Anthropic)
def hybrid_retrieve(
    query: str,
    k: int = 20,
    weights: Tuple[float, float] = (0.5, 0.5),
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
    k0: int = 60,
) -> List[Document]:
    """
    Führt ein einfaches Hybrid-Retrieval aus:
    - BM25 + Dense (Chroma)
    - Rank-Fusion auf Basis der Rangplätze
    - gibt die Top-k Dokumente zurück

    weights = (w_bm25, w_dense)
    """
    if len(weights) != 2:
        raise ValueError("weights muss genau zwei Werte enthalten: (w_bm25, w_dense)")
    if k0 < 0:
        raise ValueError("k0 muss >= 0 sein")

    w_bm25, w_dense = weights
    if w_bm25 < 0 or w_dense < 0:
        raise ValueError("weights dürfen nicht negativ sein")
    weight_sum = w_bm25 + w_dense
    if weight_sum == 0:
        raise ValueError("mindestens ein Gewicht muss > 0 sein")

    # Gewichte normalisieren, damit auch intuitive Verhaeltnisse wie (1, 3) funktionieren.
    w_bm25 /= weight_sum
    w_dense /= weight_sum

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
    doc_map: dict[Tuple[str | None, int | None, str], Document] = {}

    def add_scores(docs: List[Document], weight: float) -> None:
        for rank, doc in enumerate(docs):
            content_hash = hashlib.md5(doc.page_content.encode("utf-8")).hexdigest()
            key = (
                doc.metadata.get("filepath") or doc.metadata.get("source"),
                doc.metadata.get("page"),
                content_hash,
            )
            doc_map[key] = doc
            # Standard Reciprocal Rank Fusion (RRF)
            scores[key] += weight / (k0 + rank)


    # 3) Scores aus BM25 + Dense kombinieren
    add_scores(bm25_docs, w_bm25)
    add_scores(dense_docs, w_dense)

    # 4) Nach Score sortieren und Top-k zurückgeben
    sorted_keys = sorted(scores.keys(), key=lambda k_: scores[k_], reverse=True)
    top_keys = sorted_keys[:k]
    top_docs = [doc_map[k_] for k_ in top_keys]

    return top_docs
