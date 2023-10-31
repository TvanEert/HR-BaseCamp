number = 2
times = 1
answer = 1

opperation = "add"

while number < 500:
    if opperation == "add":
        for _ in range(times):
            print("+", number)
            answer += number
            number += 1
            if number == 501:
                break
            print(answer)
        times += 1
        opperation = "sub"
    elif opperation == "sub":
        for _ in range(times):
            print("-", number)
            answer -= number
            number += 1
            if number == 501:
                break
            print(answer)
        times += 1
        opperation = "add"

print(answer)