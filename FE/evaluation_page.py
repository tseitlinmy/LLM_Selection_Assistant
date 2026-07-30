import streamlit as st
from COMMON.defs import *
import FE.fe as fe

class __LC:
    pass

@binds_to(__LC)
def main_area(self):
    st.title("Evaluation")
    st.markdown(
            """
            <style>
            div[data-testid="stExpander"] {
                background-color: #EBEBEB;  /* light green */
                border-radius: 8px;
            }
            div[data-testid="stExpander"] div[role="button"] p {
                font-size: 18px;
            }
            </style>
            """,
            unsafe_allow_html=True,
    )
    with st.expander('Evaluation Instructions'):
        st.html('''
<ol>
<li>Uploaded prompts are launched against models of selected providers. Time & Cost statistics are gathered and are presented to user in <b><u>Evaluation List section</u></b>. On this stage, <b><u>answer correctness is not evaluated</u></b> to save time. Correctness evaluation is performed on selected model <b><u>by request only</u></b>.</li>
<li>Answer correctness is defined as correspondence to answer which was got on user side. <b><u>[SHOW ACCURACY]</u></b> button displays the selected model accuracy on status bar.</li>
<li><b><u>[DOWNLOAD]</u></b> button zips and downloads all stuff about the selected models which was gathered till now.</li>
<li>Let the user is satisfied with the selected model statistics. The user may want to be convinced that this model makes reasoning correctly when it answers the question. Then he may press <b><u>[INCLUDE CoT]</u></b> button (CoT is "Chain of Thinking" - reasoning). if the selected model supports CoT, then it will answer each question from "Evaluation Dataset" with CoT & tools call dumping. These answers will be saved for further downloading.</li>
<li>Pressing <b><u>[NEW EVALUATION]</u></b> button will return to <b><u>"Providers"</u></b> page to start new evaluation.</li>
</ol>
        ''')
@binds_to(__LC)
def side_area(self):
    btnText = "SHOW ACCURACY"
    if fe.button(btnText, use_container_width=True, id = 0):
        fe.statusText(f"The [{btnText}] button was pressed.", fe.infoLevel.INFO)
    btnText = "INCLUDE CoT"
    if fe.button(btnText, use_container_width=True, id = 1):
        fe.statusText(f"The [{btnText}] button was pressed.", fe.infoLevel.INFO)

    btnStyle = fe.ButtonStyle(id=2)
    fname = "LICENSE"  # Replace with the actual path to your file
    with open(fname, "rb") as file:
        st.download_button(
            label="DOWNLOAD",
            data=file,
            file_name=fname,
            mime="application/octet-stream",
            key=btnStyle.key(),
            use_container_width=True
        )

    if fe.button("NEW EVALUATION", use_container_width=True, id = 3):
        st.switch_page(st.session_state.pages['providers'])  # pass the StreamlitPage object

def page():
    fe.page_init("Evaluation")
    intr = __LC()

    cMain, cSide = st.columns([0.74, 0.26], vertical_alignment="top", border=True)
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