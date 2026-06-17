import streamlit as st
import fe

def page():
    # Configure page
    st.set_page_config(page_title="Welcome", layout="wide")

    # Custom CSS for styling
    st.markdown("""
    <style>
        .main-table {
            width: 100%;
            border-collapse: collapse;
            margin: 0;
        }
        .content-row {
            padding: 20px;
            text-align: left;
            border: 0px solid #ddd;
        }
        .button-row {
            padding: 20px;
            text-align: center;
            border: 0px solid #ddd;
        }
        .stButton button {
            margin: 0 auto;
        }
    </style>
    """, unsafe_allow_html=True)

    # First row - Brown background with white text
    st.markdown("""
    <table style="width: 100%;">
        <tr>
            <td 
                style="vertical-align: middle; text-align: center; background-color: #08524D; color: #CCFFA4;"
            >
                <h1>Welcome to the LLM Selection Assistant</h1>
            </td>
        </tr>
    </table>

    <div class="content-row">
        <p><h3>Motivation:</h3>
        This is a tool for cost optimization</p>
        <p><h3>Use-case:</h3>
    Let somebody writes program.<br>
    This program, particularly, sends prompts to private, closed LLM models - so need to pay per token.  
    He selected some prompts and decided to try other LLMs usage for them to decrease cost.
        </p>
    <p></p>
    <p>
    For each of selected prompts he may use "LLM Selection Assistant" which:<br> 
    • will launch this prompt on relevant models from different LLM providers.<br>
    • report launching results.<br>
    It will help to select the optimal LLM model for specified prompts launching.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # Third row - Button centered
    st.markdown('<div class="button-row">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if fe.button("Start", True):
            st.switch_page(st.session_state.pages['providers'])  # pass the StreamlitPage object
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    page()