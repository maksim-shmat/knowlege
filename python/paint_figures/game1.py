""" How it is number?"""

# pip3 install pyautogui

import random
import pyautogui

guessesTaken = 0

print('Hello! What is your name, pidrila?')
myName = input()
number = random.randint(1, 20)
print('Ok, pidrila' + myName + ', how is a number from 1 to 20?')

for guessesTaken in range(6):
    print('Tell me number.')
   # pyautogui.typewrite("Tell me number.")
   # pyautogui.typewrite("\nWrite it blockhead.", interval=0.5)
    guess = input()
    guess = int(guess)

    if guess < number:
       print("Your number is many less, how your pinus.")
    
    if guess > number:
        print("Your number is many great, how your mommy ass.")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Exelent, ' + myName + '! You get it for ' + guessesTaken + ' ones!')
if guess != number:
    number = str(number)
    print('Oh oh oh, imbecilus, that number' + number + '.')
