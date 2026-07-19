import streamlit as st
from COMMON.defs import *
import FE.fe as fe
from FE.providers_page import validate_api_keys

class __LC:
    def __init__(self):
        self.uploaded_file = None

    def validate(self):
        if self.uploaded_file is None:
            fe.statusText("No file uploaded.", fe.infoLevel.ERROR)
            return False
        return True

@binds_to(__LC)
def side_area(self):
    btnEvaluate = fe.button("Evaluate", True, use_container_width=True)
    if btnEvaluate:
                if self.validate():
                    st.switch_page(st.session_state.pages['evaluation'])  # pass the StreamlitPage object

def showCopyableText(text: str, id: int):
        ifCopy = st.button("", icon=":material/content_copy:", 
                           type="primary", help="Copy to clipboard", key="copy_btn" + str(id))
        st.html(text)

        text = text.replace('<br>', "")
        text = text.replace('&nbsp;', " ")
        if ifCopy:
            st.html(
                f'''
                <script>
                async function copyText() {{
                    const txt = `{text}`;
                    try {{
                        await navigator.clipboard.writeText(txt);
                    }} catch (err) {{
                        const el = document.createElement('textarea');
                        el.value = txt;
                        document.body.appendChild(el);
                        el.select();
                        document.execCommand('copy');
                        document.body.removeChild(el);
                    }}
                }}
                copyText();
                </script>
                ''',
                unsafe_allow_javascript=True,
            )

@binds_to(__LC)
def main_area(self):
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
            table, th, td {
                border: none !important; /* Forces the removal of existing borders */
                border-collapse: collapse; /* Merges cell lines tightly together */
            }
            table tr.separator { height: 1em; }
            .tbl-header {
                background-color : #FFEB9C;
                color            : #9C6500;
                font-weight      : bold;
                font-size        : 24px;
                text-align       : center;
                padding          : 4px;
            }
            .tbl-line {
                background-color: #EBEBEB;
                text-align: left;
                padding          : 6px;
                border-radius: 8px !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
    )

    st.markdown(
            '''
            <span style="font-size: 30px;font-weight: bold;">"Evaluation Set" Upload Page</span><BR>
            <span style="font-size: 24px;font-weight: bold;">Useful Information:</span>
            <table style="width:100%; border-collapse: collapse; border: 2px solid #D0D7E5;">
            <TR><TD class="tbl-line" style="margin-top: 0; margin-bottom: 0;">
                &nbsp;&nbsp;&nbsp;&gt; &nbsp; <a href="app/static/EDS_gathering.html"  target="_blank">Short explanation & detailed help</a>
            </TD></TR></table>''',
            unsafe_allow_html=True,
    )
    with st.expander('"LLM Built-In Tools checking" prompt prefix'):
        showCopyableText(''' 
We use "BIT" as abbreviature for "built-in or internal tool".<br>
<br>
What BITs will be called to perform the below PROMPT?<br>
* If BIT WILL BE CALLED:<br>
&nbsp;&nbsp;- Print line: ### BUILT-IN TOOLS INFO:<br>
&nbsp;&nbsp;- Give the list of called BITs. Where information about BIT is displayed in format:<br>
&nbsp;&nbsp;# BUILT-IN TOOL DESCRIPTION START<br>
&nbsp;&nbsp;TOOL NAME: specific BIT name<br>
&nbsp;&nbsp;TOOL DESCRIPTION: specific BIT description string<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Give CONSIZE description of the tool.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Do not need to give examples of use)<br>
&nbsp;&nbsp;# BUILT-IN TOOL DESCRIPTION END<br>
&nbsp;&nbsp;Empty line<br>
<br>
* If BIT WILL NOT BE CALLED - the answer should be: "### NO BUILT-IN TOOLS WERE CALLED".<br>
<br>
PROMPT:<br>
                         ''', id=1)
    with st.expander('"Tools dumping" prompt prefix'):
        showCopyableText('''
Answer the PROMPT adhering to the following rules:<br>
GOAL: To gather information required for PROMPT debugging.<br>
<br>
Instructions for Tool Usage:<br>
Whenever you call a function or tool, you must follow this structured output format:<br>
* Function Execution: Perform the necessary tool calls.<br>
* Fact Repository: Create a section titled ### TOOL_FACTS.<br>
&nbsp; List every piece of raw data returned by the tools as discrete, numbered facts.<br>
&nbsp; For each entry, you must include:<br>
&nbsp; - Tool Name: The name of the function called.<br>
&nbsp; - Tool Description string <br>
&nbsp; - Parameters: The exact arguments/parameters passed to the tool INCLUDING DEFAULT PARAMETERS VALUES.<br>
&nbsp; - Raw Output: The return from the tool in JSON format.<br>
<br>
Final Answer: Provide the concise response to the user.<br>
Strict Rule:<br>
* Do not internalize tool outputs into your prose until they have been "dumped" into the TOOL_FACTS section first.<br>
<br>
PROMPT:
    ''', id=2)

    # Define your custom CSS to target the file uploader dropzone
    custom_css = """
        <style>
            [data-testid="stFileUploaderDropzone"] {
                background-color: #EBEBEB;
                color: rgb(34 34 60); /* Text color */
                border: 1px solid rgb(195 195 195); /* solid border */
                border-radius: 8px !important;
                padding: 20px; /* Padding inside the dropzone */
            }
        /* Targets the label element inside the file uploader widget */
        [data-testid="stFileUploader"] label p {
            font-size: 24px !important;
            font-weight: bold;
        }            </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True) # Inject the CSS into the app
    self.uploaded_file = st.file_uploader('Upload "Evaluation Set" File:', label_visibility="visible")

def page():
    fe.page_init("Upload")
    intr = __LC()

    cMain, cSide = st.columns([0.80, 0.20], vertical_alignment="center", border=True)
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