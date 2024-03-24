# from dotenv import load_dotenv
from os import getenv
# from os import environ
from base64 import b64encode
# import base64
from requests import post
from fastapi import HTTPException

# load_dotenv()
client_id = getenv("CLIENT_ID")
client_secret = getenv("CLIENT_SECRET")

# client_id = environ["client_id"]
# client_secret = environ["client_secret"]

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)

    if result.status_code != 200:
        raise HTTPException(status_code=result.status_code, detail="Failed to get token")

    json_result = result.json()
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}
