from stravapy.models.detailed_gear import DetailedGear
from stravapy.models.fault import Fault
from stravapy.request import Request

class Gear:
    def __init__(self, url: str, headers: dict) -> None:
        self.url = url
        self.headers = headers

    def gear_by_id(self, id: str) -> DetailedGear | Fault:
        r = Request().get(f'{self.url}/gear/{id}', self.headers)
        if r.ok:
            return DetailedGear(**r.json())
        else:
            return Fault(**r.json())
