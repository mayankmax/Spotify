# artist.py

import requests
from Config.config import *

def get_artist_info(artist_id, access_token):
    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(artist_url, headers=headers)
    artist_data = response.json()
    return artist_data