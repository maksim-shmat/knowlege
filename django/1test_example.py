""" Django find your tests in any files with name as test.py """

import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    """ This test for site of Questions from Django site examples, I don't 
    make his that he little primitive and don't actual for prodaction.
    """
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

# Running tests
#$ python manage.py test polls
########
# more tests for tose example
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, second=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
"""
###########
# polls/tests.py
from django.urls import reverse

def create_question(qusetion_text, days):
    """
    Create a question with the given 'qustion_text' and published the
    given number of 'days' offset to now (negative for questions published
    in the past, polsitive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_question(self):
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
        Even if both past and future question exist, only past questions
        are displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response =self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
                response.context['latest_question_list'],
                ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(qusstion_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
                response.context['latest_question_list'],
                ['<Question: Past question 2.>', '<Question: Past question 1.>']
"""
###########
# polls/tests.py testing class DetailView in views.py

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text='Future question.',
            days=-5)
        url = reverse('polls:detail', args=(post_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


#########
# Writing tests with django
from django.test import TestCase
from myapp.models import Animal

class AnimalTestCase(TestCase):
    def setUP(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name='cat', sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
#########
