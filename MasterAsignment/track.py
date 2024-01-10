import sqlite3


class Track:

    def __init__(self, id: int, name: str, city: str, country: str, outdoor: bool, altitude: int) -> None:
        self.id = id
        self.name = name
        self.city = city
        self.country = country
        self.outdoor = outdoor
        self.altitude = altitude

    def get_events(self) -> list:
        con = sqlite3.connect("iceskatingapp.db")
        cur = con.cursor()

        events = cur.execute("SELECT * FROM events WHERE events.track_id = :track_id", {"track_id": self.id})
        events = events.fetchall()

        con.close()

        return events

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))
