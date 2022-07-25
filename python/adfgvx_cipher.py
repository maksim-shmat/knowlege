"""WW1 historical cipher implemented as a Python class."""

from random import shuffle, choice
from itertools import product, accumulate
from numpy import floor, sqrt

class ADFGVX:
    """ The WWI German ADFGVX cipher."""
    def __init__(self, spoly, k, alph='ADFGVX'):
        self.polybius = list(spoly.upper())
        self.pdim = int(floor(sqrt(len(self.polybius))))
        self.key = list(k.upper())
        self.keylen = len(self.key)
        self.alphabet = list(alph)
        pairs = [p[0] + p[1] for p in product(self.alphabet, self.alphabet)]
        self.encode = dict(zip(self.polybius, pairs))
        self.decode = dict((v, k) for (k, v) in self.encode.items())

    def encrypt(self, msg):
        """Encrypt with the ADFGVX cipher."""
        chars = list(''.join([self.encode[c] for c in msg.upper() if c in self.polybius]))
        colvecs = [(lett, chars[i:len(chars):self.keylen]) 
                for (i, lett) in enumerate(self.key)]
        colvecs.sort(key=lambda x: x[0])
        return ''.join([''.join(a[1]) for a in colvecs])

    def decrypt(self, cod):
        """Decrypt with the ADFGVX cipher. Does not depend on spacing of
        encoded text."""
        chars = [c for c in cod if c in self.alphabet]
        sortedkey = sorted(self.key)
        order = [self.key.index(ch) for ch in sortedkey]
        originalorder = [sortedkey.index(ch) for ch in self.key]
        base, extra = divmod(len(chars), self.keylen)
        # shuffled column lengths
        strides = [base + (1 if extra > i else 0) for i in order]
        # chuffled starts of columns
        starts = list(accumulate(strides[:-1], lambda x, y: x + y))
        # starting index
        starts = [0] + starts
        # shuffled ends of columns
        ends = [starts[i] + strides[i] for i in range(self.keylen)]
        # get reordered columns
        cols = [chars[starts[i]:ends[i]] for i in originalorder]
        # recover the rows
        pairs = []
        for i in range((len(chars) - 1) // self.keylen + 1):
            for j in range(self.keylen):
                if i * self.keylen + j < len(chars):
                    pairs.append(cols[j][i])

        return ''.join([self.decode[pairs[i] + pairs[i + 1]] for i in range(
            0, len(pairs), 2)])

if __name__ == "__main__":
    PCHARS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890')
    shuffle(PCHARS)
    POLYBIUS = ''.join(PCHARS)
    with open('unixdict.txt') as fh:
        WORDS = [w for w in (fh.read()).split()
                if len(w) == 9 and len(w) == len(set(list(w)))]
        KEY = choice(WORDS)

    SECRET, MESSAGE = ADFGVX(POLYBIUS, KEY), 'ATTACKAT1200AM'
    print(f'Polybius: {POLYBIUS}, key: {KEY}')
    print('Message: ', MESSAGE)
    ENCODED = SECRET.encrypt(MESSAGE)
    DECODED = SECRET.decrypt(ENCODED)
    print('Encoded: ', ENCODED)
    print('Decoded: ', DECODED)

