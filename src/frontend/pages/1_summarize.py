import os
from dotenv import load_dotenv
import streamlit as st
import httpx

# load .env variables
load_dotenv()

st.markdown("## Summarize a Document")

# File Uploader
uploaded_file = st.file_uploader("Upload File for Summarization here")

if uploaded_file is not None:
    # Text preview (to check what the user uploaded)
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

            payload = {"file_text": file_text}
            response = httpx.post(
                f"{os.getenv("BACKEND_URL")}/summarize",
                json = payload,
                timeout=30.0
            )

            data = response.json()
            summary = data["summary"] 

        st.success("Summary generated")
        st.write(summary)
