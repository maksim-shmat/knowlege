"""Collections lib about."""

# How many onesi repeat elements
from collections import Counter
a = ['a', 'b', 'c', 'a', 'b', 'c', 'b', 'b', 'b', 'e', 'a']
cnt = Counter(a)
cnt.most_common(3)
print(cnt)
print()

######
