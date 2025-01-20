from datetime import datetime
from typing import TypedDict
from stravapy.models.meta_activity import MetaActivity
from stravapy.models.meta_athlete import MetaAthlete
from stravapy.models.summary_segment import SummarySegment

class DetailedSegmentEffort(TypedDict):
    id: int
    activity_id: int
    elapsed_time: int
    start_date: datetime
    start_date_local: datetime
    distance: float
    is_kom: bool
    name: str
    activity: MetaActivity
    athlete: MetaAthlete
    moving_time: int
    start_index: int
    end_index: int
    average_cadence: float
    average_watts: float
    device_watts: bool
    average_heartrate: float
    max_heartrate: float
    segment: SummarySegment 
    kom_rank: int
    pr_rank: int
    hidden: bool
