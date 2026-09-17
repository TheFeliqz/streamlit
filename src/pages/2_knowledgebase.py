import streamlit as st
from services.ingest import ingest
from services.answer import answer


# File Uploader
uploaded_files = st.file_uploader("Upload File(s) to build knowledge base here",accept_multiple_files=True)

# Ingest
if st.button("Ingest"):
    if not uploaded_files:
        st.warning("Please select at least one file.")
    else:
        with st.spinner("Ingesting..."):
            ingest(uploaded_files)

        st.success("Files ingested")

# Question
question = st.text_input("Ask a question fitting the information in the knowledge base")

if st.button("Answer"):
    if not question:
        st.warning("Please enter a question")
    else:
        with st.spinner("Answering..."):
            response = answer(question)

        st.success("Done")
        st.write(response)