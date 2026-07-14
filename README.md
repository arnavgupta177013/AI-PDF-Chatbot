# AI-PDF-Chatbot
# 📄 AI PDF Chatbot using RAG & LangChain

An AI-powered document question-answering system that enables users to upload PDF documents and ask natural language questions. The application leverages **Retrieval-Augmented Generation (RAG)** to retrieve relevant document context before generating accurate, context-aware responses using a Large Language Model.

---

# 🎯 Motivation

Large Language Models often struggle with answering questions about private or domain-specific documents because they lack access to that information.

This project solves that problem by implementing a **Retrieval-Augmented Generation (RAG)** pipeline, allowing the chatbot to retrieve relevant information directly from uploaded PDFs before generating responses.

---

# ✨ Features

- Upload one or more PDF documents
- Context-aware question answering using RAG
- Semantic search using vector embeddings
- Conversational memory for follow-up questions
- Source citations for generated responses
- FastAPI backend with Streamlit web interface
- Real-time document processing

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
