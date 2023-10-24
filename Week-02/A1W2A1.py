"""from datetime import datetime, timedelta

date = input("Date:")

try:
    tomorrow = datetime.strptime(date, '%Y-%m-%d') + timedelta(1)

    print(tomorrow.strftime('%Y-%m-%d'))
except:
    print("Input format ERROR. Correct Format: YYYY-MM-DD")"""

date = input("Next Date:")

splitDate = date.split('-')

for x in range(len(splitDate)):
    splitDate[x] = int(splitDate[x])

if date[4] and date [7] == "-":
    if splitDate[1] < 8:
        if splitDate[1] == 2:
            if splitDate[2] <=27:
                splitDate[2] = splitDate[2] + 1
            else: 
                splitDate[2] = splitDate[2] = 1
                splitDate[1] = splitDate[1] + 1
        elif splitDate[1]%2 == 0:
            if splitDate[2] <= 29:
                splitDate[2] = splitDate[2] + 1
            else: 
                splitDate[2] = splitDate[2] = 1
                splitDate[1] = splitDate[1] + 1
        else:
            if splitDate[2] <= 30:
                splitDate[2] = splitDate[2] + 1
            else: 
                splitDate[2] = splitDate[2] = 1
                splitDate[1] = splitDate[1] + 1
    elif splitDate[1] <= 12:
        if splitDate[1] == 12 and splitDate[2] == 31:
            splitDate[2] = splitDate[2] = 1
            splitDate[1] = splitDate[1] = 1
            splitDate[0] = splitDate[0] + 1
        elif splitDate[1]%2 == 0:
            if splitDate[2] <= 30:
                splitDate[2] = splitDate[2] + 1
            else: 
                splitDate[2] = splitDate[2] = 1
                splitDate[1] = splitDate[1] + 1
        else:
            if splitDate[2] <= 29:
                splitDate[2] = splitDate[2] + 1
            else: 
                splitDate[2] = splitDate[2] = 1
                splitDate[1] = splitDate[1] + 1
    else:
        print("Input format ERROR. Correct Format: YYYY-MM-DD")
else:
    print("Input format ERROR. Correct Format: YYYY-MM-DD")

print(f"{splitDate[0]:04d}-{splitDate[1]:02d}-{splitDate[2]:02d}")