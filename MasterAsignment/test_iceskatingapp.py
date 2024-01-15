from skater import Skater
from event import Event
from track import Track
from datetime import datetime


# Test to check if the age of a skater is correct based on the date_of_birth
def test_age_of_skater():
    skater = Skater(32, "Tim", "van Eert", "NL", "M", datetime(2002, 8, 7))

    assert 21 == skater.get_age()


# Test to check if the amount of events for a specific skater is returned correctly
def test_amount_of_events_of_skater():
    skater = Skater(32, "Tim", "van Eert", "NL", "M", datetime(2002, 8, 7))

    assert 2 == len(skater.get_events())


# Test to check if the amount of events for a specific track is returned correctly
def test_amount_of_events_of_track():
    track = Track(29, "Hamar Olympic Hall", "Hamar", "NOR", False, 123)

    assert 12 == len(track.get_events())


# Test to check if the returned date matches the specified format for that event date
def test_event_date_conversion():
    event = Event(1, "Essent ISU World Cup - 1500m Men Division A", 29, "2003-11-08", 1200, 107.38, 4, "Erben Wennemars", "M")

    assert "08-11-2003" == event.convert_date("%d-%m-%Y")


# Test to check if the duration is converted from 1H19 to the specified format
def test_event_duration_conversion():
    event = Event(1, "Essent ISU World Cup - 1500m Men Division A", 29, "2003-11-08", 1200, 107.38, 4, "Erben Wennemars", "M")

    assert "01:47" in event.convert_duration("%M:%S")
    assert "1" in event.convert_duration("%M")
    assert "107" in event.convert_duration("%S")


# Test to check the amount of skaters on a specified event
def test_amount_of_skaters_on_event():
    event = Event(1, "Essent ISU World Cup - 1500m Men Division A", 29, "2003-11-08", 1200, 107.38, 4, "Erben Wennemars", "M")

    assert 56 == len(event.get_skaters())


# Test to validate if the given track of a specified event is correct
def test_track_on_event():
    event = Event(1, "Essent ISU World Cup - 1500m Men Division A", 29, "2003-11-08", 1200, 107.38, 4, "Erben Wennemars", "M")
    track = Track(29, "Hamar Olympic Hall", "Hamar", "NOR", False, 123)

    assert event.get_track().__dict__ == track.__dict__


test_age_of_skater()
test_amount_of_events_of_skater()
test_amount_of_events_of_track()
test_event_date_conversion()
test_event_duration_conversion()
test_amount_of_skaters_on_event()
test_track_on_event()