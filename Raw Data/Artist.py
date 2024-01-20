import requests

def get_spotify_token(client_id, client_secret):
    """
    Get Spotify access token using client credentials flow.
    """
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
    access_token = token_data.get("access_token")
    return access_token

def get_artist_info(artist_id, access_token):
    """
    Get information about a Spotify album using the artist ID.
    """
    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(artist_url, headers=headers)
    artist_data = response.json()
    return artist_data

def main():
    # Replace these with your actual values
    client_id = "31c2e953a1cc49eaa153d1fd504728a3"
    client_secret = "eb2ee00f392f49bf850c16deb6e824ce"
    access_token = get_spotify_token(client_id, client_secret)

    # Replace these with your actual album IDs
    artist_ids = ["2CIMQHirSU0MQqyYHq0eOx", "57dN52uHvrHOxijzpIgu3E", "1vCWHaC5f2uS3yhpwWbIA6"]

    for artist_id in artist_ids:
        artist_info = get_artist_info(artist_id, access_token)
        print(f"\n Artist ID: {artist_id}")
        print("Artist Information:")
        print(artist_info)

if __name__ == "__main__":
    main()