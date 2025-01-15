import streamlit as st
import requests

API_URL_SEARCH = "http://127.0.0.1:8000/search/"
API_URL_RECOMMEND = "http://127.0.0.1:8000/recommend/"

st.title("Système de recommandation de films")

# Étape 1 : Recherche de films
st.header("Recherche de films")
title = st.text_input("Entrez le titre d'un film :", "")

if st.button("Rechercher"):
    if title:
        response = requests.post(API_URL_SEARCH, json={"title": title})
        if response.status_code == 200:
            results = response.json()["results"]
            st.write("Films trouvés :")
            for film in results:
                st.write(f"Index : {film['index']} - {film['primaryTitle']} ({film['startYear']})")
        else:
            st.error("Aucun film trouvé.")
    else:
        st.warning("Veuillez entrer un titre de film.")

# Étape 2 : Sélection et recommandations
st.header("Recommandations")
index = st.number_input("Entrez l'index du film choisi :", min_value=0, step=1)

if st.button("Recommander"):
    response = requests.post(API_URL_RECOMMEND, json={"index": index})
    if response.status_code == 200:
        recommendations = response.json()["recommendations"]
        st.write("Recommandations basées sur votre sélection :")
        for reco in recommendations:
            st.write(f"{reco['primaryTitle']} ({reco['startYear']}) - Note : {reco['averageRating']} - Genres : {reco['genres']}")
    else:
        st.error("Erreur lors de la récupération des recommandations.")
