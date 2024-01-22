# config.py

import requests

def get_spotify_token(client_id, client_secret):
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    response = requests.post(token_url, headers=headers, data=data)
    token_data = response.json()
    print(response)
    access_token = token_data.get("access_token")
    return access_token
