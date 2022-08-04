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

# Using groupby

import urllib, itertools

# words = urllib.urlopen('http://wiki.puzzlers.org/pub/wordlist/unixdict.txt').read().split()
words_file = open('unixdict.txt', 'r')
text = words_file.read()
words_file.close()

text = text.lower()
words = text.split()
print(len(words))

anagrams = [list(g) for k,g in itertools.groupby(sorted(words, key=sorted), key=sorted)]

count = max(len(ana) for ana in anagrams)
for ana in anagrams:
    if len(ana) >= count:
        print(ana)
print(count)

"""
# Or disaggregating, speeding up a bit by avoiding the slightly expensive use
# of sorted as a key, updating for Python 3, and using a local unixdict.txt
from os.path import expanduser
from itertools import groupby
from operator import eq

# main :: ID ()
def main():
    """Largest anagram group in local unixdict.txt"""
    print(unlines(
        largestAnagramGroups(
            lines(readFile('unixdict.txt'))
        )
    ))

# LagestAnagramGroups :: [String] -> [[String]]
def largestAnagramGroups(ws):
    """A list of the anagram groups of the largest size found in a
    given list of words.
    """
    # wordChars :: String -> (String, String)
    def wordChars(w):
        """A word paired with it's AZ sorted characters"""
        return (''.join(sorted(w)), w)

    groups = list(map(compose(list)(snd),
        groupby(
            sorted(
                map(wordChars, ws),
                key=fst
            ),
            key=fst
        )
    ))

    intMax = max(map(len, groups))
    return list(map(
        compose(unwords)(curry(map)(snd)),
        filter(compose(curry(eq)(intMax))(len), groups)
    ))

# GENERIC ------------
# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    """Right to left function composition."""
    return lambda f: lambda x: g(f(x))

# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    """A curried function derived
    from an uncurried function."""
    return lambda a: lambda b: f(a, b)

# fst :: (a, b) -> a
def fst(tpl):
    """First member of a pair."""
    return tpl[0]

# lines :: String -> [String]
def lines(s):
    """A list of strings,
    (containing no newline characters)
    derived from a single new-line delimited string."""
    return s.splitlines()

# from os.path import expanduser
# readFile :: FilePath -> IO String
def readFile(fp):
    """The contents of any file at the path
    derived by espanding any ~ in fp."""
    with open(expanduser(fp), 'r', encoding='utf-8') as f:
        return f.read()

# snd :: (a, b) -> b
def snd(tpl):
    """Second member of a pair."""
    return tpl[1]

# unlines :: [String] -> String
def unlines(xs):
    """A single string derived by the intercalation
    of a list of strings with the newline character."""
    return '\n'.join(xs)

# unwords :: [String] -> String
def unwords(xs):
    """A space-separated string derived from a list of words."""
    return ' '.join(xs)

# MAIN ----------
if __name__ == "__main__":
    main()
