from typing import TypedDict
from stravapy.models.error import Error

class Fault(TypedDict):
    errors: list[Error]
    message: str
