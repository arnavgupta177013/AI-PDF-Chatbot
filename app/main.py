import shutil
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from pydantic import BaseModel

from . import rag
from .ingest import ingest_pdf

app = FastAPI(title="PDF RAG API")
UPLOADS = Path("uploads")
UPLOADS.mkdir(exist_ok=True)


class AskRequest(BaseModel):
    question: str
    session_id: str = "default"
    collection: str = "default"


@app.post("/upload")
def upload(file: UploadFile = File(...), collection: str = "default"):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(400, "Only PDF files are supported")
    dest = UPLOADS / Path(file.filename).name
    with dest.open("wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"file": dest.name, **ingest_pdf(dest, collection)}


@app.post("/ask")
def ask(req: AskRequest):
    return rag.ask(req.question, req.session_id, req.collection)


@app.post("/reset")
def reset(session_id: str = "default"):
    rag.HISTORY.pop(session_id, None)
    return {"ok": True}
