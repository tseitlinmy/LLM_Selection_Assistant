import streamlit as st

def page():
    st.title("Evaluation")
    if st.button("New Evaluation"):
        st.switch_page(st.session_state.pages['providers'])  # pass the StreamlitPage object
