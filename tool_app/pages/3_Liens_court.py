import pyshorteners
import streamlit as st
st.set_page_config(layout="wide", page_title="Liens courts")
st.markdown(
    "<h1 style='text-align: center'>Générateur de liens courts</h1>",
    unsafe_allow_html=True)


@st.cache
def generate_short_link(long_url):
    type_tiny = pyshorteners.Shortener()
    short_link = type_tiny.tinyurl.short(long_url)
    return short_link


long_url = st.text_input("Entrez l'URL longue :")

if long_url:
    st.metric("Lien court généré : ", generate_short_link(long_url))
