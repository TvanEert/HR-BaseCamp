from datetime import datetime


class CarParkingMachine():
    def __init__(self, capacity=10, hourly_rate=2.50, parked_cars={}):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars

    def check_in(self, license_plate: str, check_in=datetime.now()):
        if len(self.parked_cars) < self.capacity:
            car = ParkedCar(license_plate, check_in)
            self.parked_cars[license_plate] = car
            return True
        else:
            return False

    def check_out(self, license_plate: str):
        fee = self.get_parking_fee(license_plate)
        del self.parked_cars[license_plate]
        return fee

    def get_parking_fee(self, license_plate: str):
        time_difference = datetime.now() - self.parked_cars[license_plate].checked_in
        hours_elapsed = time_difference.total_seconds() / 3600
        round_hours = round(hours_elapsed + 0.5)

        if round_hours == 0:
            return self.hourly_rate
        elif round_hours >= 24:
            return 24 * self.hourly_rate
        else:
            return round_hours * self.hourly_rate


class ParkedCar():
    def __init__(self, license_plate: str, check_in: datetime):
        self.license_plate = license_plate
        self.checked_in = check_in


def main():
    carp_park = CarParkingMachine()
    running = True

    while running:
        print("\n[I] Check-in car by license plate\n" +
              "[O] Check-out car by license plate\n" +
              "[Q] Quit program\n\n")
        operation = input(": ")
        if operation.lower() == "q":
            running = False
        elif operation.lower() == "i":
            lisence = input("Input your lisence plate: ")
            if carp_park.check_in(lisence):
                print("License registered")
            elif not carp_park.check_in(lisence):
                print("Capacity reached")
        elif operation.lower() == "o":
            lisence = input("Input your lisence plate: ")
            fee = carp_park.check_out(lisence)
            print(f"Parking fee: {fee:.2f} EUR")
        else:
            print("invalid input")


if __name__ == "__main__":
    main()
