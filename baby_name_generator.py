import random, string

letter_1 = input('Enter "v" for vowel, "c" for consonants, "l" for any letter:  ')
letter_2 = input('Enter "v" for vowel, "c" for consonants, "l" for any letter:  ')
letter_3 = input('Enter "v" for vowel, "c" for consonants, "l" for any letter:  ')
letter_4 = input('Enter "v" for vowel, "c" for consonants, "l" for any letter:  ')
letter_5 = input('Enter "v" for vowel, "c" for consonants, "l" for any letter:  ')



def baby_name():
    vowel = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    letters = random.choice(string.ascii_lowercase)

    if letter_1 == 'c':
        letter1 = random.choice(consonants)
    elif letter_1 == 'v':
        letter1 = random.choice(vowel)
    elif letter_1 == 'l':
        letter1 = random.choice(letters)
    else:
        letter1 = letter_1

    if letter_2 == 'c':
        letter2 = random.choice(consonants)
    elif letter_2 == 'v':
        letter2 = random.choice(vowel)
    elif letter_2 == 'l':
        letter2 = random.choice(letters)
    else:
        letter2 = letter_2
    if letter_3 == 'c':
        letter3 = random.choice(consonants)
    elif letter_3 == 'v':
        letter3 = random.choice(vowel)
    elif letter_3 == 'l':
        letter3 = random.choice(letters)
    else:
        letter3 = letter_3

    if letter_4 == 'c':
        letter4 = random.choice(consonants)
    elif letter_4 == 'v':
        letter4 = random.choice(vowel)
    elif letter_4 == 'l':
        letter4 = random.choice(letters)
    else:
        letter4 = letter_4

    if letter_5 == 'c':
        letter5 = random.choice(consonants)
    elif letter_5 == 'v':
        letter5 = random.choice(vowel)
    elif letter_5 == 'l':
        letter5 = random.choice(letters)
    else:
        letter5 = letter_5
    name = letter1 + letter2 + letter3 + letter4 + letter5
    return name


for i in range(30):
    print(baby_name())

