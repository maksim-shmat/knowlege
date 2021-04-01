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

###### Multi Value Dict

from django.utils.datastructures import MultiValueDict

d = MultiValueDict({'a': ['1', '2', '3'], 'b': ['4'], 'c': ['5', '6']})
d['a'], d['b'], d['c']
# ('3', '4', '6')
d.getlist('a')
# ['1', '2', '3']
d.getlist('b')
# ['4']
d.getlist('c')
# ['5', '6']
d = MultiValueDict({'e': '7'})
d['e']
# '7'
d.getlist('e')
# '7'

###### Sorted Dict

from django.utils.datastructures import SortedDict

d = SortedDict([('c', '1'), ('d', '3'), ('a', '2')])
d.keys()
# ['c', 'd', 'a']
d.values()
# ['1', '3', '2']
d['b'] = '4'
d.items()
# [('c', '1') ('d', '3'), ('a', '2'), ('b', '4')]

######
