from stravapy.request import Request

class Activities:
    def __init__(self, url, headers):
            self.url = url
            self.headers = headers

    def create_activity(name: str, type, start_date_local, elapsed_time, description=None, distance=None, trainer=None, commute=None) -> None:
        Request.post()
        return

    def get_activity_by_id(id: int, include_all_efforts=False) -> None:
        Request.get()
        return
    
    def get_comments_by_activity_id(id, page=None, per_page=None):
        Request.get()
        return

    def get_kudoers_by_activity_id(id, page=None, per_page=None):
        Request.get()
        return

    def get_lap_by_activity_id(id):
        Request.get()
        return

    def get_logged_athlete_activities(before=None, after=None, page=None, per_page=None):
        Request.get()
        return

    def get_zones_by_activity_id(id):
        Request.get()
        return

    def update_activity_by_id(id: int):
        Request.put()
        return