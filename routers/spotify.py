from fastapi import APIRouter, HTTPException, Depends
from services.spotify_auth import get_token
from services.spotify_search import search_for_artist



app = APIRouter()

@app.get("/")
async def read_users():
    return [{"Just a simple fastapi app...": "Not that simple!!!;)"}]

@app.get("/search/{artist_name}")
async def search_artist(artist_name: str, token: str = Depends(get_token)):
    result = search_for_artist(token, artist_name)
    return result 
