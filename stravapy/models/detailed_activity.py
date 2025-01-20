from typing import TypedDict
from datetime import datetime
from stravapy.models.detailed_segment_effort import DetailedSegmentEffort
from stravapy.models.lap import Lap
from stravapy.models.meta_athlete import MetaAthlete
from stravapy.models.photo_summary import PhotoSummary
from stravapy.models.polyline_map import PolylineMap
from stravapy.models.split import Split
from stravapy.models.summary_gear import SummaryGear

class DetailedActivity(TypedDict):
    id: int
    external_id: str
    upload_id: int
    athlete: MetaAthlete
    name: str
    distance: float
    moving_time: int
    elapsed_time: int
    total_elevation_gain: float
    elev_high: float
    elev_low: float
    sport_type: str # todo make enum class 
    start_date: datetime
    start_date_local: datetime
    timezone: str
    start_latlng: list[float]
    end_latlng: list[float]
    achievement_count: int
    kudos_count: int
    comment_count: int
    athlete_count: int
    photo_count: int
    total_photo_count: int
    map: PolylineMap
    trainer: bool   
    commute: bool
    manual: bool
    private: bool
    flagged: bool
    workout_type: int
    upload_id_str: str
    average_speed: float
    max_speed: float
    has_kudoed: bool
    hide_from_home: bool
    gear_id: str
    kilojoules: float
    average_watts: float
    device_watts: bool
    max_watts: bool
    weighted_average_watts: int
    description: str
    photos: PhotoSummary
    gear: SummaryGear
    calories: float
    segment_efforts: DetailedSegmentEffort 
    device_name: str
    embed_token: str
    spilts_metric: list[Split]
    splits_standard: list[Split]
    laps: list[Lap]
    best_efforts: DetailedSegmentEffort 
