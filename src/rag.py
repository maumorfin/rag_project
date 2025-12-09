from langchain_community.chat_models import ChatOllama
from langchain_core.vectorstores import VectorStore
from .config import DEFAULT_LLM_MODEL
from typing import Any, Dict, List

def answer_with_rag(
    query: str,
    vs: VectorStore,
    model_name: str = DEFAULT_LLM_MODEL,
    k: int = 3,
) -> Dict[str, Any]:
    """
    Einfacher RAG-Helper:
    - holt k relevante Chunks aus dem Vectorstore
    - baut einen Kontext
    - ruft ein lokales LLM (Ollama) auf
    - gibt Antwort + Quellen zurück
    """
    retriever = vs.as_retriever(search_kwargs={"k": k})
    docs = retriever.invoke(query)

    if not docs:
        return {
            "answer": "Im Index wurden keine passenden Dokumente gefunden.",
            "sources": [],
        }

    # Kontext aus den gefundenen Chunks bauen
    context_blocks: List[str] = []
    for d in docs:
        src = d.metadata.get("source")
        page = d.metadata.get("page")
        context_blocks.append(
            f"[Quelle: {src}, Seite {page}]\n{d.page_content}"
        )

    context = "\n\n".join(context_blocks)

    prompt = f"""
Du bist ein Experte für technische Normen.

Nutze AUSSCHLIESSLICH den folgenden Kontext, um die Frage zu beantworten.
Wenn die Antwort NICHT im Kontext steht, antworte GENAU mit:
"Die Information ist im bereitgestellten Dokument nicht enthalten."

KONTEXT:
{context}

FRAGE:
{query}

ANTWORT (auf Deutsch, sachlich, präzise, höchstens 5 Sätze):
"""

    llm = ChatOllama(model=model_name, temperature=0.1)
    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": [
            {
                "source": d.metadata.get("source"),
                "page": d.metadata.get("page"),
                "filepath": d.metadata.get("filepath"),
            }
            for d in docs
        ],
    }

def debug_retrieval(query: str, vs: VectorStore, k: int = 3) -> None:
    """
    Kleiner Helper, um im Notebook zu prüfen,
    welche Chunks für eine Query gefunden werden.
    """
    retriever = vs.as_retriever(search_kwargs={"k": k})
    docs = retriever.invoke(query)

    print("Anzahl gefundener Dokumente:", len(docs))
    for i, d in enumerate(docs):
        print(f"\n--- Doc {i} ---")
        print("Source:", d.metadata.get("source"))
        print("Page:", d.metadata.get("page"))
        print(d.page_content[:400], "...")