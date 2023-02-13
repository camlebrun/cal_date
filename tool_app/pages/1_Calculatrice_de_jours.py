import datetime
import streamlit as st

st.set_page_config(layout="wide", page_title="Calculatrice de jours")

st.markdown("<h1 style='text-align: center'>Calculatrice de jours</h1>", unsafe_allow_html=True)


def calculate_date(operation, days_to_add, d):
    if operation == "Ajouter":
        d2 = d + datetime.timedelta(days=days_to_add)

    elif operation == "Soustraire":
        d2 = d - datetime.timedelta(days=days_to_add)
        
    return d2

d = st.date_input("Choisir votre date", datetime.datetime.now())
d1 = str(d)
st.write('Vous avez choisi le : ', d1)
operation = st.selectbox("Sélectionnez l'opération", ["Ajouter", "Soustraire"])
days_to_add = st.number_input("Choisir le nombre de jour à ajouter/soustraire", min_value=0, step=1)
d2 = calculate_date(operation, days_to_add, d)
d3 = str(d2)
result = st.metric("Le résultat est : ", d3)