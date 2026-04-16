# RAG-System für domänenspezifische Wissensabfrage

Dieses Projekt entstand im Rahmen einer **Bachelorarbeit** im Fachgebiet **Schienenfahrzeugtechnik**. Ziel war es, ein großes Sprachmodell (LLM) so anzupassen, dass es präzise und nachvollziehbare Antworten auf domänenspezifische Fragen aus technischen Dokumenten liefern kann – und das vollständig **lokal**, ohne externe APIs oder Cloud-Dienste.

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
| LLM | Ollama (`llama3.1:8b`, lokal) |
| PDF-Verarbeitung | PyMuPDF |

---

## Voraussetzungen

- [Ollama](https://ollama.ai) installiert und das gewünschte Modell heruntergeladen:
  ```bash
  ollama pull llama3.1:8b
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

Im Notebook `notebooks/build_index.ipynb` ausführen oder direkt in Python:

```python
from src.indexing import build_index
build_index()
```

### 3. Fragen stellen

Das Haupt-Notebook `notebooks/rag_playground.ipynb` öffnen:

- `QUESTION_ID` auf eine Frage aus `data/eval/questions.jsonl` setzen
- `QUERY_TYPE` je nach Fragetyp wählen:

```python
QUERY_TYPE = 'focused'      # Einfache, konkrete Frage  → 3 Chunks
QUERY_TYPE = 'normal'       # Standardfrage             → 5 Chunks
QUERY_TYPE = 'cross_domain' # Themenübergreifende Frage → 7 Chunks
```

- Alle Zellen ausführen

---

## Projektstruktur

```
rag_project/
├── src/
│   ├── config.py        # Pfade und Standard-Konfiguration
│   ├── processing.py    # PDF laden, bereinigen, chunken
│   ├── indexing.py      # Vektorindex und Retriever aufbauen
│   ├── hybrid.py        # Hybrid-Retrieval mit RRF-Fusion
│   ├── reranking.py     # Cross-Encoder Reranking
│   └── rag.py           # RAG-Pipeline und LLM-Integration
├── notebooks/
│   ├── build_index.ipynb      # Index erstellen
│   ├── processing.ipynb       # Datenverarbeitung erkunden
│   └── rag_playground.ipynb   # Interaktives Testen
├── data/
│   ├── raw/             # PDF-Quelldokumente (nicht im Repository)
│   ├── chunks/          # Gecachte Chunks (JSONL)
│   ├── clean_pages/     # Bereinigte Seiten (JSONL)
│   └── eval/            # Testfragen (questions.jsonl)
├── artifacts/
│   └── chroma/          # Persistierter Vektorindex (nicht im Repository)
├── environment.yml
├── requirements.txt
└── README.md
```

---

## Konfiguration

Die wichtigsten Parameter befinden sich in `notebooks/rag_playground.ipynb`:

| Parameter | Standard | Beschreibung |
|---|---|---|
| `RAG_MODE` | `hybrid` | Retrieval-Modus: `dense`, `bm25`, `hybrid` |
| `RAG_K` | `20` | Anzahl Kandidaten für den Reranker |
| `QUERY_TYPE` | `focused` | Bestimmt `RERANK_TOP_N` (3 / 5 / 7) |
| `USE_RERANKER` | `True` | Reranking aktivieren/deaktivieren |
| `CHUNK_SIZE` | `1200` | Zeichenlänge pro Chunk |
| `CHUNK_OVERLAP` | `200` | Überlappung zwischen Chunks |

Modell und Pfade werden zentral in `src/config.py` verwaltet.

---

## Hinweise

- Das System ist vollständig **offline** lauffähig. Es werden keine Daten an externe Dienste gesendet.
- Beim ersten Start werden die Modelle (`bge-m3`, `bge-reranker-v2-m3`) automatisch von HuggingFace heruntergeladen und lokal gecacht.
- Nach Änderungen an den PDF-Dokumenten muss der Index mit `REBUILD_INDEX = True` neu aufgebaut werden.
