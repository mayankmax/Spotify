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
 
def get_album_info(album_id, access_token):
    """
    Get information about a Spotify album using the album ID.
    """
    album_url = f"https://api.spotify.com/v1/albums/{album_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
 
    response = requests.get(album_url, headers=headers)
    album_data = response.json()
    return album_data
 
def main():
    
    # Replace these with your actual values
    client_id = ""
    client_secret = ""
    access_token = get_spotify_token(client_id, client_secret)
 
    # Replace these with your actual album IDs
    album_ids = ["382ObEPsp2rxGrnsizN5TX", "1A2GTWGtFfWp7KSQTwWOyo", "2noRn2Aes5aoNVsU6iWThc"]
 
    for album_id in album_ids:
        album_info = get_album_info(album_id, access_token)
        print(f"\nAlbum ID: {album_id}")
        print("Album Information:")
        print(album_info)
 
if __name__ == "__main__":
    main()
