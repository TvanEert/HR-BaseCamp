import math

numbers = '484676408044494469696698896400800469484964000800044040904046173237164000080000463783223873612110201123211464194249100200112343215221225100020001102030201104060401121242121123454321125686521522808225942060249100002000011022141220112102420121123456543'
highest_number = 0

def is_perfect_square(num):
    if num < 0:
        return False

    square_root = math.isqrt(num)

    if square_root * square_root == num:
        print("check square")
        return True
    else:
        return False

def is_palindrome(num):
    if num == num[::-1]:
        print("check pal")
        return True
    else:
        return False


for i in range(2,100):
    size = i
    for num in range(len(numbers) - size - 1):
        num = numbers[num:num + size]
        print(num)
        if is_perfect_square(int(num)):
            if is_palindrome(num):
                if int(num) > highest_number:
                    highest_number = int(num)

print(highest_number)