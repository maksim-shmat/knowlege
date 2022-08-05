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
            for word1, word2 in combinations(words, 2)
            if all(ch1 != ch2 for ch1, ch2 in zip(word1, word2)) ]

def most_deranged_ana(anagrams):
    ordered_anagrams = sorted(anagrams.items(),
            key=lambda x:(-len(x[0]), x[0]))
    many_anagrams = [anas for _, anas in ordered_anagrams if len(anas) > 2]
    d_of_anas = [is_deranged(ana_group) for ana_group in many_anagrams]
    d_of_anas = [d_group for d_group in d_of_anas if d_group]
    d_of_anas.sort(key=lambda d_group:(-len(d_group), -len(d_group[0])))
    mx = len(d_of_anas[0])
    most = [sorted(d_group) for d_group in d_of_anas if len(d_group) == mx]
    return most

if __name__ == '__main__':
    words = '~/django2/knowlege/python/unixdict.txt'
    print("Word count:", len(words))

    anagrams = find_anagrams(words)
    print("Anagram count: ", len(anagrams), "\n")

    most = most_deranged_ana(anagrams)
    print(f"\nThere are {len(most)} groups of anagrams all containing"
          f" a max {len(most[0])} deranged word-pairs:")
    for pairs in most:
        print()
        print('  ' + '\n  '.join(', '.join(p) for p in pairs))
