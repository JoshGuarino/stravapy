from stravapy.request import Request

class Athlete:
    def __init__(self, url: str, headers: dict):
        self.url = url
        self.headers = headers
    
    #todo
    def get_logged_in_athlete_activities(self):
        r = Request.get(f'{self.url}/activities', self.headers)
        return r.json()

    def get_logged_in_athlete(self):
        r = Request.get(self.url, self.headers)
        return r.json()

    def get_logged_in_athlete_zones(self):
        r = Request.get(f'{self.url}/zones', self.headers)
        return r.json()

    def get_stats(self, id: int):
        r = Request.get(f'{self.url}s/{id}/stats', self.headers)
        return r.json()

    #todo
    def update_logged_in_athlete(self, weight: int):
        r = Request.put(self.url, self.headers)
        return r.json()
    
    #todo
    def get_logged_in_athlete_clubs(self):
        r = Request.put(f'{self.url}/clubs', self.headers)
        return r.json()

    #todo
    def get_routes_by_athlete_id(self):
        r = Request.put(f'{self.url}s/{id}/routes', self.headers)
        return r.json()