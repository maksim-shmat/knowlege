"""Python tricks."""

# How to merge two dicts
>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}

>>> z = {**x, **y}

>>>z
{'a':1, 'b': 3, 'c': 4}

########
