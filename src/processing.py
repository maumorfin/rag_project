from langchain_community.document_loaders import PyPDFLoader # Langchain PDF Loader change if necessary
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import re
from pathlib import Path


def text_formatter(text: str) -> str:
    """Format text function to clean up extracted text."""

    # Add if neccessary more formatting steps
    # Getting rid of multiple new lines
    text = re.sub(r"\n+", " ", text)
    
    return text.strip()

def read_pdf(pdf_path: str | Path):
    """Read PDF and return list of cleaned pages."""
    pdf_path = Path(pdf_path)
    loader = PyPDFLoader(str(pdf_path))

    raw_docs = loader.load()   # List[Document]

    cleaned_docs = []

    for d in raw_docs:
        page_number = d.metadata.get("page", None)

        cleaned_text = text_formatter(d.page_content)

        new_doc = Document(
            page_content=cleaned_text,
            metadata={
                "source": pdf_path.name,          # filename
                "filepath": str(pdf_path),        # full path
                "page": page_number + 1,              # page number
                #"doctype": "norm",                # optional
                "doc_id": pdf_path.stem.lower(),  # e.g. "din_5566_2"
            }
        )

        cleaned_docs.append(new_doc)

    return cleaned_docs

#Chunking the documents
def chunk_documents(docs: list[Document], chunk_size: int = 1000, chunk_overlap: int = 200):
    
    """Split cleaned documents into smaller pieces while preserving metadata."""

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,                       #The metadata will be passed with langchain to the chunks 
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    chunks = text_splitter.split_documents(docs)
    return chunks
