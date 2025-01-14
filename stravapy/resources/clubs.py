from stravapy.models.club_athlete import ClubAthlete
from stravapy.models.fault import Fault
from stravapy.request import Request

class Clubs:
    def __init__(self, url: str, headers: dict):
        self.url = url
        self.headers = headers

    def get_club_activities_by_id(self, id: int, page: int = 1, per_page: int = 30):
        r = Request().get(f'{self.url}/{id}/activities?page={page}&per_page={per_page}', self.headers)
        if r.ok: 
            return r.json()
        return Fault(**r.json())

    def get_club_admins_by_id(self, id: int, page: int = 1, per_page: int = 30):
        r = Request().get(f'{self.url}/{id}/admins?page={page}&per_page={per_page}', self.headers)
        if r.ok:
            return r.json()
        return Fault(**r.json())

    def get_club_by_id(self, id: int):
        r = Request().get(f'{self.url}/{id}', self.headers)
        if r.ok:
            return r.json()
        return Fault(**r.json())

    def get_club_members_by_id(self, id: int, page: int = 1, per_page: int = 30) -> list[ClubAthlete] | Fault:
        r = Request().get(f'{self.url}/{id}/members?page={page}&per_page={per_page}', self.headers)
        if r.ok:
            return [ClubAthlete(**athlete) for athlete in r.json()]
        return Fault(**r.json())
