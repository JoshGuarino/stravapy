from typing import TypedDict 

class DetailedGear(TypedDict):
    id: str
    resource_state: int
    primary: bool
    name: str
    distance: float
    brand_name: str
    model_name: str
    frame_type: int
    description: str
