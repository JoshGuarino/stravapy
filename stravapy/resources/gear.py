from stravapy.models.detailed_gear import DetailedGear
from stravapy.models.fault import Fault
from stravapy.models.response import ResponseDict
from stravapy.request import Request

class Gear:
    def __init__(self, url: str, headers: dict) -> None:
        self.url = url
        self.headers = headers

    def gear_by_id(self, id: str) -> ResponseDict[DetailedGear]:
        r = Request().get(f'{self.url}/gear/{id}', self.headers)
        if r.ok:
            data = DetailedGear(**r.json())
            return ResponseDict(data=data, error=None) 
        error = Fault(**r.json())
        return ResponseDict(data=None, error=error) 
