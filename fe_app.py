import streamlit as st
from FE.fe import setPath as setPath
setPath()

import welcome_page
import providers_page
import upload_page
import evaluation_page

if 'pages' not in st.session_state:
    st.session_state.pages = {}

st.session_state.pages['welcome'] = st.Page(welcome_page.page, title="Welcome", url_path="Welcome")
st.session_state.pages['providers'] = st.Page(providers_page.page, title="Providers", url_path="Providers")
st.session_state.pages['upload'] = st.Page(upload_page.page, title="Upload", url_path="Upload")
st.session_state.pages['evaluation'] = st.Page(evaluation_page.page, title="Evaluation", url_path="Evaluation") 

pg = st.navigation([st.session_state.pages['welcome'],
                    st.session_state.pages['providers'],
                    st.session_state.pages['upload'],
                    st.session_state.pages['evaluation']
                    ], position="hidden")
pg.run()