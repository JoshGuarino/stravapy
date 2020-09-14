from request import Request

class Activities(object):

    def create_activity(name, type, start_date_local, elapsed_time, description=None, distance=None, trainer=None, commute=None):
        Request.post()
        return

    def get_activity_by_id(id, include_all_efforts=None):
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

    def update_activity_by_id(id):
        Request.put()
        return