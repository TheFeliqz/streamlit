import streamlit as st

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



st.markdown("## Clear files from the Knowledge Base")

# Overview of files stored in vector store
#TODO add storing source document of a chunk into the vector store and then write all unique document names 

if "cleared" not in st.session_state:
    st.session_state.cleared = False

# Confirmation window to clear Knowledge Base
@st.dialog("Confirm clearing")
def confirm_delete():
    st.write("Are you sure you want to clear the Knowledge Base?")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Yes, clear"):
            clear_vector_store()
            st.session_state.cleared = True
            st.rerun()

    with col2:
        if st.button("Cancel"):
            st.rerun()

# Button to clear Knowledge Base
if st.button("Clear Knowledge Base"):
    confirm_delete()

# Confirmation for the user that Knowledge Base has been cleared
if st.session_state.cleared:
    st.success("Knowledge Base cleared")
    st.session_state.cleared = False



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
