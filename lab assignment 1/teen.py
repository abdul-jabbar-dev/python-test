a = ['oh', 'Emelia', 'to']
s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

def create_new_string():
    output = ""
    braking = s.split(" ")
    temp = ''
    for value in a:
        for j, word in enumerate(braking):
            if (word.lower().startswith(value.lower())):
                temp = braking[j+1]
        output += temp
        output += " "
    with open("out.txt", 'w') as out:
        out.write(output[:-1])
    out.close()


create_new_string()
