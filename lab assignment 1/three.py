import pyjokes


def tell_some_jokes():
    print(" ")
    print(f"\"{pyjokes.get_joke('en')}\"")
    print(" ")


print("Hello i have a joke for you :-)")
tell_some_jokes()

yes_ans = ['yes', 'yah', 'ok', 'hmm','y']
no_ans = ['nothing', 'thx', 'never', 'no']
while True:
    ask = input("Would you listen another joke? : ")
    ask = ask.lower()
    if ask in yes_ans:
        tell_some_jokes()
    else:
        print("Thanks for listen boring jokes ")
        break
