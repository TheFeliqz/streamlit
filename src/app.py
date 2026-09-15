import streamlit as st

st.title ("Document Summary")


pages = [
    st.Page("pages/1_summarize.py", title="Summarize"),
    st.Page("pages/2_knowledgebase.py", title="Knowledge Base")
]

navigation = st.navigation(pages)
navigation.run()
