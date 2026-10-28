from typing import Optional

from langchain_google_genai import ChatGoogleGenerativeAI

from . import config
from .ingest import get_store

llm = ChatGoogleGenerativeAI(model=config.LLM_MODEL, temperature=0.2)
HISTORY: dict = {}  # session_id -> [(role, text)]

CONDENSE = """Given the chat history and a follow-up question, rewrite the follow-up \
as a standalone question. Return only the question.

History:
{history}

Follow-up: {question}"""

ANSWER = """Answer the question using ONLY the context below. If the answer is not in \
the context, say you could not find it in the documents. Cite sources inline like [file.pdf p.3].

Context:
{context}

Question: {question}"""


def _text(msg) -> str:
    c = msg.content
    if isinstance(c, str):
        return c
    return "".join(x if isinstance(x, str) else x.get("text", "") for x in c)


def retrieve(question: str, collection: str = "default", k: Optional[int] = None):
    """Returns [(Document, distance)]. Swap this function to test hybrid/rerank later."""
    return get_store(collection).similarity_search_with_score(question, k=k or config.TOP_K)


def ask(question: str, session_id: str = "default", collection: str = "default") -> dict:
    hist = HISTORY.setdefault(session_id, [])
    standalone = question
    if hist:
        h = "\n".join(f"{r}: {t}" for r, t in hist[-6:])
        standalone = _text(llm.invoke(CONDENSE.format(history=h, question=question))).strip()

    hits = retrieve(standalone, collection)
    context = "\n\n".join(
        f"[{d.metadata['source']} p.{d.metadata['page']}]\n{d.page_content}" for d, _ in hits)
    answer = _text(llm.invoke(ANSWER.format(context=context, question=standalone)))

    hist += [("User", question), ("Assistant", answer)]
    return {
        "answer": answer,
        "standalone_question": standalone,
        "sources": [{"file": d.metadata["source"], "page": d.metadata["page"],
                     "snippet": d.page_content[:300], "distance": float(s)} for d, s in hits],
    }
