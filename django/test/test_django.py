""" What in heaven's name django tests are you talking about?"""

###### wraps(func)

def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def test():
    print('Testing!')
decorated = decorator(test)
decorated.__name__
# 'wrapper'

### wraps() from Python
from django.utils.functional import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def test():
    print('Testing!')

decorated = decorator(test)
decorated.__name__
# 'test'

#1 Simple test example with unittest

import unittest

class IntergerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):
        self.assertEquals(1 + 2, 3)

    def testMultiply(self):
        self.assertEquals(5 * 8, 40)

if __name__ == '__main__':
    unittest.main()

#2 How to start test on the Django?
./manage.py test

#3 Check birthdate function

from django.db import models

class Person(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __unicode__(self):
        return "%s %s" % (self.first, self.last)

    def age_on_date(self, date):
        if date < self.birthdate:
            return 0
        return (date - self.birthdate).days / 365

# Handling tests
>>> from datetime import date
>>> p = Person(firstname="Jeff", lastname="Forcier", city="Jersey City", state="NJ", birthdate=date(1982, 7, 15))
>>> p.age_on_date(date(2008, 8, 10))
26
>>> p.age_on_date(date(1950, 1, 1))
0
>>> p.age_on_date(p.birthdate)
0

# doctests
def age_on_date(self, date):
    """Return integer = age of man.
    >>> from datetime import date  # >>> in code is normal for doctests
    >>> p = Person(firstname="Jeff", lastname="Forcier", city = "Jersey City", state="NJ", birthdate=date(1982, 7, 15))
    >>> p.age_on_date(date(2008, 8, 10))
    26
    >>> p.age_on_date(date(1950, 1, 1))
    0
    >>> p.age_on_date(p.birthdate)
    p
    """
    if date < self.birthdate:
        return 0
    return (date - self.birthdate).days / 365

# next run
$ ./manage.py test myapp

#4 simple test polls/tests.py

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

# python manage.py test polls
