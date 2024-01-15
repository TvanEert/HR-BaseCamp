from track import Track
from event import Event
from skater import Skater
from datetime import datetime
import sqlite3
import csv


class Reporter:
    # How many skaters are there? -> int
    def total_amount_of_skaters(self) -> int:
        con = sqlite3.connect("iceskatingapp.db")
        cur = con.cursor()

        skaters = cur.execute("SELECT * FROM skaters").fetchall()

        con.close()

        return len(skaters)

    # What is the highest track? -> Track
    def highest_track(self) -> Track:
        con = sqlite3.connect("iceskatingapp.db")
        cur = con.cursor()

        track = cur.execute("SELECT * FROM tracks ORDER BY altitude DESC").fetchone()

        con.close()

        return Track(*track)

    # What is the longest and shortest event? -> tuple[Event, Event]
    def longest_and_shortest_event(self) -> tuple[Event, Event]:
        con = sqlite3.connect("iceskatingapp.db")
        cur = con.cursor()

        longest = cur.execute("SELECT * FROM events ORDER BY duration DESC").fetchone()
        shortest = cur.execute("SELECT * FROM events ORDER BY duration ASC").fetchone()

        con.close()

        return (Event(*longest), Event(*shortest))

    # Which event has the most laps for the given track_id -> tuple[Event, ...]
    def events_with_most_laps_for_track(self, track_id: int) -> tuple[Event, ...]:
        event_list = []

        con = sqlite3.connect("iceskatingapp.db")
        cur = con.cursor()

        highest_laps = cur.execute("SELECT laps FROM events WHERE events.track_id =:track_id ORDER BY laps DESC",
                                   {"track_id": track_id}).fetchone()

        events = cur.execute("SELECT * FROM events Where events.track_id = :track_id and events.laps = :laps",
                             {"track_id": track_id, "laps": highest_laps[0]}).fetchall()

        for event in events:
            event_list.append(Event(*event))

        con.close()

        return tuple(event_list)

    # Which skaters have made the most events -> tuple[Skater, ...]
    # Which skaters have made the most succesful events -> tuple[Skater, ...]
    def skaters_with_most_events(self, only_wins: bool = False) -> tuple[Skater, ...]:
        if only_wins:
            con = sqlite3.connect("iceskatingapp.db")
            cur = con.cursor()

            most_events_won = cur.execute("""SELECT winner,
                                          COUNT(winner)
                                          AS won_events
                                          FROM events
                                          GROUP BY winner
                                          ORDER BY won_events
                                          DESC LIMIT 1""").fetchone()

            skater_most_wins = cur.execute("SELECT * FROM skaters WHERE id = :id",
                                           {"id": most_events_won[0]}).fetchone()

            con.close()

            skater_most_wins_list = [Skater(*skater_most_wins)]

            return tuple(skater_most_wins_list)
        else:
            con = sqlite3.connect("iceskatingapp.db")
            cur = con.cursor()

            most_attended_events = cur.execute("""SELECT skater_id,
                                               COUNT(skater_id)
                                               AS attended_events
                                               FROM event_skaters
                                               GROUP BY skater_id
                                               ORDER BY attended_events
                                               DESC LIMIT 1""").fetchone()
            skater_most_attended = cur.execute("SELECT * FROM skaters WHERE skaters.id = :skater_id",
                                               {"skater_id": most_attended_events[0]}).fetchone()

            skater_most_attended_list = [Skater(*skater_most_attended)]

            con.close()

            return tuple(skater_most_attended_list)

    # Which track has the most events -> Track
    def tracks_with_most_events(self) -> tuple[Track, ...]:
        con = sqlite3.connect("iceskatingapp.db")
        cur = con.cursor()

        track_most_events_id = cur.execute("""SELECT track_id,
                                        COUNT(track_id)
                                        AS track_used
                                        FROM events
                                        GROUP BY track_id
                                        ORDER BY track_used
                                        DESC LIMIT 1""").fetchone()
        track_most_events = cur.execute("SELECT * FROM tracks WHERE tracks.id = :track_id",
                                        {"track_id": track_most_events_id[0]}).fetchone()

        track_most_events_list = [Track(*track_most_events)]

        con.close()

        return tuple(track_most_events_list)

    # Which track had the first event? -> Track
    # Which track had the first outdoor event? -> Track
    def get_first_event(self, outdoor_only: bool = False) -> Track:
        if outdoor_only:
            con = sqlite3.connect("iceskatingapp.db")
            cur = con.cursor()

            list_of_ids = []

            outdoor_tracks = cur.execute("SELECT id FROM tracks WHERE tracks.outdoor = 1").fetchall()
            for track in outdoor_tracks:
                list_of_ids.append(track[0])

            id_string = ', '.join(map(str, list_of_ids))

            event_track_id = cur.execute(f"""SELECT track_id
                                         FROM events WHERE track_id IN ({id_string})
                                         ORDER BY date ASC""").fetchone()

            outdoor_track = cur.execute("SELECT * FROM tracks WHERE tracks.id = :track_id",
                                        {"track_id": event_track_id[0]}).fetchone()

            con.close()

            return Track(*outdoor_track)

        else:
            con = sqlite3.connect("iceskatingapp.db")
            cur = con.cursor()

            track_id = cur.execute("""SELECT track_id
                                   FROM events
                                   ORDER BY date ASC""").fetchone()
            track = cur.execute("SELECT * FROM tracks WHERE tracks.id = :track_id", {"track_id": track_id[0]}).fetchone()

            con.close()

            return Track(*track)

    # Which track had the latest event? -> Track
    # Which track had the latetstoutdoor event? -> Track
    def get_latest_event(self, outdoor_only: bool = False) -> Track:
        if outdoor_only:
            con = sqlite3.connect("iceskatingapp.db")
            cur = con.cursor()

            list_of_ids = []

            outdoor_tracks = cur.execute("SELECT id FROM tracks WHERE tracks.outdoor = 1").fetchall()
            for track in outdoor_tracks:
                list_of_ids.append(track[0])

            id_string = ', '.join(map(str, list_of_ids))

            event_track_id = cur.execute(f"""SELECT track_id
                                         FROM events WHERE track_id IN ({id_string})
                                         ORDER BY date DESC""").fetchone()

            outdoor_track = cur.execute("SELECT * FROM tracks WHERE tracks.id = :track_id",
                                        {"track_id": event_track_id[0]}).fetchone()

            con.close()

            return Track(*outdoor_track)

        else:
            con = sqlite3.connect("iceskatingapp.db")
            cur = con.cursor()

            track_id = cur.execute("""SELECT track_id
                                   FROM events
                                   ORDER BY date DESC""").fetchone()
            track = cur.execute("SELECT * FROM tracks WHERE tracks.id = :track_id", {"track_id": track_id[0]}).fetchone()

            con.close()

            return Track(*track)

    # Which skaters have raced track Z between period X and Y? -> tuple[Skater, ...]
    # Based on given parameter `to_csv = True` should generate CSV file as  `Skaters on Track Z between X and Y.csv`
    # example: `Skaters on Track Kometa between 2021-03-01 and 2021-06-01.csv`
    # date input always in format: YYYY-MM-DD
    # otherwise it should just return the value as tuple(Skater, ...)
    # CSV example (this are also the headers):
    #   id, first_name, last_name, nationality, gender, date_of_birth
    def get_skaters_that_skated_track_between(self, track: Track, start: datetime,
                                              end: datetime, to_csv: bool = False) -> tuple[Skater, ...]:
        con = sqlite3.connect("iceskatingapp.db")
        cur = con.cursor()

        skater_list = []

        events = cur.execute("select id FROM events WHERE date BETWEEN :start AND :end AND track_id = :track_id",
                             {"start": start.date(), "end": end.date(), "track_id": track.id}).fetchall()

        skater_id_set = set()

        for event in events:
            skaters_ids = cur.execute("SELECT skater_id FROM event_skaters WHERE event_id = :event_id", {"event_id": event[0]})
            for skater_id in skaters_ids:
                skater_id_set.add(skater_id[0])

        id_string = str(skater_id_set).strip("{}")

        skaters = cur.execute(f"SELECT * FROM skaters WHERE id IN ({id_string})").fetchall()

        con.close()

        if to_csv:
            with open(f"Skaters on Track {track.name} between {start.date()} and {end.date()}.csv", "w", newline='') as csv_file:
                writer = csv.writer(csv_file)
                field = ["id", "first_name", "last_name", "nationality", "gender", "date_of_birth"]
                writer.writerow(field)
                for skater in skaters:
                    writer.writerow(skater)

        else:
            for skater in skaters:
                skater_list.append(Skater(*skater))

            return tuple(skater_list)

    # Which tracks are located in country X? ->tuple[Track, ...]
    # Based on given parameter `to_csv = True` should generate CSV file as  `Tracks in country X.csv`
    # example: `Tracks in Country USA.csv`
    # otherwise it should just return the value as tuple(Track, ...)
    # CSV example (this are also the headers):
    #   id, name, city, country, outdoor, altitude
    def get_tracks_in_country(self, country: str, to_csv: bool = False) -> tuple[Track, ...]:
        con = sqlite3.connect("iceskatingapp.db")
        cur = con.cursor()

        tracks_list = []

        tracks = cur.execute("SELECT * FROM tracks WHERE country = :country", {"country": country}).fetchall()

        con.close()

        if to_csv:
            with open(f"Tracks in country {country}.csv", "w", newline='') as csv_file:
                writer = csv.writer(csv_file)
                field = ["id", "name", "city", "country", "outdoor", "altitude"]
                writer.writerow(field)
                for track in tracks:
                    writer.writerow(track)

        else:
            for track in tracks:
                tracks_list.append(Track(*track))

            return tuple(tracks_list)

    # Which skaters have nationality X? -> tuple[Skater, ...]
    # Based on given parameter `to_csv = True` should generate CSV file as  `Skaters with nationality X.csv`
    # example: `Skaters with nationality GER.csv`
    # otherwise it should just return the value as tuple(Skater, ...)
    # CSV example (this are also the headers):
    #   id, first_name, last_name, nationality, gender, date_of_birth
    def get_skaters_with_nationality(self, nationality: str, to_csv: bool = False) -> tuple[Skater, ...]:
        con = sqlite3.connect("iceskatingapp.db")
        cur = con.cursor()

        skaters_list = []

        skaters = cur.execute("SELECT * FROM skaters WHERE nationality = :nationality", {"nationality": nationality}).fetchall()

        con.close()

        if to_csv:
            with open(f"Skaters with nationality {nationality}.csv", "w", newline='') as csv_file:
                writer = csv.writer(csv_file)
                field = ["id", "first_name", "last_name", "nationality", "gender", "date_of_birth"]
                writer.writerow(field)
                for skater in skaters:
                    writer.writerow(skater)
        else:
            for skater in skaters:
                skaters_list.append(Skater(*skater))

            return tuple(skaters_list)
