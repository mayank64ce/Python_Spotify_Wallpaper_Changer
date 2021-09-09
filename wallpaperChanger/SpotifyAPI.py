import webbrowser
from urllib.parse import urlencode
import requests
import datetime
import os, sys

from requests.models import Response
sys.path.append(os.path.join(os.path.dirname(__file__), "..")) # just go one level up
from wallpaperChanger.server import get_callback_code
from wallpaperChanger.server_codes import SERVER_URL


class SpotifyAPI(object):

    code = None
    access_token = None
    refresh_token = None
    access_token_expires = datetime.datetime.now()
    client_id = None
    access_token_did_expire = True
    client_secret = None
    redirect_uri = SERVER_URL[:-1] # setup later Gotta rick roll
    token_url = 'https://accounts.spotify.com/authorize?'
    scope = 'user-read-currently-playing'

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret
        self.authorize_url = self.token_url + urlencode({
                                                        'client_id' : self.client_id,
                                                        'response_type':'code',
                                                        'redirect_uri' : self.redirect_uri,
                                                        'scope' : self.scope
                                                        })
    
    def request_token(self, data):
        # print('request_token')
        if 'error' in data:
            # print(data)
            raise Exception(data['error'], data['error_discription'])
        else:
            # print(data)
            return data['access_token'] if 'access_token' in data else None, data['refresh_token'] if 'refresh_token' in data else None

    def get_auth_token_with_auth_code(self, auth_code):
        token_url = 'https://accounts.spotify.com/api/token'

        response = requests.post(token_url, data = {
            'grant_type' : 'authorization_code',
            'code' : auth_code,
            'redirect_uri': self.redirect_uri,
            'client_id' : self.client_id,
            'client_secret' : self.client_secret
        })

        return self.request_token(response.json())
    
    
    
    
    def get_auth_token_with_refresh_token(self, refresh_token):
        token_url = 'https://accounts.spotify.com/api/token'
        response = requests.post(token_url, data = {
            'grant_type' : 'refresh_token',
            'refresh_token' : refresh_token,
            'client_id' : self.client_id,
            'client_secret' : self.client_secret
        })

        return self.request_token(response.json())


    def perform_auth(self):
        # print('perform_auth')
        while not self.access_token:
            if self.refresh_token:
                self.access_token, self.refresh_token = self.get_auth_token_with_refresh_token(self.refresh_token)
                # print("access_token", self.access_token)
                # print("refresh_token", self.refresh_token)
            elif self.code:
                self.access_token, self.refresh_token = self.get_auth_token_with_auth_code(self.code)
                # print("access_token", self.access_token)
                # print("refresh_token", self.refresh_token)
            else:
                webbrowser.open_new_tab(self.authorize_url)
                self.code = get_callback_code()
                print(self.code)

    def get_current_song(self):
        
        if not self.access_token:
            self.perform_auth()
        access_token = self.access_token
        query_url = 'https://api.spotify.com/v1/me/player/currently-playing?market=IN'

        headers = {
            'Authorization' : f'Bearer {access_token}'
        }

        response = requests.get(query_url, headers = headers)

        return response.json()

    # Implement get_artist_info()
    # Implement get_genres()
    # Implement change_wallpapers()






