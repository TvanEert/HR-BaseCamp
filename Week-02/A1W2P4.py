#a=5, b=6, c=5
import re

number = input("")

numbers = re.findall(r'\d+', number)

if(numbers[0] == numbers[1] == numbers[2]):
    print("Equilateral Triangle")
elif(numbers[0] != numbers[1] != numbers[2]):
    print("Scalene Triangle")
else:
    print("Isosceles triangle")