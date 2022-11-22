def sum(str):
    total = 0
    get_input = str.split("-")
    for value in get_input:
        total += float(value)
    return total


num = input("Enter number as a string: ")

print("sum is: ", sum(num))
