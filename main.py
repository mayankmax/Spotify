# main.py

from RawData.Artist import *
from RawData.AlbumData import *
from Config.config import *

def main():
    # Replace these with your actual values


    client_id = "31c2e953a1cc49eaa153d1fd504728a3"
    client_secret = "eb2ee00f392f49bf850c16deb6e824ce"
    access_token = get_spotify_token(client_id, client_secret)

    # Replace these with your actual artist and album IDs
    artist_ids = ["2CIMQHirSU0MQqyYHq0eOx","57dN52uHvrHOxijzpIgu3E","1vCWHaC5f2uS3yhpwWbIA6"]
    album_ids = ["382ObEPsp2rxGrnsizN5TX", "1A2GTWGtFfWp7KSQTwWOyo", "2noRn2Aes5aoNVsU6iWThc"]

    # Fetch and print artist information
    # print("Artist Information:")
    # for artist_id in artist_ids:
    #     artist_info = get_artist_info(artist_id, access_token)
    #     print(f"\nArtist ID: {artist_id}")
    #     print(artist_info)

   # Fetch and print album information
    print("\nAlbum Information:")
    # for album_id in album_ids:
    album_info = get_album_info("382ObEPsp2rxGrnsizN5TX", access_token)
    print("\nAlbum ID: {382ObEPsp2rxGrnsizN5TX}")
    print(album_info)

if __name__ == "__main__":
    main()
