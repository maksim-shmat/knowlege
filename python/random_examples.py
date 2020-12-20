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
"""
# 052
# Display a random integer between 1 and 100 inclusive.

import random
num = random.randint(1,100)
print(num)

# 053

