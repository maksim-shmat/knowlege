"""doctest about"""


# doctest simple
# with: $ python3 -m doctest -v doctest_simple.py
'''
def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b

RESULTS:
Trying:
    my_function(2, 3)
Expecting:
    6
ok
Trying:
    my_function("a", 3)
Expecting:
    "aaa"
ok
1 items had no tests:
    doctest_ex
1 items passed all tests:
   2 tests in doctest_ex.my_function
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
'''

#2 dictest simple with docs

'''
def my_function(a, b):
    """Return a * b.
    Work with integers:
    >>> my_function(2, 3)
    6
    >>>                           # ! finish code
    and strings:
    >>> my_function('a', 3)
    'aaa'
    >>>
    """
    return a * b
'''

#3 doctest unpredictable

'''
class MyClass:
    pass

def unpredictable(obj):
    """Return new list who contain object.

    >>> unpredictable(MyClass())
    [<doctest_unpredictable.MyClass object at 0x100055a2d0>]
    """
    return[obj]
'''

#4 doctest ellipsis

'''
class MyClass:
    pass

def unpredictable(obj):
    """Return new list how contain object.

    >>> unpredictable(MyClass())  # doctest: +ELLIPSIS
    [<doctest_ellipsis.MyClass object at 0x...>]
    """
    return [obj]
'''

#5 doctest hashed values tests

import collections

def group_by_length(words):
    """Return dict, how grupped words to the sets by lengths.

    >>> grouped = group_by_length(['python', 'module', 'of',
    ... 'the', 'week'])
    >>> grouped == { 2:set(['of']),
    ...              3:set(['the']),
    ...              4:set(['week']),
    ...              6:set(['python', 'module']),
    ...              }
    True
    
    """
    d = collections.defaultdict(set)
    for word in words:
        d[len(word)].add(word)
    return d

#6 
