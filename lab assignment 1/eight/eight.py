def make_upper(str):
    new_str = ''
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            ascii_value = ord(char)-32
            new_str += chr(ascii_value)
        else:
            new_str += char
    return new_str

def make_lower(str):
    new_str = ''
    for char in str:
        if ord(char) > 64 and ord(char) < 91:
            ascii_value = ord(char)+32
            new_str += chr(ascii_value)
        else:
            new_str += char
    return new_str

def make_capital(str):
    new_string = ''
    for index, char in enumerate(str):
        if str[index-1] == ' ':
            new_string += make_upper(char)
        else:
            if index == 0:
                new_string = make_upper(char)
            else:
                new_string += make_lower(char)
    return new_string