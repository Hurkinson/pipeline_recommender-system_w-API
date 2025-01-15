from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommender_service.recommender import search_movies, recommend_movies

app = FastAPI()


class MovieSearchRequest(BaseModel):
    title: str

class MovieRecommendRequest(BaseModel):
    index: int


#--- Routes -----------------------------------

@app.post("/search/")
def search_movies_endpoint(request: MovieSearchRequest):
    """
    Recherche de films par titre.
    """
    title = request.title
    results = search_movies(title)

    if results.empty:
        raise HTTPException(status_code=404, detail="Aucun film trouvé.")
    
    # Retourner les films possibles
    return {
        "results": results[['index', 'primaryTitle', 'originalTitle', 'startYear']].to_dict(orient='records')
    }

@app.post("/recommend/")
def recommend_movies_endpoint(request: MovieRecommendRequest):
    """
    Recommande des films basés sur l'index d'un film choisi.
    """
    index = request.index
    try:
        recommendations = recommend_movies(index)
        return {
            "recommendations": recommendations[['primaryTitle', 'originalTitle', 'startYear', 'averageRating', 'genres']].to_dict(orient='records')
        }
    except IndexError:
        raise HTTPException(status_code=400, detail="Index de film invalide.")

