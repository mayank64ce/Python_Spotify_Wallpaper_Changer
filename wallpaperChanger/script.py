import json
import base64
import requests
import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..")) # just go one level up
from wallpaperChanger.newAPI import SpotifyAPI

client_id = '9f89ff0abf1e47e5a9e000579847b95c'
client_secret = '154036756caf4488b7047d16887d656c'

spotify = SpotifyAPI(client_id, client_secret)
print('AUTH')
spotify.perform_auth()
print('Auth DOne')
# access_token = spotify.access_token
# # access_token = 'BQAlOkh3KKdUkSnKx1E2pXjQmYIuSHyZD9-7KottZvof1TAas9Tl0bdk4VLwWqC8z2LuaSJzOCvyg_3-GUp9nt5NXU3j9xQKW-2-os8gNwdrYaKssY4MRCvqLdlaOYlKJUFax9VjqugJ2Xjq'
# headers = {
#     'Authorization' : f'Bearer {access_token}'
# }

# endpoint  = 'https://api.spotify.com/v1/me/player'

# # print(access_token)
# # print(spotify.access_token)
# response = requests.get(endpoint, headers=headers)
# # print(response.status_code)
# # print(response.json())
