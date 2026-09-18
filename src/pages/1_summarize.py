import streamlit as st

from services.summarize import summarize

# File Uploader
uploaded_file = st.file_uploader("Upload File for Summarization here")

if uploaded_file is not None:
    # Text preview (to check what I uploaded)
    st.text_area(
        "Document Preview",
        uploaded_file.getvalue().decode("utf-8"),
        height=300,
        disabled=True
    )

# Summary 
if st.button("Summarize"):

    if uploaded_file is None:
        st.warning("Please select a file.")

    else:
        file_text = uploaded_file.getvalue().decode("utf-8")
        with st.spinner("Generating summary..."):
            summary = summarize(file_text)

        st.success("Summary generated")
        st.write(summary)
