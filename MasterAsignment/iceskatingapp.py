import os
import sys
import json
import sqlite3

from skater import Skater
from track import Track
from event import Event

def is_db_empty(con, cur):
    is_empty = cur.execute("SELECT * FROM tracks WHERE EXISTS(SELECT id FROM tracks WHERE tracks.id = 0 OR tracks.id > 0)")
    if is_empty.fetchone() == None:
       fill_tracks_table(con, cur)
    else:
        print("tracks table already populated")

    is_empty = cur.execute("SELECT * FROM events WHERE EXISTS(SELECT id FROM events WHERE events.id = 0 OR events.id > 0)")
    if is_empty.fetchone() == None:
       fill_events_table(con, cur)
    else:
        print("events table already populated")

    is_empty = cur.execute("SELECT * FROM skaters WHERE EXISTS(SELECT id FROM skaters WHERE skaters.id = 0 OR skaters.id > 0)")
    if is_empty.fetchone() == None:
       fill_skaters_table(con, cur)
    else:
        print("skaters table already populated")

    is_empty = cur.execute("SELECT * FROM event_skaters WHERE EXISTS(SELECT skater_id FROM event_skaters WHERE event_skaters.skater_id = 0 OR event_skaters.skater_id > 0)")
    if is_empty.fetchone() == None:
       fill_event_skaters_table(con, cur)
    else:
        print("event_skater table already populated")


def fill_tracks_table(con, cur):
    print("Filling tracks table...")
    data = read_json_file("events.json")
    for event in data:
        track_id = event["track"]["id"]
        track_name = event["track"]["name"]
        track_city = event["track"]["city"]
        track_country = event["track"]["country"]
        track_isoutdoor = event["track"]["isOutdoor"]
        track_altitude = event["track"]["altitude"]
        id_exists = cur.execute("SELECT * FROM tracks WHERE EXISTS(SELECT id FROM tracks WHERE tracks.id=:id)",
                                {"id": track_id})
        if id_exists.fetchone() == None:
            cur.execute("""INSERT INTO tracks VALUES (:id, :name,
                           :city, :country, :isoutdoor, :altitude)""",
                        {"id": track_id, 
                         "name": track_name, 
                         "city": track_city,
                         "country": track_country,
                         "isoutdoor": track_isoutdoor,
                         "altitude": track_altitude})
        
    con.commit()

def fill_events_table(con, cur):
    print("Filling events table...")

def fill_skaters_table(con, cur):
    print("Filling skaters table...")

def fill_event_skaters_table(con, cur):
    print("Filling event_skaters table...")

def read_json_file(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    
    return data

def main():
    con = sqlite3.connect(os.path.realpath("iceskatingapp.db"))
    cur = con.cursor()
    is_db_empty(con, cur)
    con.close()

if __name__ == "__main__":
    main()
