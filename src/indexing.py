from pathlib import Path
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from typing import List
from .config import RAW_DIR, CHROMA_DIR, EMBEDDING_MODEL_NAME
from .processing import read_pdf, chunk_documents

def get_embedder():
    """Initialisiert das BGE-M3 Embedding-Modell."""
    return HuggingFaceBgeEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        encode_kwargs={"normalize_embeddings": True},
    )

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
    for pdf in pdf_files:
        docs = read_pdf(pdf)
        all_docs.extend(docs)

    return all_docs

def build_index(
    chroma_dir: Path | None = None,
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
) -> Chroma:
    """
    Baut den Chroma-Index aus allen PDFs in data/raw
    und persistiert ihn unter artifacts/chroma_din.
    """
    chroma_dir = chroma_dir or CHROMA_DIR
    chroma_dir.parent.mkdir(parents=True, exist_ok=True)

    embedder = get_embedder()
    all_docs = collect_documents()
    chunks = chunk_documents(all_docs, chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    vs = Chroma.from_documents(
        documents=chunks,
        embedding=embedder,
        persist_directory=str(chroma_dir),
    )
    vs.persist()
    return vs

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