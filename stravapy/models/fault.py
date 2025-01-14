from dataclasses import dataclass
from stravapy.models.error import Error

@dataclass
class Fault:
    errors: list[Error]
    message: str
