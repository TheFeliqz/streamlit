import streamlit as st

pages = [
    st.Page("pages/1_summarize.py", title="Summarize Document"),
    st.Page("pages/2_knowledgebase.py", title="Knowledge Base"),
]

navigation = st.navigation(pages)
navigation.run()
