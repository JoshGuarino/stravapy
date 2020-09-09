from resources import *
from request import Request
from oauth import Oauth

class Stravapy:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = 'https://www.strava.com/api/v3'
        self.headers = { 'Authorization' : f'Bearer: {access_token}' }

        