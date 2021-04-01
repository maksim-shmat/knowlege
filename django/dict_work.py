""" Work with dictionary from Python and Django."""

###### Merge Dict Python3 make new object and it different. And only 2 dict.

dict_one = {'a': 1, 'b': 2, 'c': 3}
dict_two = {'c': 4, 'd': 5, 'e': 6}
combined = dict(dict_one, **dict_two)
combined['a'], combined['c'], combined['e']
# (1, 4, 6)
dict_one['a'] = 42
combined['a']
# 1

###### Merge Dict with Django with many dict and fool merge objects

from django.utils.datastructures import MergeDict

dict_one = {'a': 1, 'b': 2, 'c': 3}
dict_two = {'c': 4, 'd': 5, 'e': 6}
combined = MergeDict(dict_one, dict_two)
combined['a'], combined['c'], combined['e']
# (1, 3, 6)
dict_one['a'] = 42
combined['a']
42

######
