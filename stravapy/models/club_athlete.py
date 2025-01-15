from typing import TypedDict

class ClubAthlete(TypedDict):
    resource_state: int
    firstname: str
    lastname: str
    membership: str
    admin: bool
    owner: bool
