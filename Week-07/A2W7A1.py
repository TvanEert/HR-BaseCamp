encoded_values = []
decoded_values = []
hashkey_values = {}
reversed_hashkey_values = {}


# create a function that given the input string converts it to the encoded equivalent based on the provided
# or already set key/hashmap
# make sure to only convert values that are in the key, if the value is not present, use its own value
def encode_string(data: str, key: str = None) -> str:
    encoded_string = ""
    for letter in data:
        if letter in hashkey_values:
            encoded_string += str(hashkey_values[letter])
        else:
            encoded_string += letter

    encoded_values.append(encoded_string)

    return encoded_string


# create a function that given the input string converts it to the decoded equivalent based on the provided
# or already set key/hashmap
# make sure to only decode values that are in the key, if the value is not present, use its own value
def decode_string(data: str, key: str = None) -> str:
    decoded_string = ""
    for letter in data:
        if letter in reversed_hashkey_values:
            decoded_string += str(reversed_hashkey_values[letter])
        else:
            decoded_string += letter

    decoded_values.append(decoded_string)

    return decoded_string


# create a function that given a list of inputs converts the complete list to the encoded
# equivalent based on the key/hashmap
# you can use the already created encode function when looping through the list
# tip! make use of the map function within python with a lambda to call the internal function with all elements
# as a return value, you should return a list with the converted values
def encode_list(data: list, key: str = None) -> list:
    encoded_values_list = []

    for word in data:
        encoded_string = ""
        for letter in word:
            if letter in hashkey_values:
                encoded_string += str(hashkey_values[letter])
            else:
                encoded_string += letter

        encoded_values.append(encoded_string)
        encoded_values_list.append(encoded_string)

    return encoded_values_list


# create a function that given a list of inputs converts the complete list to the encoded
# equivalent based on the key/hashmap
# you can use the already created decode function when looping through the list
# tip! make use of the map function within python with a lambda to call the internal function with all elements
# as a return value, you should return a list with the converted values
def decode_list(data: list, key: str = None) -> list:
    decoded_values_list = []

    for word in data:
        decoded_string = ""
        for letter in word:
            if letter in reversed_hashkey_values:
                decoded_string += str(reversed_hashkey_values[letter])
            else:
                decoded_string += letter

        decoded_values.append(decoded_string)
        decoded_values_list.append(decoded_string)

    return decoded_values_list


# create a function that given a encoded value, decoded value and a key (optional) checks if the values are correct
# the return value should be a boolean value (True if values match, False if they don't match)
def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    if encoded == encode_string(decoded):
        return True
    else:
        return False


# give the option to input a hashvalue to be used/converted to a key
# each oneven character is the Key of the Dict, each even character is the coresponding Value
# you should validate if the given input is an even input, otherwise show the error: Invalid hashvalue input
# example: a@b.c>d#eA will become: {'a': '@', 'b': '.', 'c': '>', 'd', '#', 'e': 'A'}
def set_dict_key(key: str) -> None:
    for index in range(0, len(key), 2):
        hashkey_values[key[index]] = key[index + 1]

    for key, value in hashkey_values.items():
        reversed_hashkey_values[value] = key


# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [E] Encode value to hashed value
# [D] Decode hashed value to normal value
# [P] Print all encoded/decoded values
# [V] Validate 2 values against eachother
# [Q] Quit program
def main(hash_key):
    set_dict_key(hash_key)

    running = True

    print("[E] Encode value to hashed value")
    print("[D] Decode hashed value to normal value")
    print("[P] Print all encoded/decoded values")
    print("[V] Validate 2 values against eachother")
    print("[Q] Quit program")

    while running:
        operation = input("Operation: ").lower()

        if operation == "e":
            encode_value = input("Value: ")
            if "," in encode_value:
                encode_value_list = encode_value.split(", ")
                encode_list(encode_value_list)
            else:
                encode_string(encode_value)
        elif operation == "d":
            decode_value = input("Value: ")
            if "," in decode_value:
                decode_value_list = decode_value.split(", ")
                decode_list(decode_value_list)
            else:
                decode_string(decode_value)
        elif operation == "p":
            print("encoded values: ")
            for value in encoded_values:
                print(value)
            print("decoded values: ")
            for value in decoded_values:
                print(value)
        elif operation == "v":
            encode_value = input("Encoded value: ")
            decode_value = input("Decoded value: ")
            validated = validate_values(encode_value, decode_value)
            if validated:
                print("True")
            else:
                print("False")
        elif operation == "q":
            running = False


# Create a unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
if __name__ == "__main__":
    key = input("key: ")
    if len(key) % 2 == 0:
        main(key)
    else:
        print("Invalid hashvalue input")