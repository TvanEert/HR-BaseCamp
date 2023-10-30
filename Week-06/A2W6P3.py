def is_valid_password(password):
    lowercase = set("abcdefghijklmnopqrstuvwxyz")
    uppercase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digits = set("0123456789")
    symbols = set("*@!?")
    admissible_chars = lowercase | uppercase | digits | symbols

    password_set = set(password)

    if not (8 <= len(password) <= 20):
        return False

    if not password_set.issubset(admissible_chars):
        return False

    if (password_set & lowercase) and (password_set & uppercase) and \
       (password_set & digits) and (password_set & symbols):
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