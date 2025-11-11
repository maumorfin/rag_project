# Hybrid RAG (DE/EN) – BGE-M3 + BM25, Chroma→FAISS


Minimaler RAG-Stack für deutsch/englische Dokumente. Start lokal mit Chroma, später Migration auf FAISS und optional Re-Ranking.


## Features
- BGE-M3 Embeddings (mehrsprachig)
- Hybrid Retrieval (BM25 + Dense) mit RRF-Fusion
- Start: Chroma; Migration: FAISS
- Optional: bge-reranker-v2
- VS Code + Jupyter Friendly


## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env