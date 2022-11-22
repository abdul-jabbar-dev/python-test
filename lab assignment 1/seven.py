def replace_comma_with_space(text):
    new_string = ''
    for char in text:
        if char == ",":
            new_string += ' '
        else:
            new_string += char
    return new_string


s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)
