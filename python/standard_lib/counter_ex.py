"""Counter from collections lib about."""

#1 counter init

import collections

print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))
print(collections.Counter(a=2, b=3, c=1))

'''RESULTS:
Counter({'b': 3, 'a': 2, 'c': 1})
Counter({'b': 3, 'a': 2, 'c': 1})
Counter({'b': 3, 'a': 2, 'c': 1})
'''

#2 counter update

import collections

c = collections.Counter()

print('Initial :', c)

c.update('abcdaab')
print('Sequence:', c)

c.update({'a': 1, 'd': 5})
print('Dict :', c)

'''RESULTS:
Counter({'b': 3, 'a': 2, 'c': 1})
Counter({'b': 3, 'a': 2, 'c': 1})
Counter({'b': 3, 'a': 2, 'c': 1})
'''
#3 counter get values

import collections

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print('{}: {}'.format(letter, c[letter]))

'''RESULTS:
a: 3
b: 2
c: 1
d: 1
e: 0
'''

#4 counter elements()
