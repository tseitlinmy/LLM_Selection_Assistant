import streamlit as st
import FE.fe as fe
from COMMON.defs import *

if "providers" not in st.session_state:
    st.session_state.providers = {}

padding = "4px 12px"  # padding for table cells
colWidths = [0.11, 0.89]  # relative column widths for the table

# ---- Table Rows (using Streamlit columns so we can embed real edit boxes) ----
def render_row(key): # key is the provider name
    col1, col2 = st.columns(colWidths)
    with col1:
        st.markdown(
            """
            <div style="border:1px solid #D0D7E5; background-color:white;
                        color:black; padding:""" + padding + f"""; height:100%;">
                {key}
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.text_input(
            label=key,
            key=key,
            label_visibility="collapsed",
            placeholder="Enter API KEY",
        )

def render_non_implemented(key): # key is the provider name
    col1, col2 = st.columns(colWidths)
    with col1:
        st.markdown(
            """
            <div style="border:1px solid #D0D7E5; background-color:#D0D7E5;
                        color:black; padding:""" + padding + f"""; height:100%;">
                {key}
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
            <div style="border:1px solid #D0D7E5; background-color:#D0D7E5;
                        color:black; padding:""" + padding + f"""; height:100%;">
                {"Not implemented yet"}
            </div>
            """,
            unsafe_allow_html=True,
        )

import COMMON.providers as providers
def validate_api_keys():
    for provider in providers.get():
        if provider.isSupported:
            api_key = st.session_state.get(provider.name, "")
            if not api_key:
                fe.statusText(f"API key for {provider.name} is missing.", fe.infoLevel.WARNING)
                return False
            elif not provider.validate_api_key(api_key):
                fe.statusText(f"The API key for {provider.name} validation failed: {provider.status.val}", 
                              fe.infoLevel.ERROR)
                return False
            provider.apiKey = api_key  # Store the API key in the provider object
    return True

class __LC:
    pass

@binds_to(__LC)
def side_area(self):
    if fe.button("Next", True):
        if validate_api_keys():
            st.switch_page(st.session_state.pages['upload'])  # pass the StreamlitPage object

@binds_to(__LC)
def main_area(self):
    st.title("LLM Providers")

    # ---- CSS for table styling ----
    st.markdown(
        """
        <style>
        .provider-table {
            border-collapse: collapse;
            width: 100%;
        }
        .provider-table th, .provider-table td {
            border: 1px solid #D0D7E5;
            padding: """ + padding + """;
            text-align: left;
            vertical-align: middle;
        }
        /* Header styling */
        .provider-table th {
            background-color: #FFEB9C;
            color: #9C6500;
            font-weight: bold;
        }
        /* Row styling */
        .provider-table td {
            background-color: white;
            color: black;
        }
        /* Make the streamlit text_input fill the column */
        div[data-testid="stTextInput"] input {
            width: 100%; font-size: 18px;
        }
        .tight-rows div[data-testid="stVerticalBlock"] { gap: 2px; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ---- Table Header ----
    st.markdown(
        f"""
        <table class="provider-table">
            <thead>
                <tr>
                    <th style="width:{int(colWidths[0]*100)}%;">Provider Name</th>
                    <th style="width:{int(colWidths[1]*100)}%;">API KEY</th>
                </tr>
            </thead>
        </table>
        """,
        unsafe_allow_html=True,
    )

    # ---- Table Rows ----
    for provider in providers.get():
        if provider.isSupported:
            render_row(provider.name)
        else:
            render_non_implemented(provider.name)
    st.markdown("<br>", unsafe_allow_html=True)

def page():
    fe.page_init("LLM Providers")
    intr = __LC()

    cMain, cSide = st.columns([0.85, 0.15], vertical_alignment="center", border=True)
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