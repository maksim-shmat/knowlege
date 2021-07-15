""" Hot or not game."""

import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSectetNum():
    """ Return string unique random integers, length their is NUM_DIGITS."""
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, sectetNum):
    """ Return string with notes 'Hot, 'or', 'Not'."""
    if guess == secretNum:
        return 'You win!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Hot')
        elif guess[i] in secretNum:
            clues.append('or')
    if len(clues) == 0:
        return 'Not'

    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    """ Return value True, if num - string only with integers, else False."""
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

print('I chose %s numeric integer, that you need check.' % (NUM_DIGITS))
print('I give you several notes...')
print('If I speak:    It value:')
print('  Hot    Is not one integer not checkd.')
print('  or     One integer check but it is not in their position.')
print('  Not    One integer and their position checkd.')

while True:
    secretNum = getSectetNum()
    print('So, I choose a number. You have %s turns, that be checkd it.' % (MAX_GUESS))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Turn %s: ' % (guessesTaken))
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print("Turns over. I choose number %s." % (secretNum))

    print("You want play again? (yes or not)")
    if not input().lower().startswith('y'):
        break
