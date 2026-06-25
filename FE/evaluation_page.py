import streamlit as st
import FE.fe as fe

def page():
    st.set_page_config(page_title="Evaluation", layout="wide")
    st.title("Evaluation")
    if fe.button("New Evaluation"):
        st.switch_page(st.session_state.pages['providers'])  # pass the StreamlitPage object
