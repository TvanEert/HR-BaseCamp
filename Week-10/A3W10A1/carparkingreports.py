import csv
import json

def main():
    running = True

    while running:
        print("\n[P] Report all parked cars during a parking period for a specific parking machine\n" +
              "[F] Report total collected parking fee during a parking period for all parking machines\n" +
              "[Q] Quit program\n\n")
        operation = input(": ")
        if operation.lower() == "q":
            running = False
        elif operation.lower() == "p":
            pass
        elif operation.lower() == "f":
            pass
        else:
            print("invalid input")

if __name__ == '__main__':
    main()