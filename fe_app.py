import streamlit as st
from FE.fe import setPath as setPath
setPath()

import welcome
import providers
import upload
import evaluation

if 'pages' not in st.session_state:
    st.session_state.pages = {}

st.session_state.pages['welcome'] = st.Page(welcome.page, title="Welcome", url_path="Welcome")
st.session_state.pages['providers'] = st.Page(providers.page, title="Providers", url_path="Providers")
st.session_state.pages['upload'] = st.Page(upload.page, title="Upload", url_path="Upload")
st.session_state.pages['evaluation'] = st.Page(evaluation.page, title="Evaluation", url_path="Evaluation") 

pg = st.navigation([st.session_state.pages['welcome'],
                    st.session_state.pages['providers'],
                    st.session_state.pages['upload'],
                    st.session_state.pages['evaluation']
                    ], position="hidden")
pg.run()