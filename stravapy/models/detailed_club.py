from typing import TypedDict 

class DetailedClub(TypedDict):
    id: int
    resource_state: int
    name: str
    profile_medium: str
    cover_photo: str
    cover_photo_small: str
    activity_types: list[str]
    city: str
    state: str
    country: str
    private: bool
    member_count: int
    featured: bool
    verified: bool
    url: str
    membership: str
    admin: bool
    owner: bool
    follwing_count: int
