""" Random examples."""

import random
"""
# Selects a random floating-pint number between 0 and 1 and stores it in a
# variable called "num". If you want to obtain a larger number, you can 
# multiply it as shown below:
num = random.random()
num = num * 100
print(num)

num = random.randint(0,9)
# Select a random whole number between 0 and 9 (inclusive).

num1 = random.randint(0,1000)
num2 = random.randint(0,1000)
newrand = num1/num2
print(newrand)
# Create s random floating-point number by creating two random integers
# within two large ranges (in this case between 0 and 1000) and dividing
# one by the other.

num = random.randrange(0,100,5)
# Picks a random number between the numbers 0 and 100(inclusive) in steps of
# five, i.e. it will only pick from 0,5,10,15,20,etc.

colour = random.choice(["red", "black", "green"])
# Picks a random value from the options "red", "black" or "green" and stores
# it as the variable "colour". Remember: strings need to include speech
# marks but numeric data does not.

# 052
# Display a random integer between 1 and 100 inclusive.

import random
num = random.randint(1,100)
print(num)

# 053
# Display a random fruit from a list of five fruits.

import random
fruit = random.choice(['apple', 'orange', 'grape', 'bannana', 'strawberry'])
print(fruit)

# 054
# Randomly choose either heads or tails ("h" or "t"). Ask the user to make
# their choice. If their choice is the same as the randomly selected value,
# display the message "You win", otherwise display "Bad luck". At the end,
# tell the user if the computer selected heads or tails.

import random
coin = random.choice(["h", "t"])
guess = input("Enter (h)eads or (t)ails: ")
if guess == coin:
    print("You win")
else:
    print("Bad luck")
if coin == "h":
    print("It was heads")
else:
    print("It was tails")

# 055
# Randomly choose a number between 1 and 5. Ask the user to pick a number. 
# If they guess correctly, display the message "Well done", otherwise tell
# them if they are too high or too low and them to pick a second number. If
# they guess correctly on their second guess, display "Correct", otherwise
# display "You lose".

import random
num = random.randint(1,5)
guess = int(input("Enter a number: "))
if guess == num:
    print("Well done")
elif guess > num:
    print("Too high")
    guess = int(input("Guess again: "))
    if guess == num:
        print("Correct")
    else:
        print("You lose")
elif guess < num:
    print("Too low")
    guess = int(input("Guess again: "))
    if guess == num:
        print("Correct")
    else:
        print("You lose")
"""
# 056
# Randomly pick a whole number between 1 and 10. Ask the user to enter a 
# number and keep entering numbers until they enter the number that was
# randomly picked

import random
num = random.randint(1, 10)
correct = False
while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True

# 057

