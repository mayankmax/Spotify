# # #lets load album into gcp
# #     # mysql db etc
# #     #Google BigQuery


# # # Dataset info
# # # Dataset ID
# # # cobalt-particle-329816.demoDataset_001
# # # Created
# # # Jan 30, 2024, 4:58:39 PM UTC+5:30
# # # Default table expiration
# # # 30 days
# # # Last modified
# # # Jan 30, 2024, 4:58:39 PM UTC+5:30
# # # Data location
# # # US
# # # Description
# # # Default collation
# # # Default rounding mode
# # # ROUNDING_MODE_UNSPECIFIED
# # # Time travel window
# # # 7 days
# # # Storage billing model
# # # LOGICAL
# # # Case insensitive
# # # false
# # # Labels
# # # Tags


# # class AlbumLoader:
# #     def __init__(self, project_id, dataset_id, table_id, album_ids, client_id, client_secret):
# #         self.client = bigquery.Client(project=project_id)
# #         self.table_ref = self.client.dataset(dataset_id).table(table_id)
# #         self.album_ids = album_ids
# #         self.client_id = client_id
# #         self.client_secret = client_secret

# #         # Schema for data insertion
# #         self.schema = [
# #             bigquery.SchemaField("album_id", "STRING", mode="REQUIRED"),
# #             bigquery.SchemaField("album_name", "STRING", mode="REQUIRED"),
# #             bigquery.SchemaField("album_popularity", "FLOAT"),
# #             bigquery.SchemaField("Number_of_track", "INTEGER"),
# #             bigquery.SchemaField("genre", List[Union[str, None]], mode="REPEATED"),
# #             bigquery.SchemaField("release_date", "DATE"),
# #             bigquery.SchemaField("Label", "STRING"),
# #         ]

# #     def load_albums(self):
# #         try:
# #             access_token = get_spotify_token(self.client_id, self.client_secret)
# #             album_obj = AlbumExtract(self.album_ids, access_token)
# #             album_obj.ExtractAlbumData()
# #             album_data_dict = album_obj.get_album_data()

# #             # Retrieve table schema if it exists, otherwise create it
# #             table = self.client.get_table(self.table_ref)
# #             if not table:
# #                 table = bigquery.Table(self.table_ref, schema=self.schema)
# #                 self.client.create_table(table)

# #             for album_id, album_info in album_data_dict.items():
# #                 row_to_insert = (
# #                     album_id,
# #                     album_info['album_name'],
# #                     album_info['popularity'],
# #                     album_info['tracks'],
# #                     album_info['genres'],
# #                     album_info['release_date'],
# #                     album_info['labels']
# #                 )

# #                 errors = self.client.insert_rows(self.table_ref, [row_to_insert], selected_fields=self.schema)

# #                 if errors:
# #                     print(f"Error inserting row for album {album_id}: {errors}")
# #                 else:
# #                     print(f"Row for album {album_id} inserted successfully.")

# #         except Exception as e:
# #             print(f"An error occurred: {e}")

# # if __name__ == "__main__":
# #     project_id = 'cobalt-particle-329816'
# #     dataset_id = 'demoDataset_001'
# #     table_id = 'table_id'
# #     album_ids = ["382ObEPsp2rxGrnsizN5TX", "1A2GTWGtFfWp7KSQTwWOyo", "2noRn2Aes5aoNVsU6iWThc"]
# #     client_id = os.getenv('spotify_client_id')
# #     client_secret = os.getenv('spotify_client_secret')

# #     loader = AlbumLoader(project_id, dataset_id, table_id, album_ids, client_id, client_secret)
# #     loader.load_albums()



import os
import sys
from typing import List, Union


project_root = '/home/mayank/Desktop/Project/DE/Spotify/ETL'
sys.path.append(project_root)

from Extract.AlbumExtract import AlbumExtract #AlbumExtract is a class
from Config.config import get_spotify_token #get_spotify_token is function

class RedshiftAlbumLoader:
    def __init__(self, album_ids, client_id, client_secret):
        #self.connection = self._create_connection(cluster_host, database, port, user, password)
        self.album_ids = album_ids
        self.client_id = client_id
        self.client_secret = client_secret

        # Schema for data insertion
        self.schema = [
            ("album_id", "VARCHAR(255)"),
            ("album_name", "VARCHAR(255)"),
            ("album_popularity", "FLOAT"),
            ("Number_of_track", "INTEGER"),
            ("release_date", "DATE"),
            ("Label", "VARCHAR(255)"),
        ]


    def load_albums(self,connection):
        try:
            access_token = get_spotify_token(self.client_id, self.client_secret)
            album_obj = AlbumExtract(self.album_ids, access_token)
            album_obj.ExtractAlbumData()
            album_data_dict = album_obj.get_album_data()
            
            self.connection = connection

            cursor = self.connection.cursor()

            # Create table if not exists
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS albums (
                {", ".join([f"{field[0]} {field[1]}" for field in self.schema])}
            );
            """
            cursor.execute(create_table_query)
            self.connection.commit()

            for album_id, album_info in album_data_dict.items():
                insert_query = f"""
                INSERT INTO albums VALUES (
                    '{album_id}',
                    '{album_info['album_name']}',
                    {album_info['popularity']},
                    {album_info['tracks']},
                    '{album_info['release_date']}',
                    '{album_info['labels']}'
                );
                """
                cursor.execute(insert_query)
                self.connection.commit()
                print(f"Row for album {album_id} inserted successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            if self.connection:
                self.connection.close()
                print("Connection closed.")

# if __name__ == "__main__":
#     cluster_host = 'redshift-cluster-1.ckzav7enrh1x.us-east-1.redshift.amazonaws.com'
#     database = 'dev'
#     port = 5439
#     user = 'awsuser'
#     password = 'King1714'
#     album_ids = ["382ObEPsp2rxGrnsizN5TX", "1A2GTWGtFfWp7KSQTwWOyo", "2noRn2Aes5aoNVsU6iWThc"]
#     client_id = os.getenv('spotify_client_id')
#     client_secret = os.getenv('spotify_client_secret')

#     loader = RedshiftAlbumLoader(cluster_host, database, port, user, password, album_ids, client_id, client_secret)
#     conn = loader.create_connection(cluster_host, database, port, user, password)
#     loader.load_albums(conn)


    
    
