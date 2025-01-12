from dataclasses import dataclass

@dataclass
class UpdatableActivity:
    commute: bool
    trainer: bool
    hide_from_home: bool
    description: str
    name: str
    sport_type: str #todo make enum class for sport_type  
    gear_id: str
