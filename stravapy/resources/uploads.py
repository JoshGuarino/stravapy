from stravapy.models.fault import Fault
from stravapy.models.response import ResponseDict
from stravapy.models.upload import Upload
from stravapy.request import Request

class Uploads:
    def __init__(self, url: str, headers: dict) -> None:
        self.url = url
        self.headers = headers

    def create_upload(self):
        return

    def get_upload_by_id(self, id: int) -> ResponseDict[Upload]:
        r = Request().get(f'{self.url}/{id}', self.headers)
        if r.ok:
            data = Upload(**r.json()) 
            return ResponseDict(data=data, error=None)
        error = Fault(**r.json())
        return ResponseDict(data=None, error=error)
