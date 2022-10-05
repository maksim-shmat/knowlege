"""Work with random.shuffle()."""

import random
import itertools

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')

def new_deck():
    return [
            '{:>2}{}'.format(*c)
            for c in itertools.product(
                itertools.chain(range(2, 11), FACE_CARDS),
                SUITS,
            )
    ]


def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print(j, end=' ')
        print()

deck = new_deck()
print('Initial deck:')
show_deck(deck)

random.shuffle(deck)
print('\nShuffled deck:')
show_deck(deck)

hands = [[], [], [], []]

for i in range(5):
    for h in hands:
        h.append(deck.pop())

print('\nHands:')
for n, h in enumerate(hands):
    print('{}:'.format(n + 1), end=' ')
    for c in h:
        print(c, end=' ')
    print()

print('\nRemaining deck:')
show_deck(deck)

'''RESULTS:
Initial deck:
 2H  2D  2C  2S  3H  3D  3C  3S  4H  4D  4C  4S  5H 
 5D  5C  5S  6H  6D  6C  6S  7H  7D  7C  7S  8H  8D 
 8C  8S  9H  9D  9C  9S 10H 10D 10C 10S  JH  JD  JC 
 JS  QH  QD  QC  QS  KH  KD  KC  KS  AH  AD  AC  AS 

Shuffled deck:
 4S  9H  AD  2S  4D  2H  QC  5C  QH  JH 10H  JC  QD 
 QS  6H  KH  5H 10S  3C  2D  8C  9C  8D  KD  6D  5D 
 KS  4H  9D  5S  6S 10D  8S  8H  4C  7C  JS  KC  3S 
 7D 10C  AH  9S  AC  3D  7S  AS  6C  2C  JD  3H  7H 

Hands:
1:  7H  6C  AC  7D  7C 
2:  3H  AS  9S  3S  4C 
3:  JD  7S  AH  KC  8H 
4:  2C  3D 10C  JS  8S 

Remaining deck:
 4S  9H  AD  2S  4D  2H  QC  5C  QH  JH 10H  JC  QD 
 QS  6H  KH  5H 10S  3C  2D  8C  9C  8D  KD  6D  5D 
 KS  4H  9D  5S  6S 10D 
'''
