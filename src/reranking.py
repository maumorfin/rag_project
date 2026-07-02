from __future__ import annotations

from functools import lru_cache
from typing import List

from langchain_core.documents import Document
from sentence_transformers import CrossEncoder

from .config import RERANKER_MODEL_NAME as DEFAULT_RERANKER_MODEL


@lru_cache(maxsize=1)
def get_reranker(model_name: str = DEFAULT_RERANKER_MODEL) -> CrossEncoder:
    """Lädt das Cross-Encoder-Modell und cached es für die Session."""
    return CrossEncoder(model_name)


def rerank_documents(
    query: str,
    docs: List[Document],
    *,
    top_n: int = 5,
    model_name: str = DEFAULT_RERANKER_MODEL,
) -> List[Document]:
    """
    Bewertet Kandidaten-Dokumente mit einem Cross-Encoder neu und gibt
    die top_n relevantesten zurück, absteigend nach Score sortiert.
    """
    if top_n <= 0:
        raise ValueError("top_n muss größer als 0 sein")
    if not docs:
        return docs

    reranker = get_reranker(model_name=model_name)
    pairs = [(query, doc.page_content) for doc in docs]
    scores = reranker.predict(pairs)

    ranked = sorted(
        zip(scores, docs),
        key=lambda item: item[0],
        reverse=True,
    )
    return [doc for _, doc in ranked[:top_n]]
