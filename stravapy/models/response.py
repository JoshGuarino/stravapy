from dataclasses import dataclass
from stravapy.models.fault import Fault
from typing import Generic, TypeVar

T = TypeVar('T')

@dataclass
class ResponseDict(Generic[T]):
    data: T | None 
    error: Fault | None

@dataclass
class ResponseList(Generic[T]):
    data: list[T] 
    error: Fault | None
