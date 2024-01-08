import os
from datetime import datetime


class CarParkingLogger():
    def __init__(self, id: str):
        self.id = id
        carpark_file = open(os.path.join(os.getcwd(), "carparklog.txt"), "a")
        carpark_file.close()

    def restore_state(self, machine_id: str):
        restored_cars_parked = {}

        with open(os.path.join(os.getcwd(), "carparklog.txt"), 'r') as carkpark_file:
            lines = carkpark_file.readlines()
            for line in lines:
                split_line = line.strip().split(";")
                check_in_time = datetime.strptime(split_line[0], '%d-%m-%Y %H:%M:%S')
                machine_log_id = split_line[1].replace("cpm_name=", "")
                license_plate = split_line[2].replace("license_plate=", "")
                action = split_line[3].replace("action=", "")
                if machine_log_id == machine_id:
                    if action == "check-in":
                        restored_cars_parked[license_plate] = ParkedCar(license_plate, check_in_time)
                    elif action == "check-out":
                        restored_cars_parked.pop(license_plate)

        return restored_cars_parked

    def get_total_car_fee(self, license_plate: str):
        fee = 0

        with open(os.path.join(os.getcwd(), "carparklog.txt"), 'r') as carkpark_file:
            lines = carkpark_file.readlines()
            for line in lines:
                split_line = line.strip().split(";")
                license_plate_log = split_line[2].replace("license_plate=", "")
                action = split_line[3].replace("action=", "")
                if license_plate_log == license_plate and action == "check-out":
                    fee += float(split_line[4].replace("parking_fee=", ""))

        total_fee = fee
        return total_fee

    def get_machine_fee_by_day(self, car_parking_machine_id: str, search_date: str):
        fee = 0

        with open(os.path.join(os.getcwd(), "carparklog.txt"), 'r') as carkpark_file:
            lines = carkpark_file.readlines()
            for line in lines:
                split_line = line.strip().split(";")
                date = split_line[0].split(" ")[0]
                if date == search_date:
                    car_parking_machine_id_log = split_line[1].replace("cpm_name=", "")
                    action = split_line[3].replace("action=", "")
                    if car_parking_machine_id == car_parking_machine_id_log and action == "check-out":
                        fee += float(split_line[4].replace("parking_fee=", ""))

        total_fee = fee
        return round(total_fee, 2)

    def log_check_in(self, check_in: datetime, carpark_id: str, lisence: str):
        if self.id == carpark_id:
            check_in = datetime.strftime(check_in, '%d-%m-%Y %H:%M:%S')
            carpark_file = open(os.path.join(os.getcwd(), "carparklog.txt"), "a")
            carpark_file.write(f"{check_in};cpm_name={carpark_id};license_plate={lisence};action=check-in\n")
            carpark_file.close()
        else:
            print("id mismatch")

    def log_check_out(self, check_in: datetime, carpark_id: str, lisence: str, parking_fee: float):
        if self.id == carpark_id:
            check_in = datetime.strftime(check_in, '%d-%m-%Y %H:%M:%S')
            carpark_file = open(os.path.join(os.getcwd(), "carparklog.txt"), "a")
            carpark_file.write(f"{check_in};cpm_name={carpark_id};license_plate={lisence};"
                               f"action=check-out;parking_fee={parking_fee}\n")
            carpark_file.close()
        else:
            print("id mismatch")


class CarParkingMachine():
    def __init__(self, id: str, capacity=10, hourly_rate=2.50, parked_cars=None):
        if parked_cars is None:
            parked_cars = {}
        self.id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars
        self.logger = CarParkingLogger(self.id)
        self.parked_cars = self.logger.restore_state(self.id)

    def check_in(self, license_plate: str, check_in=None):
        if check_in is None:
            check_in = datetime.now().replace(microsecond=0)
        else:
            check_in = check_in.replace(microsecond=0)
        if len(self.parked_cars) < self.capacity:
            car = ParkedCar(license_plate, check_in)
            self.parked_cars[license_plate] = car
            self.logger.log_check_in(check_in, self.id, license_plate)
            return True
        else:
            return False

    def check_out(self, license_plate: str):
        fee = self.get_parking_fee(license_plate)
        self.logger.log_check_out(datetime.now(), self.id, license_plate, fee)
        del self.parked_cars[license_plate]
        return fee

    def get_parking_fee(self, license_plate: str):
        time_difference = datetime.now() - self.parked_cars[license_plate].check_in
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
        self.check_in = check_in


def main():
    carp_park = CarParkingMachine("Machine1")

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