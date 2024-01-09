from datetime import datetime
from skater import Skater
from track import Track

class Event:

    def __init__(self, id: int, name:str, track_id: int, date: datetime, distance: int, duration: float, laps: int, winner: int, category: str) -> None:
        self.id = id
        self.name = name
        self.track_id = track_id
        self.date = datetime
        self.distance = distance
        self.duration = duration
        self.winner = winner
        self.category = category

    
    def add_skater(self, skater: Skater) -> None:
        pass


    def get_skaters(self) -> list[Skater]:
        pass


    def get_track() -> Track:
        pass


    def convert_date(to_format: str) -> str:
        pass


    def convert_duration(to_format: str) -> str:
        pass


    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))
