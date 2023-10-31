import math

def is_perfect_square(num):
    if num < 0:
        return False

    square_root = math.isqrt(num)

    if square_root * square_root == num:
        return True
    else:
        return False
    
print(is_perfect_square(5))
