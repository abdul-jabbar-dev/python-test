l = ["This", "is", "very", "fantastic"]


def create_string(arr):
    new_arr = ''
    for word in arr:
        new_arr = new_arr + " " + word

    return new_arr[1:]


print(create_string(l))
