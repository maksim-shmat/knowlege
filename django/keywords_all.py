"""Print all keywords."""

import keyword

if __name__ == '__main__':
    # get all keywords
    keywords = keyword.kwlist
    # print the keywords
    for key in keywords:
        print(key)

######

s = keyword.kwlist
print(s)
