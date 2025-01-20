from typing import TypedDict
from datetime import datetime
from summary_athlete import SummaryAthlete

class Comment(TypedDict):
    id: int
    activity_id: int
    text: str
    athlete: SummaryAthlete 
    created_at: datetime 
