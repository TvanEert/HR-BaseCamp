plate = input("plate: ")

digits = 0;

for x in plate:
    if(x.isdigit()):
        digits += 1

if(digits >=2 and digits <= 4 and len(plate) == 8):
    print("valid")
else:
    print("invalid")