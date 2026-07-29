import streamlit as st
from COMMON.defs import *
import FE.fe as fe

class __LC:
    pass

@binds_to(__LC)
def main_area(self):
    st.title("Evaluation")

@binds_to(__LC)
def side_area(self):
    if fe.button("New Evaluation"):
        st.switch_page(st.session_state.pages['providers'])  # pass the StreamlitPage object

def page():
    fe.page_init("Evaluation")
    intr = __LC()

    cMain, cSide = st.columns([0.75, 0.25], vertical_alignment="top", border=True)
    with cMain:
        intr.main_area()
    with cSide:
        intr.side_area() 

    fe.statusDisplay()  # Display the status bar at the bottom of the page

if __name__ == "__main__":
    import os
    directory = os.path.dirname(__file__)
    fe.setPath(os.path.join(directory, ".."))
    page()