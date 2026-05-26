# RAG-System für domänenspezifische Wissensabfrage

Dieses Projekt entstand im Rahmen einer **Bachelorarbeit** im Fachgebiet **Schienenfahrzeugtechnik**. Ziel war es, ein großes Sprachmodell (LLM) so anzupassen, dass es präzise und nachvollziehbare Antworten auf domänenspezifische Fragen aus technischen Dokumenten liefern kann und das vollständig **lokal**, ohne externe APIs oder Cloud-Dienste.

---

## Hintergrund und Motivation

Große Sprachmodelle wie GPT oder LLaMA besitzen umfangreiches Allgemeinwissen, kennen jedoch keine projektspezifischen oder institutionellen Dokumente. Ein Fine-Tuning des Modells ist aufwendig und erfordert große Datenmengen.

**Retrieval-Augmented Generation (RAG)** löst dieses Problem, indem relevante Textpassagen aus eigenen Dokumenten gesucht und dem Modell als Kontext übergeben werden. Das Modell antwortet dann ausschließlich auf Basis dieses Kontexts – ohne externes Wissen zu erfinden.

Da im Bereich der Schienenfahrzeugtechnik oft mit vertraulichen oder internen Dokumenten gearbeitet wird, war ein **vollständig lokaler Betrieb** eine zentrale Anforderung.

---

## Was das System macht

Das System verarbeitet PDF-Dokumente und ermöglicht anschließend die gezielte Abfrage ihres Inhalts über natürlichsprachliche Fragen.

### Pipeline

```
PDF-Dokumente
     │
     ▼
Laden & Bereinigen        ← Rauschen, Kopfzeilen, Inhaltsverzeichnisse entfernen
     │
     ▼
Chunking                  ← Aufteilung in überlappende Textabschnitte
     │
     ├──────────────────────────────────┐
     ▼                                  ▼
Chroma-Vektorindex               BM25-Index
(Embedding-basiert)              (Schlüsselwort-basiert)
     │                                  │
     └──────────────┬───────────────────┘
                    ▼
           Hybrid-Retrieval              ← RRF-Fusion beider Ergebnisse
                    │
                    ▼
            Reranking                   ← Cross-Encoder bewertet Relevanz neu
                    │
                    ▼
          LLM (lokal via Ollama)        ← Antwort auf Basis der besten Chunks
                    │
                    ▼
              Antwort + Quellen
```

### Retrieval-Modi

| Modus | Beschreibung |
|---|---|
| `dense` | Semantische Suche über Embeddings (BGE-M3) |
| `bm25` | Schlüsselwortbasierte Suche |
| `hybrid` | Kombination beider Modi über Reciprocal Rank Fusion (RRF) |

Das optionale **Reranking** mit einem Cross-Encoder-Modell bewertet die gefundenen Chunks nochmals und wählt die relevantesten aus.

---

## Technologie-Stack

| Komponente | Technologie |
|---|---|
| Sprache | Python 3.11 |
| RAG-Framework | LangChain |
| Vektordatenbank | ChromaDB |
| Embeddings | `BAAI/bge-m3` (lokal, mehrsprachig) |
| Schlüsselwortsuche | BM25 (`rank-bm25`) |
| Reranker | `BAAI/bge-reranker-v2-m3` (Cross-Encoder) |
| LLM | Ollama (`llama3.1:8b` oder `mistral-nemo`, lokal) |
| PDF-Verarbeitung | PyMuPDF |

---

## Voraussetzungen

- [Ollama](https://ollama.ai) installiert und das gewünschte Modell heruntergeladen:
  ```bash
  ollama pull llama3.1:8b
  # oder alternativ:
  ollama pull mistral-nemo
  ```
- Conda (empfohlen) oder Python 3.11+
- Ca. 8 GB RAM für das LLM, zusätzlich ~2 GB für Embeddings und Reranker

---

## Installation

```bash
# 1. Repository klonen
git clone <repo-url>
cd rag_project

# 2. Conda-Umgebung erstellen (empfohlen)
conda env create -f environment.yml
conda activate rag_project

# Alternativ: pip
pip install -r requirements.txt
```

---

## Verwendung

### 1. PDF-Dokumente hinzufügen

PDFs in den Ordner `data/raw/` legen.

### 2. Index aufbauen

Direkt in Python:

```python
from src.indexing import build_index
build_index()
```

### 3. Fragen stellen

Das Haupt-Notebook `notebooks/rag_playground.ipynb` öffnen, Frage und Parameter konfigurieren und alle Zellen ausführen.

---

## Projektstruktur

```
rag_project/
├── src/
│   ├── config.py        # Zentrale Konfiguration (Pfade, Modelle)
│   ├── processing.py    # PDF-Verarbeitung: laden, bereinigen, chunken
│   ├── indexing.py      # Index aufbauen/laden, Retriever, Caching
│   ├── hybrid.py        # Hybrid-Retrieval mit gewichteter RRF-Fusion
│   ├── reranking.py     # Cross-Encoder Reranking
│   ├── rag.py           # RAG-Pipeline: Retrieval → Prompt → LLM
│   └── evaluation.py   # Hilfsfunktionen für die Evaluation
├── notebooks/
│   ├── build_index.ipynb      # Entwicklungsnotebook (Index-Aufbau)
│   ├── proccesing.ipynb       # Entwicklungsnotebook (PDF-Verarbeitung)
│   ├── rag_playground.ipynb   # Interaktives Testen der Pipeline
│   └── evaluation.ipynb       # RAG ausführen → JSON + Markdown-Report
├── data/
│   ├── raw/             # PDF-Quelldokumente (nicht im Repository)
│   └── eval/            # Evaluationsdaten (Fragen + Ergebnisse)
├── artifacts/
│   └── chroma/          # Persistierter Vektorindex (nicht im Repository)
├── environment.yml
├── requirements.txt
└── README.md
```

---

## Modulübersicht (`src/`)

### `config.py`
Zentrale Stelle für alle Pfade und Standardwerte. Wer Modell oder Pfade ändern will, macht das hier.

```python
DEFAULT_LLM_MODEL = "llama3.1:8b"            # Ollama-Modell
EMBEDDING_MODEL_NAME = "BAAI/bge-m3"
RERANKER_MODEL_NAME = "BAAI/bge-reranker-v2-m3"
PROMPT_VERSION = "llama"                     # "llama" oder "mistral"
CHROMA_DIR = ...                             # Wo der Vektorindex gespeichert wird
RAW_DIR = ...                                # Wo die PDF-Quelldateien liegen
```

---

### `processing.py`
Liest PDFs ein, bereinigt den Text und teilt ihn in Chunks auf.

**Wichtige Funktionen:**
- `load_and_clean_pdf(pdf_path, cfg)` — lädt eine PDF-Datei, entfernt Rauschen (Seitenzahlen, Inhaltsverzeichnisse, Kopfzeilen), gibt bereinigte `Document`-Objekte zurück
- `split_into_chunks(pages, cfg)` — teilt Seiten in überlappende Chunks auf, entfernt Duplikate
- `IngestConfig` — Dataclass mit allen Verarbeitungsparametern (`chunk_size`, `chunk_overlap`, `skip_first_pages`, ...)

**Ablauf:**
```
PDF → PyMuPDFLoader → clean_text() → split_into_chunks() → [Document, ...]
```

---

### `indexing.py`
Baut den ChromaDB-Vektorindex auf und stellt Retriever bereit. Alle teuren Operationen (Embedder laden, Dokumente lesen, Index laden) sind mit `@lru_cache` gecacht — innerhalb einer Session werden sie nur einmal ausgeführt.

**Wichtige Funktionen:**
- `build_index()` — erstellt den ChromaDB-Index aus allen PDFs in `RAW_DIR` und speichert ihn auf Disk. Nur einmalig nötig.
- `load_index()` — lädt den bestehenden Index (gecacht)
- `build_bm25_retriever()` — erstellt einen BM25-Retriever aus den Chunks (gecacht, nicht auf Disk persistiert)
- `build_dense_retriever()` — erstellt einen Dense-Retriever auf Basis des Chroma-Index (gecacht)
- `clear_retrieval_caches()` — leert alle Caches, z.B. nach einem Index-Rebuild

---

### `hybrid.py`
Kombiniert BM25 und Dense Retrieval über gewichtete Reciprocal Rank Fusion (RRF).

**Wichtige Funktion:**
- `hybrid_retrieve(query, k, weights, ...)` — ruft beide Retriever auf, vergibt jedem Chunk einen kombinierten Score nach der Formel `w / (k0 + rank)` und gibt die Top-k Dokumente zurück

```
BM25-Ergebnisse  ──┐
                   ├─► RRF-Score ─► Top-k Dokumente
Dense-Ergebnisse ──┘
```

Standard-Gewichtung: `weights=(0.5, 0.5)` — beide Verfahren gleichwertig.

---

### `reranking.py`
Bewertet eine Kandidatenmenge mit einem Cross-Encoder-Modell neu. Anders als Bi-Encoder-basierte Retriever (Dense) analysiert der Cross-Encoder Anfrage und Chunk **gemeinsam** und vergibt einen direkten Relevanz-Score.

**Wichtige Funktion:**
- `rerank_documents(query, docs, top_n)` — gibt die `top_n` relevantesten Chunks zurück, absteigend nach Score sortiert

Standardmodell: `BAAI/bge-reranker-v2-m3` (mehrsprachig, selbe Modellfamilie wie BGE-M3).

---

### `rag.py`
Orchestriert die gesamte RAG-Pipeline: Retrieval → optionales Reranking → Prompt-Aufbau → LLM-Aufruf.

**Wichtige Funktionen:**
- `answer_with_rag_mode(query, mode, ...)` — Hauptfunktion: führt die komplette Pipeline aus und gibt Antwort + Quellen zurück
- `get_docs_for_query(query, mode, k, ...)` — nur Retrieval, ohne LLM (nützlich zum Debuggen)

**Prompt-Varianten** (umschaltbar über `PROMPT_VERSION` in `config.py`):
- `"llama"` — Prompt optimiert für `llama3.1:8b`
- `"mistral"` — Prompt optimiert für `mistral-nemo`

---

### `evaluation.py`
Hilfsfunktionen für die Evaluation der Pipeline.

**Wichtige Funktionen:**
- `run_rag_for_eval(query, ...)` — wie `answer_with_rag_mode`, gibt zusätzlich die rohen Chunk-Texte (`retrieval_context`) zurück
- `load_questions(path)` — liest Fragen aus einer JSONL-Datei ein

---

## Konfiguration

**`src/config.py`** — globale Einstellungen (Modell, Pfade):

| Parameter | Standard | Beschreibung |
|---|---|---|
| `DEFAULT_LLM_MODEL` | `llama3.1:8b` | Ollama-Modell für die Antwortgenerierung |
| `PROMPT_VERSION` | `llama` | Prompt-Variante: `llama` oder `mistral` |
| `EMBEDDING_MODEL_NAME` | `BAAI/bge-m3` | Embedding-Modell für den Vektorindex |
| `RERANKER_MODEL_NAME` | `BAAI/bge-reranker-v2-m3` | Cross-Encoder-Modell für das Reranking |
| `CHROMA_DIR` | `artifacts/chroma` | Speicherort des Vektorindex |
| `RAW_DIR` | `data/raw` | Ordner mit den PDF-Quelldokumenten |

**`notebooks/rag_playground.ipynb`** — Parameter für interaktive Tests:

| Parameter | Standard | Beschreibung |
|---|---|---|
| `RAG_MODE` | `hybrid` | Retrieval-Modus: `dense`, `bm25`, `hybrid` |
| `RAG_K` | `20` | Anzahl Kandidaten für den Reranker |
| `QUERY_TYPE` | `normal` | Bestimmt `RERANK_TOP_N` (`focused`=3, `normal`=5, `cross_domain`=7) |
| `USE_RERANKER` | `True` | Reranking aktivieren/deaktivieren |
| `CHUNK_SIZE` | `1200` | Zeichenlänge pro Chunk |
| `CHUNK_OVERLAP` | `200` | Überlappung zwischen Chunks |

**`notebooks/evaluation.ipynb`** — Parameter für die Evaluation:

| Parameter | Standard | Beschreibung |
|---|---|---|
| `MODEL_CHOICE` | `llama` | Modell-Auswahl: `llama` (llama3.1:8b) oder `mistral` (mistral-nemo) |
| `RAG_MODE` | `hybrid` | Retrieval-Modus |
| `RAG_K` | `20` | Anzahl Kandidaten für den Reranker |
| `USE_RERANKER` | `True` | Reranking aktivieren/deaktivieren |
| `RERANK_TOP_N` | `5` | Anzahl der Chunks nach dem Reranking |
| `QUESTION_IDS` | `None` | Bestimmte Fragen auswählen (`None` = alle) |

---

## Hinweise

- Das System ist vollständig **offline** lauffähig. Es werden keine Daten an externe Dienste gesendet.
- Beim ersten Start werden die Modelle (`bge-m3`, `bge-reranker-v2-m3`) automatisch von HuggingFace heruntergeladen und lokal gecacht.
- Nach Änderungen an den PDF-Dokumenten muss der Index mit `REBUILD_INDEX = True` neu aufgebaut werden.
