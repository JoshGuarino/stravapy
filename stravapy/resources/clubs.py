from stravapy.request import Request

class Clubs:
    def __init__(self, url: str, headers: dict):
        self.url = url
        self.headers = headers

    def get_club_activities_by_id(self, id: int):
        r = Request.get(f'{self.url}/{id}/activities', self.headers)
        return r.json()

    def get_club_admins_by_id(self, id: int):
        r = Request.get(f'{self.url}/{id}/admins', self.headers)
        return r.json()

    def get_club_by_id(self, id: int):
        r = Request.get(f'{self.url}/{id}', self.headers)
        return r.json()

    def get_club_members_by_id(self, id: int):
        r = Request.get(f'{self.url}/{id}/members', self.headers)
        return r.json()