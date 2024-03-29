from skater import Skater
from event import Event
from track import Track
from datetime import datetime


# Test to check if the age of a skater is correct based on the date_of_birth
def test_age_of_skater():
    skater = Skater(32, "Tim", "van Eert", "NL", "M", datetime(2002, 8, 7))
    
    assert 21 == skater.get_age(datetime(2024, 11, 1))


# Test to check if the amount of events for a specific skater is returned correctly
def test_amount_of_events_of_skater():
    raise NotImplementedError()


# Test to check if the amount of events for a specific track is returned correctly
def test_amount_of_events_of_track():
    raise NotImplementedError()


# Test to check if the returned date matches the specified format for that event date
def test_event_date_conversion():
    raise NotImplementedError()


# Test to check if the duration is converted from 1H19 to the specified format
def test_event_duration_conversion():
    raise NotImplementedError()


# Test to check the amount of skaters on a specified event
def test_amount_of_skaters_on_event():
    raise NotImplementedError()


# Test to validate if the given track of a specified event is correct
def test_track_on_event():
    raise NotImplementedError()


test_age_of_skater()