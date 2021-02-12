""" Django find your tests in any files with name as test.py """

import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    """This test for site of Questions from Django site examples, I don't 
    make his that he little primitive and don't actual for prodaction.
    """
    def test_was_published_recently_with_future_question(self):
        """ was_published_recently() returns False for questions whose pub_date
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
    """was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    """was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, second=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)

###########
# polls/tests.py
from django.urls import reverse

def create_question(qusetion_text, days):
    """Create a question with the given 'qustion_text' and published the
    given number of 'days' offset to now (negative for questions published
    in the past, polsitive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_question(self):
        """Questions with a pub_date in the past are displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
                response.context['latest_question_list'],
                ['<Question: Past question.>']
        )

    def test_future_question(self):
        """Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """Even if both past and future question exist, only past questions
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
        """The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(qusstion_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
                response.context['latest_question_list'],
                ['<Question: Past question 2.>', '<Question: Past question 1.>'])

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
# Set setting the language for test
from django.conf import settings

def test_language_using_cookie(self):
    self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'fr'})
    response = self.client.get('/')
    self.assertEqual(response.content, b"Bienvenue sur mon site.")

###

def test_language_using_header(self):
    response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='fr')
    self.assertEqual(response.content, b"Bienvenue sur mon site.")

###
from django.utils import translation

def test_language_using_override(self):
    with translation.override('fr'):
        response = self.client.get('/')
    self.assertEqual(response.content, b"Bienvenue sur mon site.")

############
# Unit test using the test client
import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/customer/details/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.context['customers']), 5)

############
# liveServerTestCase with selenium
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.slenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_wpath('//input[@value="Log in"]').click()
##########
# SQLite run the tests with selenium
def test_login(self):
    from selenium.webdriver.support.wait import WebDriverWait
    timeout = 2
    ...
    self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
    # Wait until the response is received
    WebDriverWait(self.selenium, timeout).until(
            lambda driver: driver.find_element_by_tag_nam('body'))
########
# use default test client
import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/customer/details/')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        client = Client()
        response = client.get('/customer/index/')
        self.assertEqual(response.status_code, 200)
###
from django.test import TestCase

class SimpleTest(TestCase):
    def test_detail(self):
        response = self.client.get('/customer/details/')
        self.assertEqual(response.status_code, 200)

###########
# castomizing the test client
from django.test import Client, TestCase

class MyTestClient(Client):
    # Specialized methods for your environment
    ...
class MyTest(TestCase):
    client_class = MyTestClient

    def test_my_stuff(self):
        # Here self.client is an instance of MyTestClient...
        call_some_test_code()
##########
# add dumbdata fixtures for the test
from django.test import TestCase
from myapp.models import Animal

class AnimalTestCase(TestCase):
    fixtures = ['mammals.json', 'birds']

    def setUp(self):
        # Test definitions as before.
        call_setup_methods()

    def test_fluffy_animals(self):
        # A test that uses the fixtures.
        call_some_test_code()

###########
# use SimpleTestCase.settings()
from django.test import TestCase

class LoginTestCase(TestCase):
    def test_login(self):
        # First check for the default behavior
        response = self.client.get('/sekrit/')
        self.assertRedirect(response, '/accounts/login/?next=/sekrit/')

        # Then override the LOGIN_URL setting
        with self.settings(LOGIN_URL='/other/login/'):
            response = self.client.get('/sekrit/')
            self.assertRedirects(response, '/other/login/?next=/sekrit/')
###########
# use SimpleTestCase.modify_settings()
from django.test import TestCase

class MiddlewareTestCase(TestCase):

    def test_cache_middleware(self):
        with self.modify_settings(MIDDLEWARE={
            'append': 'django.middleware.cache.FetchFromCacheMiddleware',
            'prepend': 'django.middleware.cache.UpdateCacheMiddleware',
            'remove': [
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
            ],
        }):
            response = self.client.get('/')
            # ...
############
# use override_settings()
from django.test import TestCase, override_settings

class LoginTestCase(TestCase):
    @override_settings(LOGIN_URL='/other/login/')
    def test_login(self):
        response = self.client.get('/sekrit/')
        self.assertRedirects(response, '/other/login/?next=/sekrit/')

###
# The decorator can also be applied to TestCase classes
from django.test import TestCase, override_settings

@override_settings(LOGIN_URL='/other/login/')
class LoginTestCase(TestCase):

    def test_login(self):
        response = self.client.get('/sekrit/')
        self.assertRedirects(response, '/other/login/?next=/sekrit/')

############
# use modify_settings() decorator
from django.test import TestCase, modify_settings

class MiddlewareTestCase(TestCase):
    @modify_settings(MIDDLEWARE={
        'append': 'django.middleware.cache.FetchFromCacheMiddleware',
        'prepend': 'django.middleware.cache.UpdateCacheMiddleware',
    })
    def test_cache_middleware(self):
        response = self.client.get('/')
        # ...
###
# the decorator can also be applied to test case classes:
from django.test import TestCase, modify_settings

@modify_settings(MIDDLEWARE={
    'append': 'django.middleware.cache.FetchFromCacheMiddleware',
    'prepend': 'django.middleware.cache.UpdateCacheMiddleware',
})
class MiddlewareTestCase(TestCase):
    def test_cache_middleware(self):
        response = self.client.get('/')
        # ...
##########
# tagging tests
# you can tag your tests so you can easily run a particular subset. For
# example, you might label fast or slow tests
from django.test import tag

class SampleTestCase(TestCase):
    @tag('fast')
    def test_fast(self):
        ...
    @tag('slow')
    def test_slow(self):
        ...
    @tag('slow', 'core')
    def test_slow_but_core(self):
        ...
### subclasses inherit tags from superclasses, and methods inherit tags from
# their class
    @tag('slow', 'core')
    class SampleTestCase(TestCase):
        ...
    @tag('foo')
    class SampleTestCaseChild(SampleTestCase):
        @tag('bar')
        def test(self):
            ...
### start tests
# $./manage.py test --tag=fast
# $./manage.py test --tag=fast --tag=core
# $./manage.py test --tag=core --exclude-tag=slow
###############
# test email services with dummy outbox
from django.core import mail
from django.test import TestCase

class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail(
                'Subject here', 'Here is the message.',
                'from@example.com', ['to@example.com'],
                fail_silently=False,
        )
        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
#########
# management commands can be tested with the call_command() function.
from io import StringIO
from django.core.management import call_command
from django.test import TestCase

class ClosepollTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command('closepoll', stdout=out)
        self.assertIn('Expected output', out.getvalue())

###########
# skipping tests
class MyTests(TestCase):
    @skipIfDBFeature('supports_transactions')
    def test_transaction_behavior(self):
        # ... conditional test code
        pass

###
class MyTests(TestCase):
    @skipUnlessDBFeature('supports_transactions')
    def test_transaction_behavior(self):
        # ... conditional test code
        pass
############
# use request factory for test
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .view import MyView, my_view

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
                username='jacob', email='jacob@...', password='top_secret')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/customer/details')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.use manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = my_view(request)
        # Use this syntax for class-based views.
        response = MyView.as_view()(request)
        self.assertEqual(response.status_code, 200)

###########
# testing class-based views
# views.py
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'myapp/home.html'

    def get_context_data(self, **kwargs):
        kwargs['environment'] = 'Production'
        return super().get_context_data(**kwargs)

###
# tests.py
from django.test import RequestFactory, TesCase
from .views import HomeView

class HomePageTest(TestCase):
    def test_environment_set_in_context(self):
        request = RequestFactory().get('/')
        view = HomeView()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('environment', context)

###########
# enforce running test classes sequentially
import os

from django.test import TestCase
from django.test.testcases import SerializeMixin

class ImageTestCaseMixin(SerializeMixin):
    lockfile = __file__

    def setUp(self):
        self.filename = os.path.join(temp_storage_dir, 'my_file.png')
        self.file = create_file(self.filename)

class RemoveImageTests(ImageTestCaseMixin, TestCase):
    def test_remove_image(self):
        os.remove(self.filename)
        self.assertFalse(os.path.exists(self.filename))

class ResizeImageTests(ImageTestCaseMixin, TestCase):
    def test_resize_image(self):
        resize_image(self.file, (48, 48))
        self.assertEqual(get_image_size(self.file), (48, 48))

##########
# using the django test runner to test reusable applications
# runtests.py
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_test(["tests"])
    sys.exit(bool(failures))

###
# tests/test_settings.py
SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
        "tests",
]
##########
# writing own system checks
from django.core.checks import Error, register

@register()
def example_check(app_configs, **kwargs):
    errors = []
    # ...your check logic here
    if check_failed:
        errors.append(
                Error(
                    'an error',
                    hint='A hint.',
                    obj=checked_object,
                    id='myapp.E001',
                )
        )
    return errors

##########
# registering and labeling checks
from django.core.checks import register, Tags

@register(Tags.compatibility)
def my_check(app_configs, **kwargs):
    # ... perform compatibility checks and collect errors
    return errors

###
@register(Tags.security, deploy=True)
def my_check(app_configs, **kwargs):
    ...

###
def my_check(app_configs, **kwargs):
    ...
register(my_check, Tags.security, deploy=True)

##########
# field, model, manager, and database checks
from django.core import checks
from django.db import models

class RangedIntegerField(models.IntegerField):
    def __init__(self, min=None, max=None, **kwargs):
        super().__init__(**kwargs)
        self.min = min
        self.max = max

    def check(self, **kwargs):
        # Call the superclass
        errors = super().check(**kwargs)

        # Do some custom checks and add messages to 'errors':
        errors.extend(self._check_min_max_values(**kwargs))

        # Return all errors and warnings
        return errors

    def _check_min_max_values(self, **kwargs):
        if (self.min is not None and
                self.max is not None and
                self.min > self.max):
            return [
                    checks.Error(
                        'min greater than max.',
                        hint='Decrease min or increase max.',
                        obj=self,
                        id='myapp.E001',
                    )
            ]
        # When no error, return an empty list
        return []

###
class MyModel(models.Model):
    @classmethod
    def check(cls, ** kwargs):
        errors = super().check(**kwargs)
        # ... your own checks ...
        return errors

############
# checks and tests
from django.core.checks import Error
errors = checked_object.check()
expected_errors = [
        Error(
            'an error',
            hint='A hint.',
            obj=checked_object,
            id='myapp.E001',
        )
]
self.assertEqual(errors, expected_errors)

############
# sync to async
from asgiref.sync import sync_to_async

results = await sync_to_async(Blog.objects.get, thread_sensitive=True)(pk=123)

###
from asgiref.sync import sync_to_async

def _get_blog(pk):
    return Blog.objects.select_related('author').get(pk=pk)

get_blog = sync_to_async(_get_blog, thread_sensitive=True)

###########
# asinc adapter function
# async_to_sync()
from asgiref.sync import async_to_sync

async def get_data(...):
    ...
sync_get_data = async_to_sync(get_data)
@async_to_sync
async def get_other_data(...):
    ...

###
# sync_to_async()
from asgiref.sync import sync_to_async

async_function = sync_to_async(sync_function, thread_sensitive=False)
async_function = sync_to_async(sensitive_sync_function, thread_sensitive=True)

@sync_to_async
def sync_function(...):
    ...

#############
# writing custom django-admin command
polls/
    __init__.py
    models.py
    management/
        commands/
            _private.py
            closepoll.py
    tests.py
    views.py

### polls/management/commands/closepoll.py
from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))

###########
class ContextTest(unittest.TestCase):
    def test_against_dictionary(self):
        c1 = Context()
        c1['update'] = 'value'
        self.assertEqual(cq.flatten(), {
            'True': True,
            'None': None,
            'False': False,
            'update': 'value',
        })

###########
