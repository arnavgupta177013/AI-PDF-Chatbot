from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from . import config


def get_store(collection: str = "default") -> Chroma:
    emb = GoogleGenerativeAIEmbeddings(model=config.EMBED_MODEL)
    return Chroma(collection_name=collection, embedding_function=emb,
                  persist_directory=config.CHROMA_DIR)


def ingest_pdf(path, collection: str = "default") -> dict:
    name = Path(path).name
    pages = PyPDFLoader(str(path)).load()
    for p in pages:
        p.metadata["source"] = name
        p.metadata["page"] = int(p.metadata.get("page", 0)) + 1  # 1-indexed for humans
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP)
    chunks = splitter.split_documents(pages)
    ids = [f"{collection}:{name}:{i}" for i in range(len(chunks))]  # re-upload = overwrite
    get_store(collection).add_documents(chunks, ids=ids)
    return {"pages": len(pages), "chunks": len(chunks)}
