moby_words = []
for word in infile: # with open as infile
    if word.strip():
        moby_words.append(word.strip())

moby_words = []
with open('moby_01_clean.txt') as infile:
    for word in infile:
        if word.strip():
            moby_words.append(word.srtip())

word_list = list(word_count.items())
word_list.sort(key=lambda x: x[1])
print("Most common words:")
for word in reversed(word_list[-5:]):
    print(word)
print("\nLeast common words:")
for word in word_list[:5]:
    print(word)
"""
Most common words:
('the', 14)
('and', 9)
('i', 9)
('of', 8)
('is', 7)

Least common words:
('see', 1)
('growing', 1)
('soul', 1)
('having', 1)
('regulating', 1)
