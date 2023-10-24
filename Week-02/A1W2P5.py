#Date: Month: 12, Day: 5
import re

date = input("Date: ")

date = re.findall(r'\d+', date)
print(date[0])
if date[0] == '12' and date[1] == '25':
    print("kerst")
else:
    print("geen")