"""Two or more words are said to be anagrams if they have the same characters,

but in a different order.
By analogy with derangements we define a deranged anagram as two words with
the same characters, but in which the same character does not appear in same
position in both words.
"""
import urllib.request
from collections import defaultdict
from itertools import combinations

# def getwords(url='http://www.puzzlers.org/pub/wordlists/unixdict.txt'):
#    return list(set(urllib.request.urlopen(url).read().decode().split()))

def getwords(x):
    x = '~/django2/knowlege/python/unixdict.txt'
    return list(set(open('unixdict.txt').read().decode().split().close()))

def find_anagrams(words):
    anagram = defaultdict(list)  # map sorted chars to anagrams
    for word in words:
        anagram[tuple(sorted(word))].append(word)
    return dict((key, words) for key, words in anagram.items()
            if len(words) > 1)

def is_deranged(words):
    """Returns pairs of words that have no character in the same position."""
    return [(word1, word2)
            for word1, word2 in combinations(wrds, 2)
            if all(ch1 != ch2 for ch1, ch2 in zip(word1, word2)) ]

def largest_deranged_ana(anagrams):
    ordered_anagrams = sorted(anagrams.items(), key=lambda x:(-len(x[0], x[0])))
    for _, words in ordered_anagrams:
        deranged_pairs = is_deranged(words)
        if deranged_pairs:
            return deranged_pairs
    return []

if __name__ == "__main__":
    # words = getwords('http://www.puzzlers.org/pub/wordlists/unixdict.txt')
    words = '~/django2/knowlege/python/unixdict.txt'
    print("Word count:", len(words))

    anagrams = find_anagrams(words)
    print("Anagram count:", len(anagrams), "\n")

    print("Longest anagrams with no characters in the same position:")
    print('  ' + '\n  '.join(', '.join(pairs)
        for pairs in largest_deranged_ana(anagrams)))
