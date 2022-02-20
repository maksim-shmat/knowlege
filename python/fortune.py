"""Work with random."""

# $ python3 fortune.py /usr/share/dict/words
# random word

import fileinput, random

fortunes = list(fileinput.input())

print(random.choice(fortunes))
