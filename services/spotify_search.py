from requests import get
from fastapi import HTTPException
from services.spotify_auth import get_auth_header


def search_for_artist(token, artist_name):
    headers = get_auth_header(token)
    url = "https://api.spotify.com/v1/search"
    query = f"?q={artist_name}&type=artist&limit=10&market=PL"

    query_url = url + query
    result = get(query_url, headers=headers)

    if result.status_code != 200:
        raise HTTPException(status_code=result.status_code, detail="Failed to search for artist")

    json_result = result.json()
    return json_result
