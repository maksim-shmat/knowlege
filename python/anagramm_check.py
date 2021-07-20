"""Check anagramms."""

from collections import Counter

str1 = 'proglib'
str2 = 'proglib'

print(Counter(str1) == Counter(str2))
