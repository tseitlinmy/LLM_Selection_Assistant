import streamlit as st
import fe

def page():
    st.title("Providers")
    if fe.button("Next", True):
        st.switch_page(st.session_state.pages['upload'])  # pass the StreamlitPage object
