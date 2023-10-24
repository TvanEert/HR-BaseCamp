def unique_chars_set(text):
    return len(set(text))


def unique_chars_dict(text):
    char_dict = {}
    for letter in text:
        if letter not in char_dict:
            char_dict[letter] = len(char_dict) + 1
    return len(char_dict)


if __name__ == '__main__':
    text = input("text: ")
    unique_chars = unique_chars_dict(text)
    print(unique_chars)