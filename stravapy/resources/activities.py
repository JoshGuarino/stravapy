from stravapy.models.comment import Comment
from stravapy.models.fault import Fault
from stravapy.models.lap import Lap
from stravapy.models.response import ResponseDict, ResponseList
from stravapy.models.summary_athlete import SummaryAthlete
from stravapy.models.updatable_activity import UpdatableActivity
from stravapy.models.detailed_activity import DetailedActivity
from stravapy.request import Request
from datetime import datetime
from dataclasses import asdict

class Activities:
    def __init__(self, url, headers):
            self.url = url
            self.headers = headers

    def create_activity(
        self, 
        name: str, 
        activity_type: str, 
        start_date_local: datetime,
        elapsed_time: int, 
        description: str = "", 
        distance: int = 0, 
        trainer: bool = False, 
        commute: bool = False
    ) -> ResponseDict[DetailedActivity]:
        data = {
            "name": name,
            "type": activity_type,
            "start_date_local": start_date_local.isoformat(),
            "elapsed_time": elapsed_time,
            "description": description,
            "distance": distance,
            "trainer": trainer,
            "commute": commute
        }
        r = Request().post(self.url, self.headers, data)
        if r.ok:
            data = DetailedActivity(**r.json())
            return ResponseDict(data=data, error=None)
        error =  Fault(**r.json())
        return ResponseDict(data=None, error=error)

    def get_activity_by_id(self, id: int, include_all_efforts=False) -> ResponseDict[DetailedActivity]:
        r = Request().get(f'{self.url}/{id}?include_all_efforts={include_all_efforts}', self.headers)
        if r.ok:
            data = DetailedActivity(**r.json())
            return ResponseDict(data=data, error=None)
        error = Fault(**r.json())
        return ResponseDict(data=None, error=error)
    
    def get_comments_by_activity_id(self, id: int, page: int = 1, per_page: int = 30) -> ResponseList[Comment]:
        r = Request().get(f'{self.url}/{id}/comments?page={page}&per_page={per_page}', self.headers)
        if r.ok:
            data = [Comment(**comment) for comment in r.json()] 
            return ResponseList(data=data, error=None)
        error = Fault(**r.json())
        return ResponseList(data=[], error=error) 

    def get_kudoers_by_activity_id(self, id: int, page: int = 1, per_page: int = 30) -> ResponseList[SummaryAthlete]:
        r = Request().get(f'{self.url}/{id}/kudos?page={page}&per_page={per_page}', self.headers)
        if r.ok:
            data = [SummaryAthlete(**athlete) for athlete in r.json()]
            return ResponseList(data=data, error=None)
        error = Fault(**r.json())
        return ResponseList(data=[], error=error)

    def get_laps_by_activity_id(self, id: int) -> ResponseList[Lap]:
        r = Request().get(f'{self.url}/{id}/laps', self.headers)
        if r.ok:
            data = [Lap(**lap) for lap in r.json()]
            return ResponseList(data=data, error=None)
        error = Fault(**r.json())
        return ResponseList(data=[], error=error)

    # todo
    def get_zones_by_activity_id(self, id: int):
        r = Request().get(f'{self.url}/{id}/zones', self.headers)
        return r.json()

    def update_activity_by_id(self, id: int, updatable_activity: UpdatableActivity) -> ResponseDict[DetailedActivity]:
        r = Request().put(f'{self.url}/{id}', self.headers, updatable_activity)
        if r.ok:
            data = DetailedActivity(**r.json())
            return ResponseDict(data=data, error=None)
        error = Fault(**r.json())
        return ResponseDict(data=None, error=error)
