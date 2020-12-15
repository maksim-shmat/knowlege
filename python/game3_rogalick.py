""" Questions and choice."""

import random
import time

def displayIntro():
    print(""" You will be in the earth of chmudelz.
For you be two chars. Na odnom piki tochonie. Na drugom eto samoe. How is he?""")
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('How chare you choice? (push the button 1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You sitdown and ...')
    time.sleep(2)
    print('Your is nervious...')
    time.sleep(2)
    print('Your ass is sweat for your nervious...')
    time.sleep(2)
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)
    if chosenCave == str(friendlyCave):
        print('... this is the end!')
    else:
        print('... you serious?! Pidrila.')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('You want more? (yes or no)')
    playAgain = input()
