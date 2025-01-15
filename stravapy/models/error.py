from typing import TypedDict

class Error(TypedDict):
    code: str
    field: str
    resource: str
