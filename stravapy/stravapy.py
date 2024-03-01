from stravapy.resources import *

class Stravapy:
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = 'https://www.strava.com/api/v3'
        self.headers = { 'Authorization' : f'Bearer {self.access_token}' }
        self.activities = activities.Activities(f'{self.base_url}/activities', self.headers) #todo
        self.athlete = athlete.Athlete(f'{self.base_url}/athlete', self.headers) #todo
        self.clubs = clubs.Clubs(f'{self.base_url}/clubs', self.headers)
        self.gear = gear.Gear(f'{self.base_url}/gear', self.headers)
        self.routes = routes.Routes #todo
        self.running_races = running_races.RunningRaces #todo
        self.segment_efforts = segment_efforts.SegmentEfforts #todo
        self.segments = segments.Segments #todo
        self.streams = streams.Streams #todo
        self.uploads = uploads.Uploads #todo