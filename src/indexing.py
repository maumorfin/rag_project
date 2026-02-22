from __future__ import annotations
from functools import lru_cache
from pathlib import Path
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document
from typing import List
from .config import RAW_DIR, CHROMA_DIR, EMBEDDING_MODEL_NAME
from .processing import IngestConfig, load_and_clean_pdf, split_into_chunks

def clear_retrieval_caches() -> None:
    """Leert In-Memory-Caches für Retriever/Korpus, z. B. nach Rebuilds."""
    get_embedder.cache_clear()
    collect_documents.cache_clear()
    get_corpus_chunks.cache_clear()
    load_index.cache_clear()
    build_bm25_retriever.cache_clear()
    build_dense_retriever.cache_clear()

@lru_cache(maxsize=1)
def get_embedder():
    """Initialisiert das BGE-M3 Embedding-Modell."""
    return HuggingFaceBgeEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        encode_kwargs={"normalize_embeddings": True},
    )

@lru_cache(maxsize=1)
def collect_documents() -> List[Document]:
    """
    Lädt alle PDFs aus data/raw und gibt eine Liste
    gecleanter LangChain-Document-Objekte zurück.
    """
    if not RAW_DIR.exists():
        raise FileNotFoundError(f"RAW_DIR existiert nicht: {RAW_DIR}")

    pdf_files = list(RAW_DIR.rglob("*.pdf"))
    if not pdf_files:
        raise FileNotFoundError(f"Keine PDFs unter {RAW_DIR} gefunden.")

    all_docs: List[Document] = []
    ingest_cfg = IngestConfig()
    for pdf in pdf_files:
        docs, _ = load_and_clean_pdf(pdf, ingest_cfg, verbose=False)
        all_docs.extend(docs)

    return all_docs

@lru_cache(maxsize=8)
def get_corpus_chunks(chunk_size=1200, chunk_overlap=200):
    all_docs = collect_documents()
    chunk_cfg = IngestConfig(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks, _ = split_into_chunks(all_docs, chunk_cfg)
    return chunks


def build_index(
    chroma_dir: Path | None = None,
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
) -> Chroma:
    
    """
    Baut den Chroma-Index aus allen PDFs in RAW_DIR
    und persistiert ihn unter artifacts/chroma_din.
    """
        
    chroma_dir = chroma_dir or CHROMA_DIR
    chroma_dir.parent.mkdir(parents=True, exist_ok=True)

    embedder = get_embedder()
    chunks = get_corpus_chunks(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    vs = Chroma.from_documents(
        documents=chunks,
        embedding=embedder,
        persist_directory=str(chroma_dir),
    )
    vs.persist()
    clear_retrieval_caches()
    return vs

@lru_cache(maxsize=4)
def load_index(chroma_dir: Path | None = None) -> Chroma:
    """
    Lädt einen bestehenden Chroma-Index aus artifacts/chroma_din.
    """
    chroma_dir = chroma_dir or CHROMA_DIR
    embedder = get_embedder()

    vs = Chroma(
        embedding_function=embedder,
        persist_directory=str(chroma_dir),
    )
    return vs

@lru_cache(maxsize=16)
def build_bm25_retriever(
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
    k: int = 10,
) -> BM25Retriever:
    """
    Baut einen BM25-Retriever auf Basis des gesamten Korpus
    (alle PDFs in RAW_DIR, gechunkt).
    
    Achtung: BM25 wird nicht persistiert, sondern bei jedem Aufruf
    neu aus den Chunks aufgebaut.
    """
    chunks = get_corpus_chunks(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    bm25 = BM25Retriever.from_documents(chunks)
    bm25.k = k  # Anzahl der zurückgegebenen Dokumente pro Anfrage
    return bm25

@lru_cache(maxsize=16)
def build_dense_retriever(k: int = 10):
    """
    Baut einen Dense-Retriever auf Basis des bestehenden Chroma-Index.
    """
    vs = load_index()  # nutzt CHROMA_DIR + get_embedder()
    retriever = vs.as_retriever(search_kwargs={"k": k})
    return retriever
