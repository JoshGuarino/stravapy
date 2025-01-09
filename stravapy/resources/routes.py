from stravapy.request import Request

class Routes(object):
    def __init__(self, url: str, headers: dict):
        self.url = url
        self.headers = headers

    def get_route_as_gpx(self, id: int):
        r = Request().get(f'{self.url}/{id}/export_gpx', self.headers) 
        return r.json()

    def ger_route_as_tcx(self, id: int):
        r = Request().get(f'{self.url}/{id}/export_tcx', self.headers) 
        return r.json()
        
    def get_route_by_id(self, id: int):
        r = Request().get(f'{self.url}/{id}', self.headers) 
        return r.json()
