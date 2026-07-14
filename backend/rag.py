# backend/rag.py
"""
RAG Pipeline

Responsible for:
1. Retrieving relevant document chunks
2. Constructing the prompt
3. Sending the prompt to the LLM
4. Returning the generated response
"""

from vector_store import get_vector_store
from llm import get_llm


class RAGPipeline:
    def __init__(self):

        self.vector_db = get_vector_store()
        self.llm = get_llm()

    def ask(self, question: str):

        # -------------------------
        # Retrieve Relevant Chunks
        # -------------------------
        documents = self.vector_db.similarity_search(
            question,
            k=4
        )

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        # -------------------------
        # Prompt
        # -------------------------
        prompt = f"""
You are an intelligent AI assistant.

Answer the user's question ONLY using the provided context.

If the answer cannot be found,
say that the document does not contain enough information.

Context:
{context}

Question:
{question}

Answer:
"""

        # -------------------------
        # Generate Answer
        # -------------------------
        response = self.llm.invoke(prompt)

        return {
            "answer": response.content,
            "sources": [
                doc.metadata
                for doc in documents
            ]
        }
