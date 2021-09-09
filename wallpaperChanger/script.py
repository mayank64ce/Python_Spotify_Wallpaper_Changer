import json
import base64
import requests
import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..")) # just go one level up
from wallpaperChanger.SpotifyAPI import SpotifyAPI
from wallpaperChanger.server_codes import CLIENT_ID, CLIENT_SECRET

client_id = CLIENT_ID
client_secret = CLIENT_SECRET

# print('BUGGG')

spotify = SpotifyAPI(client_id, client_secret)
spotify.perform_auth()
data = spotify.get_current_song()
os.system("cls")
print(data['item']['name'], ' by ' ,data['item']['artists'][0]['name'])
# print(spotify.access_token, 'hello')



