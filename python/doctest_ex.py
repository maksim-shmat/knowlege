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
'''
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
'''
#6 doctest blankline

'''
def double_space(lines):
    """Show list of strings with double spaces.

    >>> double_space(['Line one.', 'Line two.'])
    Line one.
    <BLANKLINE>
    Line two.
    <BLANKLINE>
    """
    for l in lines:
        print(l)
        print()

RESULTS:
Trying:
    double_space(['Line one.', 'Line two.'])
Expecting:
    Line one.
    <BLANKLINE>
    Line two.
    <BLANKLINE>
ok
1 items had no tests:
    doctest_ex
1 items passed all tests:
   1 tests in doctest_ex.double_space
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
'''

#7 Trubles with unvisible spaces
'''
def my_function(a, b):
    """
    >>> my_function(2, 3)
    6 # this
    >>> my_function('a', 3)
    'aaa'
    
    """
    return a * b
'''

#7.1 doctest ndiff for check unvisible spaces

'''
def my_function(a, b):
    """
    >>> my_function(2, 3) #doctest: +REPORT_NDIFF
    6 
    >>> my_function('a', 3)
    'aaa'
    
    """
    return a * b

RESULTS:
Trying:
    my_function(2, 3) #doctest: +REPORT_NDIFF
Expecting:
    6 
**********************************************************************
File "/home/jack/django2/knowlege/python/doctest_ex.py", line 156, in doctest_ex.my_function
Failed example:
    my_function(2, 3) #doctest: +REPORT_NDIFF
Differences (ndiff with -expected +actual):
    - 6 
    ?  -
    + 6
Trying:
    my_function('a', 3)
Expecting:
    'aaa'
ok
1 items had no tests:
    doctest_ex
**********************************************************************
1 items had failures:
   1 of   2 in doctest_ex.my_function
2 tests in 2 items.
1 passed and 1 failed.
***Test Failed*** 1 failures.
'''

#8 normalize whitespace

'''
def my_function(a, b):
    """Return a * b.

    >>> my_function(['A', 'B'], 3)  #doctest: +NORMALIZE_WHITESPACE
    ['A', 'B',
     'A', 'B',
     'A', 'B']

    >>> my_function(['A', 'B'], 2)  #doctest: +NORMALIZE_WHITESPACE
    [ 'A', 'B',
      'A', 'B', ]
    """
    return a * b
'''

#9 doctest docstring

'''
"""Test may be in any string of docs into module.

Tests module level accross boarders classes and functions

>>> A('a') == B('b')
False

"""


class A:
    """Simple class.

    >>> A('instance_name').name
    'instance_name'

    """

    def __init__(self, name):
        self.name = name

    def method(self):
        """Return special value.

        >>> A('name').method()
        'eman'

        """
        return ''.join(reversed(self.name))


class B(A):
    """More simple class.

    >>> B('different_name').name
    'different_name'
    """
'''

#10 doctest in help  # for doctest_in_help.txt
# start with: $ python3 -m doctest -v doctest_in_help.txt
'''

def my_function(a, b):
    """Return a * b"""
    return a * b
'''

#11 doctest testmod

'''
def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function('a', 3)
    'aaa'

    """
    return a * b

if __name__ == '__main__':
    import doctest
    doctest.testmod()

RESULTS:
$ python3 doctest_ex.py -v
Trying:
    my_function(2, 3)
Expecting:
    6
ok
Trying:
    my_function('a', 3)
Expecting:
    'aaa'
ok
1 items had no tests:
    __main__
1 items passed all tests:
   2 tests in __main__.my_function
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
'''

#12 doctest testfile

import doctest
'''
if __name__ == '__main__':
    doctest.testfile('doctest_in_help.txt')
'''

#13 doctest unittest

import doctest
import unittest
'''
import doctest_simple

suite = unittest.TestSuite()
suite.addTest(doctest.DocTestSuite(doctest_simple))
suite.addTest(doctest.DocFileSuite('doctest_in_help.txt'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
'''

#14 doctest test globals
# run with: $ python3 -m doctest -v doctest_test_globals.py

'''
class TestGlobals:

    def one(self):
        """
        >>> var = 'value'
        >>> 'var' in globals()
        True
        """

    def two(self):
        """
        >>> 'var' in globals()
        False
        """
'''

#15 doctest mutable globals
# run with: $ python3 -m doctest -v doctest_mutable_globals.py
'''
_module_data = {}


class TestGlobals:

    def one(self):
        """
        >>> TestGlobals().one()
        >>> 'var' in _module_data
        True

        """
        _module_data['var'] = 'value'

    def two(self):
        """
        >>> 'var' in _module_data
        False
        """
'''
