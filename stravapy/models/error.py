from dataclasses import dataclass

@dataclass
class Error:
    code: str
    field: str
    resource: str
