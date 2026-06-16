import streamlit as st

def page():
    st.title("Evaluation")
    if st.button("Next"):
        st.switch_page(st.session_state.pages['evaluation'])  # pass the StreamlitPage object
