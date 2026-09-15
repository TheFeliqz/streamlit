import streamlit as st

name = st.text_input("Testinput")

if st.button("Submit"):
    st.write(f"Hello, {name}")


# _________________________ #

# File uploader

# "Summarize" Button

# "Wating for Summary..." Display

# Display the answer when its ready
