from stravapy.models.club_activity import ClubActivity
from stravapy.models.club_athlete import ClubAthlete
from stravapy.models.detailed_club import DetailedClub
from stravapy.models.fault import Fault
from stravapy.models.response import ResponseDict, ResponseList 
from stravapy.models.summary_athlete import SummaryAthlete
from stravapy.request import Request

class Clubs:
    def __init__(self, url: str, headers: dict):
        self.url = url
        self.headers = headers

    def get_club_activities_by_id(self, id: int, page: int = 1, per_page: int = 30) -> ResponseList[ClubActivity]:
        r = Request().get(f'{self.url}/{id}/activities?page={page}&per_page={per_page}', self.headers)
        if r.ok: 
            data = [ClubActivity(**activity) for activity in r.json()]
            return ResponseList(data=data, error=None)
        error = Fault(**r.json())
        return ResponseList(data=[], error=error)

    def get_club_admins_by_id(self, id: int, page: int = 1, per_page: int = 30) -> ResponseList[SummaryAthlete]:
        r = Request().get(f'{self.url}/{id}/admins?page={page}&per_page={per_page}', self.headers)
        if r.ok:
            data = [SummaryAthlete(**athlete) for athlete in r.json()]
            return ResponseList(data=data, error=None)
        error = Fault(**r.json())
        return ResponseList(data=[], error=error)

    def get_club_by_id(self, id: int) -> ResponseDict[DetailedClub]:
        r = Request().get(f'{self.url}/{id}', self.headers)
        if r.ok:
            data = DetailedClub(**r.json())
            return ResponseDict(data=data, error=None)
        error = Fault(**r.json())
        return ResponseDict(data=None, error=error)

    def get_club_members_by_id(self, id: int, page: int = 1, per_page: int = 30) -> ResponseList[ClubAthlete]:
        r = Request().get(f'{self.url}/{id}/members?page={page}&per_page={per_page}', self.headers)
        if r.ok:
            data = [ClubAthlete(**athlete) for athlete in r.json()]
            return ResponseList(data=data, error=None)
        error = Fault(**r.json())
        return ResponseList(data=[], error=error)
