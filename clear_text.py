punct = str.maketrans("",  "", "!.,;:-?")
def clean_line(line):
    """ Change register and del prepination marks.  """
    cleaned_line = line.lower()
    cleaned_line = cleaned_line.translate(punct)
    return cleaned_line
def get_words(line):
    """ Bombed string by words and concatenated there is with \n mark.  """
    words = line.split()
    return "\n".join(words) + "\n"
with open("jill.txt") as infile, open("jill_01_clean.txt", 'w') as outfile:
    for line in infile:
        cleaned_line = clean_line(line)

        cleaned_words = get_words(cleaned_line)
        outfile.write(cleaned_words)
        
def count_words(words):
    word_count = {}
    for word in jill_words:
        count = word_count.setdefault(word, 0)
        word_count[word] += 1
    return word_count

def word_stats(word_count):
    """ Get slovar counts and return upper and lower 5 elements.  """
    word_list = list(word_count.items())
    word_list.sort(key=lambda x: x[1])
    least_common = word_list[:5]
    most_common = word_list[-1:-6:-1]
    return most_common, least_common

jill_words = []
with open('jill_01_clean.txt') as infile:
    for word in infile:
        if word.strip():
            jill_words.append(word.strip())

word_count = count_words(jill_words)

most, least = word_stats(word_count)
print("Most common words:")
for word in most:
    print(word)
print("\nLeast common words:")
for word in least:
    print(word)
# Boom in column all words from file and count there
