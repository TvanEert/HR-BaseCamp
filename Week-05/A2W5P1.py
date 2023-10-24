import random


def arithmetic_operation(arithemic_type):
    correct = 0
    incorrect = 0
    for _ in range(10):
        random_number1 = random.randint(1, 100)
        random_number2 = random.randint(1, 100)
        if arithmetic_type == "summation":
            answer = int(input(f"{random_number1} + {random_number2}: "))
            if answer == random_number1 + random_number2:
                correct += 1
            else:
                incorrect += 1
        elif arithmetic_type == "multiplication":
            answer = int(input(f"{random_number1} * {random_number2}: "))
            if answer == random_number1 * random_number2:
                correct += 1
            else:
                incorrect += 1
        elif arithmetic_type == "subtraction":
            answer = int(input(f"{random_number1} - {random_number2}: "))
            if answer == random_number1 - random_number2:
                correct += 1
            else:
                incorrect += 1
    return correct, incorrect


if __name__ == "__main__":
    arithmetic_type = input("Arithmetic type: ")
    correct, incorrect = arithmetic_operation(arithmetic_type)
    print(f'You had {correct} correct and {incorrect} incorrect answers in "{arithmetic_type}"')