"""pprint() about."""

from pprint import pprint

from pprint_data import data  # make a file pprint_data.py

print('PRINT:')
print(data)
print()
print('PRINT:')
pprint(data)

'''RESULTS:
PRINT:
[(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}), (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}), (3, ['m', 'n']), (4, ['o', 'p', 'q']), (5, ['r', 's', 't', 'u', 'v', 'x', 'y', 'z'])]

PRINT:
[(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
 (2,
  {'e': 'E',
   'f': 'F',
   'g': 'G',
   'h': 'H',
   'i': 'I',
   'j': 'J',
   'k': 'K',
   'l': 'L'}),
 (3, ['m', 'n']),
 (4, ['o', 'p', 'q']),
 (5, ['r', 's', 't', 'u', 'v', 'x', 'y', 'z'])]
'''

#2 pformat() for formating stdout

import logging
from pprint import pformat
from pprint_data import data

logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)-8s %(message)s',
)

logging.debug('Logging pformatted data')
formatted = pformat(data)
for line in formatted.splitlines():
    logging.debug(line.rstrip())

'''RESULTS:
DEBUG    Logging pformatted data
DEBUG    [(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
DEBUG     (2,
DEBUG      {'e': 'E',
DEBUG       'f': 'F',
DEBUG       'g': 'G',
DEBUG       'h': 'H',
DEBUG       'i': 'I',
DEBUG       'j': 'J',
DEBUG       'k': 'K',
DEBUG       'l': 'L'}),
DEBUG     (3, ['m', 'n']),
DEBUG     (4, ['o', 'p', 'q']),
DEBUG     (5, ['r', 's', 't', 'u', 'v', 'x', 'y', 'z'])]
'''

#3 Class PrettyPrinter() from pprint() for user data if it use __repr__()

from pprint import pprint

class node:

    def __init__(self, name, contents=[]):
        self.name = name
        self.contents = contents[:]

    def __repr__(self):
        return (
                'node(' + repr(self.name) + ', ' +
                repr(self.contents) + ')'
        )

trees = [
        node('node-1'),
        node('node-2', [node('node-2-1')]),
        node('node-3', [node('node-3-1')]),
]
pprint(trees)

'''RESULTS:
[node('node-1', []),
 node('node-2', [node('node-2-1', [])]),
 node('node-3', [node('node-3-1', [])])]
'''

#4 pprint recursion

from pprint import pprint

local_data = ['a', 'b', 1, 2]
local_data.append(local_data)  # list add to oneself

print('id(local_data) =>', id(local_data))
pprint(local_data)

'''RESULTS:
id(local_data) => 140419950948992
['a', 'b', 1, 2, <Recursion on list with id=140419950948992>]
'''

#5 restrict depth print

from pprint import pprint

from pprint_data import data

pprint(data, depth=1)
pprint(data, depth=2)

'''RESULTS:
[(...), (...), (...), (...), (...)]
[(1, {...}), (2, {...}), (3, [...]), (4, [...]), (5, [...])]
'''

#6 pprint width

from pprint import pprint

from pprint_data import data

for width in [80, 5]:
    print('WIDTH =', width)
    pprint(data, width=width)
    print()

'''RESULTS:
WIDTH = 5
[(1,
  {'a': 'A',
   'b': 'B',
   'c': 'C',
   'd': 'D'}),
 (2,
  {'e': 'E',
   'f': 'F',
   'g': 'G',
   'h': 'H',
   'i': 'I',
   'j': 'J',
   'k': 'K',
   'l': 'L'}),
 (3,
  ['m',
   'n']),
 (4,
  ['o',
   'p',
   'q']),
 (5,
  ['r',
   's',
   't',
   'u',
   'v',
   'x',
   'y',
   'z'])]
'''
#7 pprint compact

from pprint import pprint

from pprint_data import data

print('DEFAULT:')
pprint(data, compact=False)
print('\nCOMPACT:')
pprint(data, compact=True)

'''RESULTS:
DEFAULT:
[(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
 (2,
  {'e': 'E',
   'f': 'F',
   'g': 'G',
   'h': 'H',
   'i': 'I',
   'j': 'J',
   'k': 'K',
   'l': 'L'}),
 (3, ['m', 'n']),
 (4, ['o', 'p', 'q']),
 (5, ['r', 's', 't', 'u', 'v', 'x', 'y', 'z'])]

COMPACT:
[(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
 (2,
  {'e': 'E',
   'f': 'F',
   'g': 'G',
   'h': 'H',
   'i': 'I',
   'j': 'J',
   'k': 'K',
   'l': 'L'}),
 (3, ['m', 'n']), (4, ['o', 'p', 'q']),         # This is compact
 (5, ['r', 's', 't', 'u', 'v', 'x', 'y', 'z'])]
'''
