years = int(input("Human Years:"))

if(years >= 2):
    years = years - 2
    dogYears = (2 * 10.5) + years * 4
    print("Dog years: ", dogYears)
elif(years < 2):
    dogYears = (years * 10.5)
    print("Dog years: ", dogYears)
elif years < 0:
    print("Only positive numbers are allowed")