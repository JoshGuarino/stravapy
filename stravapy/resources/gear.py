from stravapy.request import Request

class Gear:
    def __init__(self, url: str, headers: dict):
        self.url = url
        self.headers = headers

    def gear_by_id(self, id: str):
        r = Request().get(f'{self.url}/gear/{id}', self.headers)
        return r.json()
