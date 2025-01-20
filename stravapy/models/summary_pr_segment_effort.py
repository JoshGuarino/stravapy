from datetime import datetime
from typing import TypedDict

class SummaryPrSegmentEffort(TypedDict):
    pr_activity_id: int
    pr_elapsed_time: int
    pr_date: datetime
    effort_count: int
