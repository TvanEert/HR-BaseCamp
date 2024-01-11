from datetime import datetime, timedelta
from skater import Skater
from track import Track
import sqlite3


class Event:

    def __init__(self, id: int, name: str, track_id: int, date: datetime, distance: int, duration: float,
                 laps: int, winner: int, category: str) -> None:
        self.id = id
        self.name = name
        self.track_id = track_id
        if date is None:
            self.date = datetime.today()
        else:
            self.date = datetime.strptime(date, '%Y-%m-%d')
        self.distance = distance
        self.duration = duration
        self.winner = winner
        self.category = category

    def add_skater(self, skater: Skater) -> None:
        pass

    def get_skaters(self) -> list:
        skaters = []

        con = sqlite3.connect("iceskatingapp.db")
        cur = con.cursor()

        skater_ids = cur.execute("SELECT * FROM event_skaters WHERE event_skaters.event_id = :event_id",
                                {"event_id": self.id})
        skater_ids = skater_ids.fetchall()

        for skater_id in skater_ids:
            skater = cur.execute("SELECT * FROM skaters WHERE skaters.id = :skater_id", {"skater_id": skater_id[0]})
            skater = skater.fetchone()
            skaters.append(skater)

        con.close()

        return skaters

    def get_track(self) -> Track:
        con = sqlite3.connect("iceskatingapp.db")
        cur = con.cursor()

        track = cur.execute("SELECT * FROM tracks WHERE tracks.id = :track_id", {"track_id": self.track_id})
        track = track.fetchone()

        con.close()

        track = Track(*track)

        return track

    def convert_date(self, to_format: str) -> str:
        return self.date.strftime(to_format)

    def convert_duration(self, to_format: str) -> str:
        if to_format == "%M:%S":
            min = str(int(self.duration) // 60).zfill(2)
            sec  = int(self.duration) % 60
            return f"{min}:{sec}"
        elif to_format == "%S":
            return str(int(self.duration))
        elif to_format == "%M":
            return str(int(self.duration) // 60).zfill(2)



    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))