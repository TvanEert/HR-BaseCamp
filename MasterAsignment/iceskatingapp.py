import json
import sqlite3
from datetime import datetime

from skater import Skater
from track import Track
from event import Event
from iceskatingreporter import Reporter


def is_db_empty(con, cur):
    is_tracks_empty = cur.execute("""SELECT * FROM tracks WHERE EXISTS
                                  (SELECT id FROM tracks WHERE
                                  tracks.id = 0 OR tracks.id > 0)""")
    if is_tracks_empty.fetchone() is None:
        fill_tracks_table(con, cur)
    else:
        print("tracks table already populated")

    is_events_empty = cur.execute("""SELECT * FROM events WHERE EXISTS
                                  (SELECT id FROM events WHERE
                                  events.id = 0 OR events.id > 0)""")
    if is_events_empty.fetchone() is None:
       fill_events_table(con, cur)
    else:
        print("events table already populated")

    is_skaters_empty = cur.execute("""SELECT * FROM skaters WHERE EXISTS
                                   (SELECT id FROM skaters WHERE
                                   skaters.id = 0 OR skaters.id > 0)""")
    if is_skaters_empty.fetchone() is None:
       fill_skaters_table(con, cur)
    else:
        print("skaters table already populated")

    is_event_skaters_empty = cur.execute("""SELECT * FROM event_skaters WHERE EXISTS
                                         (SELECT skater_id FROM event_skaters WHERE
                                         event_skaters.skater_id = 0 OR event_skaters.skater_id > 0)""")
    if is_event_skaters_empty.fetchone() is None:
       fill_event_skaters_table(con, cur)
    else:
        print("event_skater table already populated")


def fill_tracks_table(con, cur):
    print("Filling tracks table...")
    json_data = read_json_file("events.json")
    for event in json_data:
        track = event["track"]
        cur.execute("""INSERT INTO tracks VALUES (:id, :name,
                    :city, :country, :isoutdoor, :altitude)
                    ON CONFLICT (id) DO NOTHING""",
                    {"id": track["id"],
                     "name": track["name"],
                     "city": track["city"],
                     "country": track["country"],
                     "isoutdoor": track["isOutdoor"],
                     "altitude": track["altitude"]})

    con.commit()


def fill_events_table(con, cur):
    print("Filling events table...")
    json_data = read_json_file("events.json")
    for event in json_data:
        duration = convert_time_to_float(event["results"][0]["time"])
        cur.execute("""INSERT INTO events VALUES (:id, :name,
                    :track_id, :date, :distance, :duration,
                    :laps, :winner, :catagory)
                    ON CONFLICT (id) DO NOTHING""",
                    {"id": event["id"],
                     "name": event["title"],
                     "track_id": event["track"]["id"],
                     "date": event["start"],
                     "distance": event["distance"]["distance"],
                     "duration": duration,
                     "laps": event["distance"]["lapCount"],
                     "winner": event["results"][0]["skater"]["firstName"] +
                     " " + event["results"][0]["skater"]["lastName"],
                     "catagory": event["category"]})

    con.commit()


def fill_skaters_table(con, cur):
    print("Filling skaters table...")
    json_data = read_json_file("events.json")
    for event in json_data:
        for placement in event["results"]:
            skater = placement["skater"]
            cur.execute("""INSERT INTO skaters VALUES (:id, :first_name,
                        :last_name, :nationaliy, :gender, :date_of_birth)
                        ON CONFLICT (id) DO NOTHING""",
                        {"id": skater["id"],
                         "first_name": skater["firstName"],
                         "last_name": skater["lastName"],
                         "nationaliy": skater["country"],
                         "gender": skater["gender"],
                         "date_of_birth": skater["dateOfBirth"]})

    con.commit()


def fill_event_skaters_table(con, cur):
    print("Filling event_skaters table...")
    json_data = read_json_file("events.json")
    for event in json_data:
        for placement in event["results"]:
            skater = placement["skater"]
            cur.execute("INSERT INTO event_skaters VALUES (:skater_id, :event_id)",
                        {"skater_id": skater["id"],
                         "event_id": event["id"]})

    con.commit()
    
def convert_time_to_float(duration: str) -> float:
    if ":" in duration:
        duration = duration.split(":")
        min_to_sec = int(duration[0]) * 60
        time_in_float = float(duration[1]) + min_to_sec
    else:
        time_in_float = float(duration)
    return time_in_float
    
    
def read_json_file(file_name):
    with open(file_name, "r") as file:
        json_data = json.load(file)

    return json_data


def main():
    con = sqlite3.connect("iceskatingapp.db")
    cur = con.cursor()
    is_db_empty(con, cur)
    con.close()

    # tim = Skater(32, "Tim", "van Eert", "NL", "M", datetime(2002, 8, 7))
    # print(len(tim.get_events()))

    # track = Track(29, None, None, None, None, None)
    # print(len(track.get_events()))

    event = Event(1, "Essent ISU World Cup - 1500m Men Division A", 29, "2003-11-8", 1500, 107.370, 4, "Erben Wennemars", "M")
    
    print(event.convert_duration("%M:%S"))

    reporter = Reporter()
    print(reporter.highest_track())

if __name__ == "__main__":
    main()
