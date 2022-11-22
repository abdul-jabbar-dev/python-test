d = {'!': 1, '@': 2, '#': 3, '$': 4, '%': 5, '^': 6}


def create_list(dec):
    output = []
    for i, item in enumerate(d):
        output.append(item)
        output.append(d[item])

    return output

result = create_list(d)
print(result)
