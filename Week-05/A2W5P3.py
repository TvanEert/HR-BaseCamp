def check_triangle(a, b, c):
    return a < b + c and b < a + c and c < a + b


if __name__ == '__main__':
    triangle_side1 = float(input("Enter the length of side A: "))
    triangle_side2 = float(input("Enter the length of side B: "))
    triangle_side3 = float(input("Enter the length of side C: "))

    if check_triangle(triangle_side1, triangle_side2, triangle_side3):
        print("possible")
    else:
        print("impossible")