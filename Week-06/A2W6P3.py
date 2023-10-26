def is_valid_password(password):
    lowercase = set("abcdefghijklmnopqrstuvwxyz")
    uppercase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digits = set("0123456789")
    symbols = set("*@!?")

    password = set(password)

    for char in password:
        if char in lowercase:
            pass
        elif char in uppercase:
            pass
        elif char in digits:
            pass
        elif char not in symbols:
            return False

    if 8 <= len(password) <= 20:
        return False

    if (password & lowercase) and (password & uppercase) and (password & digits) and (password & symbols):
        return True

    else:
        return False


if __name__ == "__main__":
    attempts = 3

    while attempts > 0:
        password = input("")
        if is_valid_password(password):
            print("Password is valid")
            break
        else:
            print("Password is invalid")
            attempts -= 1

    if attempts == 0:
        print("You used up your attempts. ")