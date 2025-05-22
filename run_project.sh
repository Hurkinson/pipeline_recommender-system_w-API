#!/bin/bash

set -e

function info {
    echo -e "\033[1;34m[INFO]\033[0m $1"
}

function error {
    echo -e "\033[1;31m[ERREUR]\033[0m $1"
}

ENV_DIR="reco_env"

# Création de l'environnement virtuel s'il n'existe pas
if [ ! -d "$ENV_DIR" ]; then
    info "Création de l'environnement virtuel '$ENV_DIR'..."
    python -m venv $ENV_DIR
else
    info "L'environnement virtuel '$ENV_DIR' existe déjà."
fi

source $ENV_DIR/Scripts/activate

info "Mise à jour de pip..."
python.exe -m pip install --upgrade pip

info "Installation des dépendances..."
pip install -r requirements.txt

info "Lancement de l'API FastAPI..."
uvicorn api.main:app --host 0.0.0.0 --port 8000 &
API_PID=$!

info "Lancement de l'application Streamlit..."
streamlit run frontend/app.py &

info "Tous les services sont lancés."
wait $API_PID
