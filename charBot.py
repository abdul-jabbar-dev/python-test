import random
# input


def listening():
    return input("Say something: ")

# process


greeting_word = ['hi', 'hello', 'yo']
by_word = ['bye', 'tata', 'by']


def thinking(input_massage):
    massage_pice = input_massage.lower().split(' ')
    for pice in massage_pice:
        if pice in greeting_word:
            output(f'{random.choice(greeting_word)} man')
            return
        elif pice in by_word:
            output(f'Ok {random.choice(by_word)} ! see you')
            return
# output


def output(msg):
    print(msg)


while True:
    thinking(listening())
