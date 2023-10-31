correct_sequence = []

def juggler_sequence(number):
    sequence = []
    print(number)
    sequence.append(number)

    while number != 1:
        if number % 2 == 0:
            number = int(pow(number, 0.5))
            sequence.append(number)
        else:
            number = int(pow(number, 1.5))
            sequence.append(number)
    
    return sequence


for i in range(2,100000):
    sequence = juggler_sequence(i)
    if len(sequence) == 51:
        correct_sequence = sequence
        break

print(correct_sequence, "correct")