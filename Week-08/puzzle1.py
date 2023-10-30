sum = 0 
counter = 0
number = 1

while number <= 100:
    counter += 1
    if not "5" in str(counter) and not "3" in str(counter):
        sum += counter
        number += 1
        print(number)
        print(counter)

print(sum)