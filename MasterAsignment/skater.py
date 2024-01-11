from datetime import datetime
import sqlite3


class Skater:

    def __init__(self, id: int, first_name: str, last_name: str, nationality: str, gender: str, date_of_birth: datetime) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.gender = gender
        self.date_of_birth = date_of_birth

    def get_age(self, date: datetime = None) -> int:
        if date is None:
            date = datetime.today()

        age = date.year - self.date_of_birth.year

        if (date.month, date.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age

    def get_events(self) -> list:
        events = []

        con = sqlite3.connect("iceskatingapp.db")
        cur = con.cursor()

        event_ids = cur.execute("SELECT * FROM event_skaters WHERE event_skaters.skater_id = :skater_id",
                                {"skater_id": self.id})
        event_ids = event_ids.fetchall()

        for event_id in event_ids:
            event = cur.execute("SELECT * FROM events WHERE events.id = :event_id",
                                {"event_id": event_id[1]})
            event = event.fetchone()
            events.append(event)

        con.close()

        return events

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))