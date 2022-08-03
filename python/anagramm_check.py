"""Check anagrams."""

"""
from collections import Counter

str1 = 'proglib'
str2 = 'proglib'

print(Counter(str1) == Counter(str2))

#2 Using default dict

import urllib.request
from collections import defaultdict

#words = urllib.request.urlopen('http://wiki.puzzlers.org/pub/wordlists/unixdict.txt').read().split()
words_file = open('unixdict.txt', 'r')
text = words_file.read()
words_file.close()

text = text.lower()
words = text.split()
print(len(words))

anagram = defaultdict(list)  # map sorted chars to anagrams
for word in words:
    anagram[tuple(sorted(word))].append(word)

count = max(len(ana) for ana in anagram.values())
for ana in anagram.values():
    if len(ana) >= count:
        print([x.decode() for x in ana])

#error: decode() not str method
"""

# Using groupby

