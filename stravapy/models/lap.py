from datetime import datetime
from typing import TypedDict
from stravapy.models.meta_activity import MetaActivity
from stravapy.models.meta_athlete import MetaAthlete

class Lap(TypedDict):
    id: int
    activity: MetaActivity 
    athlete: MetaAthlete
    average_cadence: float
    average_speed: float
    distance: float
    elapsed_time: int
    start_index: int
    end_index: int
    lap_index: int
    max_speed: float
    moving_time: int
    name: str
    pace_zone: int
    split: int
    start_date: datetime
    start_date_local: datetime
    total_elevation_gain: float
