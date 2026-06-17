import streamlit as st
import fe

def page():
    st.title("Evaluation")
    if fe.button("Next", True):
        st.switch_page(st.session_state.pages['evaluation'])  # pass the StreamlitPage object
