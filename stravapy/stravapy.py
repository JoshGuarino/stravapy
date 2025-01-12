from stravapy.resources import *

class Stravapy:
   def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = 'https://www.strava.com/api/v3'
        self.headers = { 'Authorization' : f'Bearer {self.access_token}' }
        self.activities = activities.Activities(f'{self.base_url}/activities', self.headers)
        self.athlete = athlete.Athlete(f'{self.base_url}/athlete', self.headers) 
        self.clubs = clubs.Clubs(f'{self.base_url}/clubs', self.headers)
        self.gear = gear.Gear(f'{self.base_url}/gear', self.headers)
        self.routes = routes.Routes(f'{self.base_url}/routes', self.headers) 
        self.segment_efforts = segment_efforts.SegmentEfforts(f'{self.base_url}/segment_efforts', self.headers) 
        self.segments = segments.Segments(f'{self.base_url}/segments', self.headers)
        self.streams = streams.Streams #todo
        self.uploads = uploads.Uploads #todo
