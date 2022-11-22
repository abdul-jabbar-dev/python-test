inp = 'x3b4U5i2'

def proses(inp):
    str = inp
    new_str = ''
    stored_char = ''
    for char in str:
        if char.isdigit():
            for i in range(int(char)):
                new_str += stored_char
        elif char.isalpha():
            stored_char = char
    return ''.join(sorted(new_str.lower()))


print(proses(inp))
