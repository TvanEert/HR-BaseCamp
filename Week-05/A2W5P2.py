def calculate_fare(distance):
    distance = float(distance) * 1000
    fare_times = float(distance) / 140 + 0.5
    fare = 4 + round(fare_times) * 0.25
    return fare


if __name__ == "__main__":
    distance = input("Disctance")
    fare = calculate_fare(distance)
    print(f"{fare:.2f}")