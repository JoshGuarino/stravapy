from stravapy.resources import *

class Stravapy:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = 'https://www.strava.com/api/v3'
        self.headers = { 'Authorization' : f'Bearer: {access_token}' }
        self.activities = activities.Activities
        self.athlete = athlete.Athlete
        self.clubs = clubs.Clubs
        self.gear = gear.Gear
        self.routes = routes.Routes
        self.running_races = running_races.RunningRaces
        self.segment_efforts = segment_efforts.SegmentEfforts
        self.segments = segments.Segments
        self.streams = streams.Streams
        self.uploads = uploads.Uploads