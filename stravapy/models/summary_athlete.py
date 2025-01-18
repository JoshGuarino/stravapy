from typing import TypedDict
from datetime import datetime

class SummaryAthlete(TypedDict):
    id: int
    resource_state: int
    firstname: str
    lastname: str
    profile_medium: str
    profile: str
    city: str
    state: str
    country: str
    sex: str
    premium: bool
    summit: bool
    created_at: datetime 
    updated_at: datetime 
