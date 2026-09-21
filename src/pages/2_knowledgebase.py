import streamlit as st

from services.ingest import ingest
from services.answer import answer
from components.vector_store import clear_vector_store

st.markdown("## Add files to the Knowledge Base")

# File Uploader
uploaded_files = st.file_uploader("Upload File(s) to build knowledge base here",accept_multiple_files=True, type=["txt", "md"])

# Ingest
if st.button("Ingest"):
    if not uploaded_files:
        st.warning("Please select at least one file.")
    else:
        with st.spinner("Ingesting..."):
            ingest(uploaded_files)

        st.success("Files ingested")



st.markdown("## Delete files from the Knowledge Base")

# Overview of files stored in vector store
# add storing source document of a chunk into the vector store and then write all unique document names 
pass

import streamlit as st

# Confirmation window to delete Knowledge Base
@st.dialog("Confirm deletion")
def confirm_delete():
    st.write("Are you sure you want to delete this collection?")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Yes, delete"):
            clear_vector_store()
            st.rerun()
    with col2:
        if st.button("Cancel"):
            st.rerun()

if st.button("Delete collection"):
    confirm_delete()



st.markdown("## Ask a Question to the Knowledge Base")

col1, col2 = st.columns(2)

# Question
with col1:
    question = st.text_input("Ask a question for the information in the knowledge base")

# Selection for how hard the question is
with col2:
    complexity = st.pills(
        "Complexity of your question",
        ["Easy", "Medium", "Hard"],
        default="Easy",
        required=True
    )

# Answer Button
if st.button("Answer"):
    if not question:
        st.warning("Please enter a question")
    else:
        with st.spinner("Answering..."):
            response = answer(question, complexity)

        st.success("Done")
        st.write(response)
