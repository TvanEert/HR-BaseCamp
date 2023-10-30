dict_key_value = {}
encoded_values = []
decoded_values = []


# create a function that given the input string converts it to the encoded equivalent based on the provided or already set key/hashmap
# make sure to only convert values that are in the key, if the value is not present, use its own value
def encode_string(data: str, key: str = None) -> str:
    ...

# create a function that given the input string converts it to the decoded equivalent based on the provided or already set key/hashmap
# make sure to only decode values that are in the key, if the value is not present, use its own value
def decode_string(data: str, key: str = None) -> str:
    ...

# create a function that given a list of inputs converts the complete list to the encoded equivalent based on the key/hashmap
# you can use the already created encode function when looping through the list
# tip! make use of the map function within python with a lambda to call the internal function with all elements
# as a return value, you should return a list with the converted values
def encode_list(data: list, key: str = None) -> list:
    ...

# create a function that given a list of inputs converts the complete list to the encoded equivalent based on the key/hashmap
# you can use the already created decode function when looping through the list
# tip! make use of the map function within python with a lambda to call the internal function with all elements
# as a return value, you should return a list with the converted values
def decode_list(data: list, key: str = None) -> list:
    ...

# create a function that given a encoded value, decoded value and a key (optional) checks if the values are correct
# the return value should be a boolean value (True if values match, False if they don't match)
def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    ...

# give the option to input a hashvalue to be used/converted to a key
# each oneven character is the Key of the Dict, each even character is the coresponding Value
# you should validate if the given input is an even input, otherwise show the error: Invalid hashvalue input
# example: a@b.c>d#eA will become: {'a': '@', 'b': '.', 'c': '>', 'd', '#', 'e': 'A'}
def set_dict_key(key: str) -> None:
    ...

# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [E] Encode value to hashed value
# [D] Decode hashed value to normal value
# [P] Print all encoded/decoded values
# [V] Validate 2 values against eachother
# [Q] Quit program
def main():
    running = True

    print("\n [E] Encode value to hashed value\n",
          "[D] Decode hashed value to normal value\n",
          "[P] Print all encoded/decoded values\n",
          "[V] Validate 2 values against eachother\n",
          "[Q] Quit program\n")

    while running:
        operation = input("Operation: ").lower()

        if operation == "e":
            encode_string()
        elif operation == "d":
            decode_string()
        elif operation == "p":
            print(encoded_values)
            print(decoded_values)
        elif operation == "v":
            validate_values()
        elif operation == "q":
            running = False


# Create a unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
if __name__ == "__main__":
    main()