pipeline Recommender system avec frontend Streamlit via fast API. V.0 - 16_12_2024

# utilisation 

lancez le script run_project.sh depuis le bash:

./run_project.sh

- création d'environnement virtuel (reco_env)
- mise à jour de pip
- Installation des dépendances (requirement.txt) 
- Lancement de l'API FastAPI
- Lancement de l'application Streamlit

# Description

##1. Système de recommandation
Fichier : recommender_service/recommender.py

    * Recherche initiale des films.
    * Génération des recommandations à partir d'un film sélectionné.

##2. API FastAPI
Fichier : api/main.py
    L'API expose deux endpoints :

    * Recherche de films (/search) : L'utilisateur envoie un titre, et l'API retourne une liste de films possibles.
    * Recommandation (/recommend) : L'utilisateur envoie l'index du film choisi, et l'API retourne les recommandations.

##3. Frontend Streamlit
Fichier : frontend/app.py
    L'interface Streamlit gère :

    * L'entrée utilisateur pour la recherche d'un film.
    * L'affichage des résultats de recherche.
    * La saisie de l'index pour sélectionner un film et afficher les recommandations.


# Résumé du flux :

Recherche de films :

    L'utilisateur entre un titre dans Streamlit.
    Le titre est envoyé à l'API /search/.
    L'API retourne une liste de films similaires.

Sélection d'un film :

    L'utilisateur choisit un film parmi les résultats.
    L'index du film est envoyé à l'API /recommend/.

Recommandations :

    L'API retourne une liste de films recommandés basée sur le film sélectionné.
    Streamlit affiche les recommandations.