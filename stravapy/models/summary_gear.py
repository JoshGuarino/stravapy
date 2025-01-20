from typing import TypedDict

class SummaryGear(TypedDict):
    id: str
    resource_state: int
    primary: bool
    name: str
    distance: float
