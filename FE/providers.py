import streamlit as st
import fe

def page():
    st.set_page_config(page_title="Providers", layout="wide")
    st.title("Providers")
    if fe.button("Next", True):
        st.switch_page(st.session_state.pages['upload'])  # pass the StreamlitPage object

if __name__ == "__main__":
    import os
    directory = os.path.dirname(__file__)
    fe.setPath(os.path.join(directory, ".."))
    page()