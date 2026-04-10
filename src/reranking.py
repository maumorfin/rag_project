from __future__ import annotations

from functools import lru_cache
from typing import List

from FlagEmbedding import FlagReranker
from langchain_core.documents import Document


DEFAULT_RERANKER_MODEL = "BAAI/bge-reranker-v2-m3"


@lru_cache(maxsize=4)
def get_reranker(
    model_name: str = DEFAULT_RERANKER_MODEL,
    use_fp16: bool = False,
) -> FlagReranker:
    """Create and cache a reranker instance per model/settings combination."""
    return FlagReranker(model_name, use_fp16=use_fp16)


def rerank_documents(
    query: str,
    docs: List[Document],
    *,
    top_n: int = 5,
    model_name: str = DEFAULT_RERANKER_MODEL,
    use_fp16: bool = False,
) -> List[Document]:
    """
    Rerank retrieved documents with a cross-encoder style reranker.

    The input docs are assumed to be candidate results from hybrid
    retrieval. The function returns the best top_n docs after reranking.
    """
    if top_n <= 0:
        raise ValueError("top_n must be > 0")
    if not docs:
        return docs

    reranker = get_reranker(model_name=model_name, use_fp16=use_fp16)
    pairs = [(query, doc.page_content) for doc in docs]
    scores = reranker.compute_score(pairs)

    ranked = sorted(
        zip(scores, docs),
        key=lambda item: item[0],
        reverse=True,
    )
    return [doc for _, doc in ranked[:top_n]]
