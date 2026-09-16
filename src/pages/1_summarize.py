import streamlit as st

from services.summarize import summarize


# File uploader
uploaded_file = st.file_uploader("Upload File for Summarization here")

if uploaded_file is not None:
    file_text = uploaded_file.getvalue().decode("utf-8")
    st.write(file_text)


# "Summarize" Button
if st.button("Summarize"):
    summarize(file_text)
    

# "Wating for Summary..." Display

# Display the answer when its ready
