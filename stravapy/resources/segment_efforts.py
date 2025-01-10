from stravapy.request import Request
from datetime import datetime

class SegmentEfforts:
    def __init__(self, url: str, headers: dict):
        self.url = url
        self.headers = headers

    def get_efforts_by_segment_id(
        self, 
        segment_id: int, 
        start_date_local: datetime = datetime.fromtimestamp(0), 
        end_date_local: datetime = datetime.now(), 
        per_page: int = 30
    ):
        r = Request().get(
            f'''
            {self.url}
            ?segment_id={segment_id}
            &start_date_local={start_date_local.isoformat()}
            &end_date_local={end_date_local.isoformat()}
            &per_page={per_page}
            ''', 
            self.headers
        )
        return r.json()

    def get_segment_effort_by_id(self, id: int):
        r = Request().get(f'{self.url}/{id}', self.headers)
        return r.json()
