import random

number = random.randint(1, 11)
count = 1

name = input('How may i call you?')
print('Hi', name)
choice = input("shall we play a game [Y/N]")
if choice == 'y':
    guess = int(input('I have a number taken between 1 & 100... Guess it.!'))

    while guess != number:
        count += 1
        if guess > number:
            print('Guess again by decreasing ur value...')
        elif guess < number:
            print('Guess again by increasing ur value')
        guess = int(input())

    print('your guess', guess, "is right at", count, 'th time')

else:
    print("Bye bye", name, 'See you again')
