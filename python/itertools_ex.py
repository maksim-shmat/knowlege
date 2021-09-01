"""itertools about."""

import itertools as it

# accumulate() - min(11), min(11,3), min(11, 3, 9)...
zacum = list(it.accumulate([11, 3, 9, 7, 5], func=min))
print(zacum)
print()

###### chain() glued several elements to one

fchain = list(it.chain([1, 2, 3], [4, 5], [6]))
print(fchain)
print()

###### combinations() - combinations and length of combinations

acombo = list(it.combinations([1, 2, 3], 2))
print(acombo)
print()

###### clear elements, del it

from itertools import compress

letters = ['A', 'B', 'C', 'B', 'D']
mask = [1, 0, 1, 0, 0]  # 1 == True
result = compress(letters, mask)
print(list(result))

