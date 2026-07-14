# AI PDF Chatbot using RAG & LangChain

🚧 **Status:** Work in Progress

This project is currently under active development as part of my learning in Retrieval-Augmented Generation (RAG), LangChain, FastAPI, and Generative AI.

## Planned Features

- PDF upload
- Text extraction
- Vector embeddings
- ChromaDB vector store
- LangChain RAG pipeline
- Gemini API integration
- FastAPI backend
- Streamlit frontend
- Conversational memory
- Docker deployment

## Tech Stack

- Python
- LangChain
- ChromaDB
- Gemini API
- FastAPI
- Streamlit
- Docker

## Roadmap

- [ ] PDF ingestion
- [ ] Text chunking
- [ ] Embedding generation
- [ ] Vector database integration
- [ ] RAG pipeline
- [ ] Chat interface
- [ ] Docker support
---

# ⚙️ Architecture

```text
PDF Upload
      │
      ▼
PDF Text Extraction
      │
      ▼
Text Chunking
      │
      ▼
Embedding Generation
      │
      ▼
ChromaDB Vector Database
      │
      ▼
Relevant Context Retrieval
      │
      ▼
LangChain
      │
      ▼
Gemini API
      │
      ▼
Response with Source Citations
```

---

# 🛠️ Tech Stack

### Programming

- Python

### Generative AI

- LangChain
- Gemini API
- Prompt Engineering

### Retrieval

- ChromaDB
- Retrieval-Augmented Generation (RAG)

### Backend

- FastAPI
- REST APIs

### Frontend

- Streamlit

### Document Processing

- PyMuPDF *(or PyPDF2, depending on your implementation)*

---

# 🚀 How It Works

1. Upload one or more PDF documents.
2. Extract text from the uploaded files.
3. Split the text into smaller chunks.
4. Convert chunks into vector embeddings.
5. Store embeddings in ChromaDB.
6. Retrieve the most relevant chunks for a user's query.
7. Pass the retrieved context to the Gemini API through LangChain.
8. Generate an accurate answer with supporting document context.



# 📈 Future Improvements

- Multi-document search
- Voice input and output
- OCR support for scanned PDFs
- Multi-agent workflow using LangGraph
- User authentication
- Docker deployment
- Cloud deployment (AWS/GCP/Azure)

---

# 👨‍💻 Author

**Arnav Gupta**

- LinkedIn: https://www.linkedin.com/in/arnavgupta1470
- GitHub: https://github.com/arnavgupta177013
