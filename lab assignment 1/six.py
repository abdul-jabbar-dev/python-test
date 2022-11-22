def clean_string(text):
    result = ''
    for char in text:
        if char.isalpha():
            result += char
    return result


s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)
