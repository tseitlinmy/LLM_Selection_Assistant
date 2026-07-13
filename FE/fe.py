import streamlit as st
import os
import sys
from enum import Enum

infoLevel = Enum("infoLevel", "ERROR WARNING INFO DEBUG")
levelIcon = {
    infoLevel.ERROR: "❌",
    infoLevel.WARNING: "⚠️",
    infoLevel.INFO: "ℹ️",
    infoLevel.DEBUG: "🐞",
}

def setPath(base_path=None):
    if base_path is None:
        base_path = os.path.dirname(sys.argv[0])
    sys.path.append(base_path)

def button(label: str, isBold: bool = False, use_container_width: bool = False, id: int = 0) -> bool:
    weight = "700" if isBold else "400"

    # Custom CSS for the button
    st.markdown("""
    <style>
    /* Target the button container */
    div.st-key-btn""" + str(id) + """ button {
        background-color: #7E3D01 !important;
        color: #DDD9C3 !important;
        
        /* Text centering */
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        
        /* Margins - min and max horizontal */
        margin-top: 0px !important;
        margin-bottom: 0px !important;
        margin-left: clamp(10px, 5vw, 12px) !important;
        margin-right: clamp(10px, 5vw, 12px) !important;
        
        /* Additional styling */
        /* Border */
        border: 2px solid #DDD9C3 !important;
        border-radius: 8px !important;
        padding: 0 24px !important;
        width: calc(100% - clamp(20px, 10vw, 24px)) !important;
        line-height: 1.2 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        white-space: nowrap !important;
    }

    div.st-key-btn""" + str(id) + """ button p {
        /* Typography */
        font-family: "Arial", sans-serif;
        font-size: 26px !important;
        font-weight: """ + weight + """ !important;
    }

    /* Hover effect */
    div.st-key-btn""" + str(id) + """ button:hover {
        background-color: #9A4D02 !important;
        transform: scale(1.02) !important;
        box-shadow: 0 4px 15px rgba(126, 61, 1, 0.4) !important;
    }

    /* Active/click effect */
    div.st-key-btn""" + str(id) + """ button:active {
        transform: scale(0.98) !important;
    }

    /* Focus state for accessibility */
    div.st-key-btn""" + str(id) + """ button:focus {
        outline: 2px solid #DDD9C3 !important;
        outline-offset: 2px !important;
    }

    /* Ensure container doesn't add extra margins */
    div.st-key-btn""" + str(id) + """ {
        margin: 0 !important;
        padding: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Create the button
    return st.button(label, use_container_width = use_container_width, key="btn" + str(id))

def statusText(text, level=infoLevel.INFO):
    st.session_state.sb_text = f"{levelIcon[level]} {text}"
def statusClear():
    st.session_state.sb_text = "&nbsp;"

# Should be last call. Because Streamlit draws the page from top to bottom, 
# and we want the status bar to be at the bottom of the page.
def statusDisplay():
    if "sb_text" not in st.session_state:
        statusClear()
    with st.bottom:
        st.markdown(
            f"""
            <div style="
                width: 100%;
                background-color: #66cdaa;
                text-align: left;
                margin: 0 4px;
                border-top: 3px solid #000;
                padding-left: 4px;
                box-sizing: border-box;
            ">{st.session_state.sb_text}</div>
            """,
            unsafe_allow_html=True,
        )

def page_init(page_title):
    st.set_page_config(page_title=page_title, layout="wide")
    statusClear()  # Clear the status bar at the bottom of the page

if __name__ == "__main__":
    st.set_page_config(page_title="Test tools", layout="wide")
    if button("Click Me"):
        statusText("Button clicked!", infoLevel.INFO)
    statusDisplay()
