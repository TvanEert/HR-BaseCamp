from carparking import *
from datetime import datetime, timedelta

# Test for a normal check-in with correct result (True)
def test_check_in_capacity_normal():
    car_park = CarParkingMachine("south")

    if car_park.check_in("AA-123-A"): return True
    else: return False

# Test for a check-in with maximum capacity reached (False)
def test_check_in_capacity_reached():
    car_park = CarParkingMachine(2)
    car_park.check_in("AA-123-A")
    car_park.check_in("AA-123-B")

    if not car_park.check_in("AA-123-C"): return True
    else: return False

# Test for checking the correct parking fees
def test_parking_fee():
    # Assert that parking time 2h10m, gives correct parking fee
    # Assert that parking time 24h, gives correct parking fee
    # Assert that parking time 30h == 24h max, gives correct parking fee
    pass

# Test for validating check-out behaviour
def test_check_out():
    # Assert that {license_plate} is in parked_cars
    # Assert that correct parking fee is provided when checking-out {license_plate}
    # Aseert that {license_plate} is no longer in parked_cars
    pass

if __name__ == "__main__":
    if test_check_in_capacity_normal():
        print("test_check_in_capacity_normal code works as expected")
    else: print("test_check_in_capacity_normal code does not work as expected")

    if test_check_in_capacity_reached():
        print("test_check_in_capacity_reached code works as expected")
    else: print("test_check_in_capacity_reached code does not work as expected")
