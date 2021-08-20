"""Flip a coin game. True or False?"""

import random
import string

def flipCoin():
    return random.choice([True, False])

for i in range(0,5):
    print(flipCoin())
print()

###### flip a coin experiment using random.random()

import random
import string

def flipCoin():
    f = random.random()
    return True if f<0.5 else False

for i in range(0,5):
    print(flipCoin())
print()
######
