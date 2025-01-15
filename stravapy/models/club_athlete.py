from dataclasses import dataclass

@dataclass
class ClubAthlete:
    resource_state: int
    firstname: str
    lastname: str
    membership: str
    admin: bool
    owner: bool
