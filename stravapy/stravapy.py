from stravapy.resources import *

class Stravapy:
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = 'https://www.strava.com/api/v3'
        self.headers = { 'Authorization' : f'Bearer {self.access_token}' }
        self.activities = activities.Activities(f'{self.base_url}/activities', self.headers)
        self.athlete = athlete.Athlete(f'{self.base_url}/athlete', self.headers)
        self.clubs = clubs.Clubs
        self.gear = gear.Gear(f'{self.base_url}/gear', self.headers)
        self.routes = routes.Routes
        self.running_races = running_races.RunningRaces
        self.segment_efforts = segment_efforts.SegmentEfforts
        self.segments = segments.Segments
        self.streams = streams.Streams
        self.uploads = uploads.Uploads