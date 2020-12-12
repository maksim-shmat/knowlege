class EmptyStringError(Exception):
    pass
def clean_line(line):
    """ Change register and del prepination mark.  """
    # Show exception if the string is empty
    if not line.strip():
        raise EmptyStringError()
    # Go to one register
    cleaned_line = line.lower()

    # Del prepination mark
    cleaned_line = cleaned_line.translate(punct)
    return cleaned_line
def count_words(words):
    """ Get cleaned list of words and return dict of counters.  """
    word_count = {}
    for word in words:
        try:
            count = word_count.setdefault(word, 0)
        except TypeError:
            # If 'word' don't hashig - go to next word.
            pass
        word_count[word] += 1
    return word_count
def word_stats(word_count):
    """ Get dict counters and return upper and lower five elements.  """
    word_list = list(word_count.items())
    word_list.sort(key=lambda x: x[1])
    try:
        least_common = word_list[:5]
        most_common = word_list[-1:-6:-1]
    except IndexError as e:
        # If list empty or to much short - only return full list
        least_common = word_list
        most_common = list(reversed(word_list))
    return most_common, least_common
