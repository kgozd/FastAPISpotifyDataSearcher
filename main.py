from fastapi import FastAPI
from routers import spotify

app = FastAPI( 
    title="SpotifyDataSearcher",
    description = 'Just a FastAPI wrapper for SpotifyAPI Search for "fun" purpose. It uses Github Actions to contanarize and publish app on Azure ;) ',
    version="0.0.1",
    contact={
        "name": "kgozd",
        "url": "https://github.com/kgozd",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
    )

app.include_router(spotify.app)
 