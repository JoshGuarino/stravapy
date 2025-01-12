from stravapy.request import Request
from datetime import datetime

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
    ):
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
        return r.json()

    def get_activity_by_id(self, id: int, include_all_efforts=False):
        r = Request().get(f'{self.url}/{id}?include_all_efforts={include_all_efforts}', self.headers)
        return r.json()
    
    # todo
    def get_comments_by_activity_id(self):
        Request().get(self.url, self.headers)
        return

    def get_kudoers_by_activity_id(self, id: int, page: int = 1, per_page: int = 30):
        r = Request().get(f'{self.url}/{id}/kudos?page={page}&per_page={per_page}', self.headers)
        return r.json()

    def get_lap_by_activity_id(self, id: int):
        r = Request().get(f'{self.url}/{id}/laps', self.headers)
        return r.json()

    def get_zones_by_activity_id(self, id: int):
        r = Request().get(f'{self.url}/{id}/zones', self.headers)
        return r.json()

    #todo
    def update_activity_by_id(self, id: int):
        r = Request().put(f'{self.url}/{id}', self.headers)
        return r.json()
