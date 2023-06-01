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

#5 polls/tests.py

def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() return False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

def testy_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datatime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)

#6 polls/tests.py IF no question exist

from django.urls import reverse

def create_question(question_text, days):
    """
    Create a question with the given 'question_text' and published the
    given number of 'days', offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


calss QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
                response.context['latest_question_list'],
                ['<Question: Past question.>']
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on 
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
                response.context['latest_question_list'],
                ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """
        The question index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
                response.contexti['latest_question_list'],
                ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

#7 Basic unit test script

from django.test import SimpleTestCase):


class TestingCalibrator(SimpleTestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pass(self):
        '''Checks if True == True, Value set to True'''
        self.assertFalse(True)

# $ python manage.py test becoming_a_django_entdev.chapter_9

#8 Testing Django Models
# models.py
...
MAKE_CHOICES = (
        ...
        (8, 'Jeep'),
        ...
)

# tests.py
from django.test import ..., TestCase
from djmoney.money import Money
from ..chapter_3.models import (
        Engine,
        Seller,
        Vehicle,
        VehicleModel
)

class ModelUnitTestCase(TestCase):
    def setUp(self):
        model = VehicleModel.objects.create(
                name = 'Grand Cherokee Laredo 4WD',
                make = 8
        )
        engine = Engine.objects.create(
                name = '3.6L FI FFV DO',
                vehicle_model = model
        )
        vehicle = Vehicle.objects.create(
                vin = 'aa890123456789012',
                sold = False,
                price = Money(39875, 'USD'),
                make = 8,
                vehicle_model = model,
                engine = engine
        )
        seller = Seller.objects.create_user(
                'test',
                'testing@example.com',
                'testpassword',
                is_staff = True,
                is_superuser = True,
                is_active = True,
                name = 'Chapter 9 Seller 1'
        )
        seller.vehicles.set([vehicle])

    def test_full_vehicle_name(self):
        vehicle_1 = Vehicle.objects.get(
                vin = 'aa890123456789012'
        )
        self.assertEqual(
                vehicle_1.full_vehicle_name(),
                'Jeep Grand Cherokee Laredo 4WD - 3.6L FI
                FFV DO'
        )

#9 
