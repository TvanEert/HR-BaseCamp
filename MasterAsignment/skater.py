from datetime import datetime

class Skater:

    def __init__(self, id: int, first_name: str, last_name: str, nationality: str, gender: str, date_of_birth: datetime) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.gender = gender
        self.date_of_birth = date_of_birth


    def get_age(self, date: datetime = None) -> int:
        if date == None:
            date = datetime.now()

    
    def get_events() -> list:
        pass

    
    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))
