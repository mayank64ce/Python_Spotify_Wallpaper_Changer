import datetime
import base64
import requests

class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    client_id = None
    access_token_did_expire = True
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token'

    def __init__(self, client_id, client_secret,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_token_data(self):
        return {
                'grant_type': 'client_credentials'
            }

    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            'Authorization': f'Basic {client_creds_b64}'
        }
    
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        respone = requests.post(token_url, data=token_data, headers=token_headers)
        valid_request = respone.status_code in range(200,299)
        # print(respone.json())
        # print('hello')

        if not valid_request:
            return False
        
        data = respone.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in']
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        self.access_token = access_token
        
        return True
        
    
    def get_client_credentials(self):
        """
        Returns base64 encoded string
        """
        client_id = self.client_id
        client_secret = self.client_secret

        if client_secret == None or client_id == None:
            raise Exception('You must set client_id and client_secret!!')

        client_creds = f'{client_id}:{client_secret}'
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()
