from typing import TypedDict
from stravapy.models.summary_pr_segment_effort import SummaryPrSegmentEffort
from stravapy.models.summary_segment_effort import SummarySegmentEffort

class SummarySegment(TypedDict):
    id: int
    name: str
    activity_type: str
    distance: float
    average_grade: float
    maximum_grade: float
    elevation_high: float
    elevation_low: float
    start_latlng: list[float]
    end_latlng: list[float]
    climb_category: int
    city: str
    state: str
    country: str
    private: bool
    athlete_pr_effort: SummaryPrSegmentEffort
    athlete_segment_stats: SummarySegmentEffort
