from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional, Dict

logger = logging.getLogger(__name__)

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Konfiguration

@dataclass
class IngestConfig:
    skip_first_pages: int = 2
    min_chars: int = 80
    drop_toc: bool = True
    drop_noise_pages: bool = True
    stop_at_references: bool = False
    repair_encoding: bool = True

    chunk_size: int = 1200
    chunk_overlap: int = 200
    dedupe: bool = True
    dedupe_min_chars: int = 120


# Muster / Erkennungsregeln


MATH_CHARS = set("=<>≤≥±∑∫√^→≈≠×÷·")
MOJIBAKE = ("Ã", "â", "Â", "�")

RE_PAGE_NUMBER = re.compile(r"^\s*\d+\s*$", flags=re.MULTILINE)
RE_HYPHEN_BREAK = re.compile(r"(?<=\w)-\n(?=\w)")  
RE_LIST_ITEM = re.compile(r"^\s*([-•*]|\d+[\).:]|[A-Za-z][\):])\s+", flags=re.MULTILINE)

RE_TOC = re.compile(r"(Inhaltsverzeichnis|Abbildungsverzeichnis|Tabellenverzeichnis)", flags=re.IGNORECASE)
RE_REF = re.compile(r"^\s*(Literaturverzeichnis|References|Bibliography|Literatur)\s*$",
                    flags=re.IGNORECASE | re.MULTILINE)
RE_APPENDIX = re.compile(r"^\s*(Anhang|Appendix)\b", flags=re.IGNORECASE)
RE_NOISE_FIRSTLINE = re.compile(r"^\s*(Impressum|Abkürzungsverzeichnis|Abbreviations?|Glossar|Nomenklatur|Danksagung)\b",
                                flags=re.IGNORECASE)


# Hilfsfunktionen

def _to_int(x: object, default: int = 0) -> int:
    try:
        return int(x)
    except (TypeError, ValueError):
        return default


def _mojibake_score(text: str) -> tuple[int, int]:
    bad = sum(text.count(m) for m in MOJIBAKE)
    good = sum(text.count(ch) for ch in ("ä", "ö", "ü", "Ä", "Ö", "Ü", "ß"))
    return bad, -good


def _repair_mojibake(text: str) -> str:
    if not any(m in text for m in MOJIBAKE):
        return text

    candidates = [text]
    for enc in ("latin1", "cp1252"):
        try:
            candidates.append(text.encode(enc).decode("utf-8"))
        except UnicodeError:
            pass

    return min(candidates, key=_mojibake_score)


def _first_line(text: str) -> str:
    for ln in text.splitlines():
        s = ln.strip()
        if s:
            return s
    return ""


def _looks_like_table(text: str) -> bool:
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if len(lines) < 3:
        return False
    sample = lines[:40]
    n = len(sample)
    colish = sum(bool(re.search(r"\s{2,}|\t|\|", ln)) for ln in sample)
    numeric = sum(bool(re.search(r"\d", ln)) for ln in sample)
    return (colish / n > 0.35) or (numeric / n > 0.70)


def _looks_like_formula(text: str) -> bool:
    return sum(ch in MATH_CHARS for ch in text) >= 2


def _looks_like_list(text: str) -> bool:
    return bool(RE_LIST_ITEM.search(text))


def _is_noise_page(text: str) -> bool:
    first = _first_line(text)
    if not first:
        return True
    if RE_NOISE_FIRSTLINE.search(first):
        return True

    # glossary/abbrev-ish: many short lines + many acronyms
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if len(lines) >= 12:
        short_lines = sum(len(ln) <= 28 for ln in lines)
        acronyms = sum(bool(re.fullmatch(r"[A-Z0-9][A-Z0-9\-]{1,12}", ln)) for ln in lines)
        if short_lines / len(lines) > 0.55 and acronyms >= 8:
            return True

    return False


# -----------------------------
# Cleaning
# -----------------------------

def clean_text(text: str, *, repair_encoding: bool = True) -> str:
    """
    Bereinigt PDF-Text und behaelt die Struktur:
    - Absaetze (\n\n) bleiben erhalten
    - Tabellen, Formeln und Listen werden nicht zusammengefasst
    - Nur normaler Fliesstext wird umgebrochen
    """
    t = text.replace("\r\n", "\n").replace("\r", "\n")
    if repair_encoding:
        t = _repair_mojibake(t)

    t = RE_PAGE_NUMBER.sub("", t)
    t = RE_HYPHEN_BREAK.sub("", t)
    t = re.sub(r"\n{3,}", "\n\n", t)

    parts = [p.strip() for p in re.split(r"\n\n+", t) if p.strip()]
    out: list[str] = []

    for p in parts:
        if _looks_like_table(p) or _looks_like_formula(p) or _looks_like_list(p):
            out.append(p)
        else:
            p = re.sub(r"(?<!\n)\n(?!\n)", " ", p)
            p = re.sub(r"[ \t]{2,}", " ", p)
            out.append(p.strip())

    return "\n\n".join(out).strip()


# -----------------------------
# Ingest + split
# -----------------------------

def load_and_clean_pdf(pdf_path: str | Path, cfg: IngestConfig, *, verbose: bool = True) -> tuple[list[Document], Dict[str, int]]:
    """
    Laedt ein PDF und gibt bereinigte Seiten-Dokumente sowie Statistiken zurueck.
    """
    path = Path(pdf_path)
    if not path.is_file():
        raise FileNotFoundError(f"PDF nicht gefunden: {path}")

    loader = PyMuPDFLoader(str(path))
    raw = loader.load()

    # Statistiken zur Nachverfolgung verworfener Seiten
    stats = {
        "raw_pages": len(raw),
        "kept_pages": 0,
        "dropped_front": 0,
        "dropped_toc": 0,
        "dropped_noise": 0,
        "dropped_short": 0,
        "references_pages": 0,
        "appendix_pages": 0,
    }

    docs: list[Document] = []
    section = "body"

    for d in raw:
        page0 = _to_int(d.metadata.get("page"), 0)

        if page0 < cfg.skip_first_pages:
            stats["dropped_front"] += 1
            continue

        cleaned = clean_text(d.page_content, repair_encoding=cfg.repair_encoding)

        if cfg.drop_toc:
            if RE_TOC.search(cleaned):
                stats["dropped_toc"] += 1
                continue
            if len(re.findall(r"\.{5,}", cleaned)) > 5:
                stats["dropped_toc"] += 1
                continue

        if cfg.drop_noise_pages and _is_noise_page(cleaned):
            stats["dropped_noise"] += 1
            continue

        # Abschnittserkennung (Literatur, Anhang)
        first = _first_line(cleaned)
        if RE_REF.search(cleaned):
            section = "references"
            stats["references_pages"] += 1
            if cfg.stop_at_references:
                break
        elif RE_APPENDIX.search(first):
            section = "appendix"
            stats["appendix_pages"] += 1

        if len(cleaned) < cfg.min_chars:
            stats["dropped_short"] += 1
            continue

        docs.append(Document(
            page_content=cleaned,
            metadata={
                "source": path.name,
                "filepath": str(path),
                "page": page0 + 1,
                "doc_id": path.stem.lower(),
                "content_type": "page",
                "section": section,
            }
        ))
        stats["kept_pages"] += 1

    if verbose:
        print(f"[ingest] {path.name}: kept {stats['kept_pages']}/{stats['raw_pages']} pages "
              f"(front {stats['dropped_front']}, toc {stats['dropped_toc']}, "
              f"noise {stats['dropped_noise']}, short {stats['dropped_short']})")

    return docs, stats


def split_into_chunks(pages: list[Document], cfg: IngestConfig) -> tuple[list[Document], Dict[str, int]]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=cfg.chunk_size,
        chunk_overlap=cfg.chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
        length_function=len,
    )
    chunks = splitter.split_documents(pages)

    if not cfg.dedupe:
        return chunks, {"chunks": len(chunks), "deduped": 0}

    unique: list[Document] = []
    seen: set[tuple[Optional[str], str]] = set()
    deduped = 0

    for c in chunks:
        norm = re.sub(r"\s+", " ", c.page_content).strip().lower()
        if len(norm) < cfg.dedupe_min_chars:
            unique.append(c)
            continue

        key = (c.metadata.get("filepath"), norm)  # filepath eindeutiger als source
        if key in seen:
            deduped += 1
            continue

        seen.add(key)
        unique.append(c)

    return unique, {"chunks": len(unique), "deduped": deduped}


# JSONL-Hilfsfunktionen

def save_jsonl(docs: Iterable[Document], out_path: str | Path) -> None:
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for d in docs:
            f.write(json.dumps({"page_content": d.page_content, "metadata": d.metadata}, ensure_ascii=False) + "\n")


def load_jsonl(in_path: str | Path) -> list[Document]:
    path = Path(in_path)
    docs: list[Document] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            docs.append(Document(page_content=obj["page_content"], metadata=obj["metadata"]))
    return docs

