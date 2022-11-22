s = "Programming Hero is the best"


def word_reverse(s):
    sep_words = s.split(" ")
    new_str = ''
    for word in sep_words:
        for char in word[::-1]:
            new_str += char
        new_str += " "
    return new_str


print(word_reverse(s))
