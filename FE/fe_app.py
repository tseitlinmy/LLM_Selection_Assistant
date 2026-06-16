import streamlit as st
import welcome

if 'pages' not in st.session_state:
    st.session_state.pages = {}


def page_2():
    st.title("Page 2")
    "Machine learning"
    if st.button("Go to Welcome"):
        st.switch_page(st.session_state.pages['welcome'])  # pass the StreamlitPage object

st.session_state.pages['welcome'] = welcome.welcome_page
st.session_state.pages['page2'] = page_2

st.session_state.pages['welcome'] = st.Page(welcome.welcome_page, title="Welcome")
st.session_state.pages['page2'] = st.Page(page_2, title="Page 2")

pg = st.navigation([st.session_state.pages['welcome'],
                    st.session_state.pages['page2']], position="hidden")
pg.run()

