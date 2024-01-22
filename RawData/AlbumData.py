# album.py

import requests
from config import get_spotify_token

def get_album_info(album_id, access_token):
    album_url = f"https://api.spotify.com/v1/albums/{album_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(album_url, headers=headers)
    album_data = response.json()
    return album_data
