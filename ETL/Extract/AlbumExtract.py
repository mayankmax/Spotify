#Get the Raw data from album and store it  in
# dictionary

from ...RawData.AlbumData import *
from ...Config.config import *

class AlbumExtract:
    def __init__(self,albumId,accessToken):
        self.albumId = albumId
        self.accessToken = accessToken
        
        
    def ExtractAlbumData(self):
        for album_id in self.albumId:
            response = get_album_info(album_id, self.accessToken)
            print(response['popularity'])
            
            
album_ids = ["382ObEPsp2rxGrnsizN5TX", "1A2GTWGtFfWp7KSQTwWOyo", "2noRn2Aes5aoNVsU6iWThc"]  
client_id = "31c2e953a1cc49eaa153d1fd504728a3"
client_secret = "eb2ee00f392f49bf850c16deb6e824ce"
access_token = get_spotify_token(client_id, client_secret)
       
albumObj = AlbumExtract(album_ids,access_token)

albumObj.ExtractAlbumData()
            
