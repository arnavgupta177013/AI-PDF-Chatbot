# PDF RAG Chatbot
LangChain + ChromaDB + Gemini, served with FastAPI, UI in Streamlit.

## Run
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    cp .env.example .env        # add your GOOGLE_API_KEY
    uvicorn app.main:app --reload          # terminal 1
    streamlit run ui.py                    # terminal 2

## Evaluate (run from project root)
    python -m eval.evaluate gen --collection biomed --n 40
    python -m eval.evaluate run --collection biomed
