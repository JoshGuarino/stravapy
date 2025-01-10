from stravapy.request import Request

class Segments:
    def __init__(self, url: str, headers: dict):
        self.url = url
        self.headers = headers

    def explore_segments(self, bounds: list[float], activity_type: str = 'all', min_cat: int = 0, max_cat: int = 6):
        r = Request().get(
            f'{self.url}/explore?bounds={bounds}&activity_type={activity_type}&min_cat={min_cat}&max_cat={max_cat}',
            self.headers
        ) 
        return r.json()

    def get_logged_in_athlete_starred_segments(self, page: int = 1, per_page: int = 30):
        r = Request().get(f'{self.url}/starred?page={page}&per_page={per_page}', self.headers) 
        return r.json()

    def get_segment_by_id(self, id: int):
        r = Request().get(f'{self.url}/{id}', self.headers) 
        return r.json()

    def star_segment(self, id: int, starred: bool = False):
        r = Request().put(f'{self.url}/{id}/starred', self.headers, {'starred': starred}) 
        return r.json()
