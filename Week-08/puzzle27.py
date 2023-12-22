import string

alphabet = string.ascii_uppercase

def decrypt():
    encrypted_message = "CDEFGHIJKLMNOPQRSTUVWXYZA"
    for key in range(1,27):

        
        decrypted_message = ""

        for c in encrypted_message:

            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position - key) % 26
                new_character = alphabet[new_position]
                decrypted_message += new_character
            else:
                decrypted_message += c
            
            key += 4

        print(decrypted_message)

decrypt()