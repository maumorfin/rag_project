from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Literal

from langchain_core.documents import Document

from .config import DEFAULT_LLM_MODEL
from .rag import (
    DEFAULT_RERANKER_MODEL,
    _build_context,
    _build_rag_prompt,
    get_docs_for_query,
    get_llm,
)
from .reranking import rerank_documents

# Implementierungsansatz eigenständig erarbeitet; 
# Diskussion und Konkretisierung mit KI-Unterstützung (Claude Code, Anthropic)

def run_rag_for_eval(
    query: str,
    mode: Literal["dense", "bm25", "hybrid"] = "hybrid",
    k: int = 20,
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
    use_reranker: bool = True,
    rerank_top_n: int = 5,
    reranker_model: str = DEFAULT_RERANKER_MODEL,
    llm_model: str = DEFAULT_LLM_MODEL,
) -> Dict[str, Any]:
    """
    RAG-Pipeline für die Evaluation.

    Gibt zusätzlich zu Antwort und Quellen die rohen Chunk-Texte zurück
    (`retrieval_context`), die im Notebook als JSON gespeichert und
    anschließend manuell bewertet werden.
    """
    docs: List[Document] = get_docs_for_query(
        query=query,
        mode=mode,
        k=k,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    if not docs:
        return {
            "answer": "Im Index wurden keine passenden Dokumente gefunden.",
            "retrieval_context": [],
            "sources": [],
        }

    if use_reranker:
        docs = rerank_documents(
            query=query,
            docs=docs,
            top_n=rerank_top_n,
            model_name=reranker_model,
        )

    context = _build_context(docs)
    prompt = _build_rag_prompt(context=context, query=query)
    llm = get_llm(model_name=llm_model, temperature=0.1)
    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "retrieval_context": [doc.page_content for doc in docs],
        "sources": [
            {"source": doc.metadata.get("source"), "page": doc.metadata.get("page")}
            for doc in docs
        ],
    }


def load_questions(path: str | Path) -> List[Dict[str, Any]]:
    """Lädt alle Fragen aus der JSONL-Datei."""
    questions = []
    with Path(path).open("r", encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if line:
                questions.append(json.loads(line))
    return questions
