import requests
import streamlit as st

API = "http://localhost:8000"
st.set_page_config(page_title="PDF Chatbot", page_icon="📄")
st.title("📄 Chat with your PDFs")

if "msgs" not in st.session_state:
    st.session_state.msgs = []

with st.sidebar:
    collection = st.text_input("Collection", "default")
    files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
    if st.button("Index") and files:
        for f in files:
            r = requests.post(f"{API}/upload", params={"collection": collection},
                              files={"file": (f.name, f.getvalue(), "application/pdf")})
            st.write(f"{f.name}: {r.json() if r.ok else r.text}")
    if st.button("New chat"):
        requests.post(f"{API}/reset")
        st.session_state.msgs = []

for m in st.session_state.msgs:
    with st.chat_message(m["role"]):
        st.markdown(m["text"])

if q := st.chat_input("Ask about your documents"):
    st.session_state.msgs.append({"role": "user", "text": q})
    with st.chat_message("user"):
        st.markdown(q)
    r = requests.post(f"{API}/ask", json={"question": q, "collection": collection})
    if r.ok:
        d = r.json()
        with st.chat_message("assistant"):
            st.markdown(d["answer"])
            with st.expander("Sources"):
                for s in d["sources"]:
                    st.markdown(f"**{s['file']} — p.{s['page']}**")
                    st.caption(s["snippet"])
        st.session_state.msgs.append({"role": "assistant", "text": d["answer"]})
    else:
        st.error(r.text)
