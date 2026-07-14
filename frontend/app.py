# frontend/app.py

import streamlit as st
import requests

# -----------------------------
# Configuration
# -----------------------------
API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("📄 AI PDF Chatbot")
    st.write(
        "Upload one or more PDF documents and ask questions using "
        "Retrieval-Augmented Generation (RAG)."
    )

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:
        if st.button("Process PDF"):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            try:
                response = requests.post(
                    f"{API_URL}/upload",
                    files=files
                )

                if response.status_code == 200:
                    st.success("PDF processed successfully!")
                else:
                    st.error(response.text)

            except Exception:
                st.error("Backend server is not running.")

# -----------------------------
# Chat Section
# -----------------------------
st.title("💬 Chat with your PDF")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    try:

        response = requests.post(
            f"{API_URL}/chat",
            json={
                "question": question
            }
        )

        if response.status_code == 200:

            answer = response.json()["answer"]

        else:

            answer = "Something went wrong."

    except Exception:

        answer = "Backend server is not running."

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)
