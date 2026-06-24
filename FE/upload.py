import streamlit as st
import fe

def page():
    st.set_page_config(page_title="Upload", layout="wide")
    st.title("Upload")
    if fe.button("Next", True):
        st.switch_page(st.session_state.pages['evaluation'])  # pass the StreamlitPage object
