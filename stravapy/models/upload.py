from typing import TypedDict

class Upload(TypedDict):
    id: int
    id_str: str
    external_id: str
    error: str
    status: str
    activity_id: int
