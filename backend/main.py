# backend/main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import shutil

app = FastAPI(title="AI PDF Chatbot API")

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# -----------------------------
# Request Model
# -----------------------------
class ChatRequest(BaseModel):
    question: str


# -----------------------------
# Upload PDF
# -----------------------------
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF file.

    TODO:
    - Extract text
    - Chunk document
    - Generate embeddings
    - Store in ChromaDB
    """

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "status": "success",
        "filename": file.filename,
        "message": "PDF uploaded successfully."
    }


# -----------------------------
# Chat
# -----------------------------
@app.post("/chat")
async def chat(request: ChatRequest):
    """
    Chat endpoint.

    TODO:
    - Retrieve relevant document chunks
    - Build prompt
    - Query Gemini
    - Return answer with citations
    """

    answer = (
        "Backend is connected successfully.\n\n"
        f"You asked:\n\n'{request.question}'\n\n"
        "The RAG pipeline will be integrated here."
    )

    return {
        "answer": answer
    }


# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
async def root():
    return {
        "status": "running",
        "service": "AI PDF Chatbot Backend"
    }
