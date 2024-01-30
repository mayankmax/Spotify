#Get the Raw data from artist and store it in a dictionary

import sys
import os
from dotenv import load_dotenv

load_dotenv()

# Add the root project directory to sys.path
project_root = '/home/mayank/Desktop/Project/DE/Spotify/'
sys.path.append(project_root)

# Now you can import the module
from RawData.Artist import get_artist_info
from Config.config import get_spotify_token

class ArtistExtract:
    result = {}  # This is a dictionary
    def __init__(self, artistId, accessToken):
        self.artistId = artistId
        self.accessToken = accessToken

    def ExtractArtistData(self):
        for artist_id in self.artistId:
            response = get_artist_info(artist_id, self.accessToken)
            # Add artist's information to the result dictionary
            self.result[artist_id] = {
                'artist_name': response['name'],
                'artist_popularity': response['popularity'],
                'artist_id': response['id'],
                'artist_genre': response['genres'],  # this is a list type
                'artist_followers': response['followers']['total']
            }

    def get_result(self):
        return self.result

# Sample artist_ids
# artist_ids = ["2CIMQHirSU0MQqyYHq0eOx", "57dN52uHvrHOxijzpIgu3E", "1vCWHaC5f2uS3yhpwWbIA6"]
# client_id = os.getenv('spotify_client_id')
# client_secret = os.getenv('spotify_client_secret')

# print(client_id)
# print(client_secret)
# access_token = get_spotify_token(client_id, client_secret)

# artistObj = ArtistExtract(artist_ids, access_token)

# # Extract artist data
# artistObj.ExtractArtistData()

# # Get the result dictionary
# result_dict = artistObj.get_result()

# # Print the result for each artist
# for artist_id, artist_info in result_dict.items():
#     print(f"Artist ID: {artist_id}")
#     print(f"Name: {artist_info['artist_name']}")
#     print(f"Popularity: {artist_info['artist_popularity']}")
#     print(f"Genre: {artist_info['artist_genre']}")
#     print(f"Followers: {artist_info['artist_followers']}")
#     print("\n")
