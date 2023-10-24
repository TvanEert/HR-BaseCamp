def is_integer(text):
    integer = False
    if text.isdigit():
        integer = True
    elif text[0] == "+" or text[0] == "-":
        if text[1:].isdigit():
            integer = True
    
    return integer
