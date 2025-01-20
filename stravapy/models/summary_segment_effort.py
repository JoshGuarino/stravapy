from datetime import datetime
from typing import TypedDict

class SummarySegmentEffort(TypedDict):
    id: int
    activity_id: int
    elapsed_time: int
    start_date: datetime
    start_date_local: datetime
    distance: float
    is_kom: bool
