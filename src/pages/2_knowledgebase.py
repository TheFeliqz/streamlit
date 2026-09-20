import streamlit as st
from services.ingest import ingest
from services.answer import answer

# File Uploader
uploaded_files = st.file_uploader("Upload File(s) to build knowledge base here",accept_multiple_files=True, type=["txt", "md"])

if uploaded_files is not None:
    # Text preview (to check what the user uploaded)
    for file in uploaded_files:
        st.text_area(
            "Document Preview",
            file.getvalue().decode("utf-8"),
            height=200,
            disabled=True
        )

# Ingest
if st.button("Ingest"):
    if not uploaded_files:
        st.warning("Please select at least one file.")
    else:
        with st.spinner("Ingesting..."):
            ingest(uploaded_files)

        st.success("Files ingested")

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
