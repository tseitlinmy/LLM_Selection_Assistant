import streamlit as st

def page():
    st.title("Providers")
    if st.button("Next"):
        st.switch_page(st.session_state.pages['upload'])  # pass the StreamlitPage object
