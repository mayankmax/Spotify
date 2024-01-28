#Get the Raw data from album and store it in a dictionary

import sys
import os

# Add the root project directory to sys.path
project_root = '/home/mayank/Desktop/Project/DE/Spotify/'
sys.path.append(project_root)

# Now you can import the module
from RawData.AlbumData import get_album_info
from Config.config import get_spotify_token

class AlbumExtract:
    def __init__(self, album_ids, access_token):
        self.album_ids = album_ids
        self.access_token = access_token
        self.album_data = {}  # Dictionary to store album information

    def ExtractAlbumData(self):
        for album_id in self.album_ids:
            response = get_album_info(album_id, self.access_token)

            # Store album information in the dictionary
            self.album_data[album_id] = {
                'album_name': response['name'],
                'popularity': response['popularity'],
                'genres': response['genres'],
                'tracks': response['total_tracks'],
                'release_date': response['release_date'],
                'labels': response['label']
            }

    def get_album_data(self):
        return self.album_data

# Sample album_ids
album_ids = ["382ObEPsp2rxGrnsizN5TX", "1A2GTWGtFfWp7KSQTwWOyo", "2noRn2Aes5aoNVsU6iWThc"]
# client_id = 
# client_secret = "eb2ee00f392f49bf850c16deb6e824ce"

# export SPOTIFY_CLIENT_ID= "31c2e953a1cc49eaa153d1fd504728a3"
# export SPOTIFY_CLIENT_SECRET= "eb2ee00f392f49bf850c16deb6e824ce"
client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")


client_id = client_id[1:]
client_secret = client_secret[1:]
access_token = get_spotify_token(client_id, client_secret)

albumObj = AlbumExtract(album_ids, access_token)

# Extract album data
albumObj.ExtractAlbumData()

# Get the album data dictionary
album_data_dict = albumObj.get_album_data()

# Print the result for each album
for album_id, album_info in album_data_dict.items():
    print(f"Album ID: {album_id}")
    print(f"Name: {album_info['album_name']}")
    print(f"Popularity: {album_info['popularity']}")
    print(f"Genres: {album_info['genres']}")
    print(f"Tracks: {album_info['tracks']}")
    print(f"Release Date: {album_info['release_date']}")
    print(f"Labels: {album_info['labels']}")
    print("\n")
