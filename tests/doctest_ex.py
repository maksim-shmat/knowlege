"""Tests with doctest."""

import doctest, doctest_ex

def square(x):
    """
    Squares a number and returns the result.
    >>> square(2)
    4
    >>> square(3)
    9
    >>> square(3)  # for bad test
    27
    """
    return x * x

if __name__ == '__main__':

    doctest.testmod(doctest_ex)

# $ python3 doctest_ex.py -v

# for unittest_ex.py

def product(x, y):
    if x == 7 and y == 9:
        return 'An insidious bug has surfaced!'
    else:
        return x * y
# .. == OK OK, FF == Failure Failure, .F == OK Failure
