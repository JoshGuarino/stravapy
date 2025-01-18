from typing import TypedDict
from stravapy.models.meta_athlete import MetaAthlete

class ClubActivity(TypedDict):
    athlete: MetaAthlete
    name: str
    distance: float
    moving_time: int
    elapsed_time: int
    total_elevation_gain: float
    sport_type: str # todo implment sport_type enum class 
    workout_type: int
