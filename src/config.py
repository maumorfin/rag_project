# src/config.py
from pathlib import Path

# Projekt-Root (eine Ebene über src/)
ROOT = Path(__file__).resolve().parents[1]

# Datenpfade
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"

# Artefakte (Vectorstore etc.)
ARTIFACTS_DIR = ROOT / "artifacts"
CHROMA_DIR = ARTIFACTS_DIR / "chroma_din"  # Name bei Bedarf ändern

# Default-Embedding-Modell
EMBEDDING_MODEL_NAME = "BAAI/bge-m3"

# Default-LLM für RAG
DEFAULT_LLM_MODEL = "llama3.1:8b"
