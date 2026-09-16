import streamlit as st

from services.summarize import summarize


# File uploader
uploaded_file = st.file_uploader("Upload File for Summarization here")

if uploaded_file is not None:
    file_text = uploaded_file.getvalue().decode("utf-8")

    # Text preview (to check what I uploaded)
    st.text_area(
        "Document Preview",
        file_text,
        height=300,
        disabled=True
    )


# Summary 
if st.button("Summarize"):
    with st.spinner("Generating summary..."):
        summary = summarize(file_text)

    st.success("Summary generated")
    st.write(summary)

