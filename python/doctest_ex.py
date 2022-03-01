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
