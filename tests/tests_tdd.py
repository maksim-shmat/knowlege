""" Tests work. """

Процесс TDD имеет много общего с научным методом, который
основа современной науки. В научном методе важно
сначала сформулируйте гипотезу, соберите данные, а затем проведите эксперименты, которые
повторяются и поддаются проверке, чтобы подтвердить или опровергнуть вашу гипотезу.
Я рекомендую попробовать TDD, когда вы научитесь писать
тесты для ваших проектов. Новичкам может быть сложно составить контрольный пример
это проверяет, как должен вести себя код. По тем же причинам я не буду
предложить TDD для исследовательского программирования.

# tests.py
from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import HomeView
class HomePageOpenTestCase(TestCase):   # speaking name
    def test_home_page_resolves(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__,
                         HomeView.as_view().__name__)
# start a test
$ ./manage.py test app1
Creating test database for alias 'default'...
-------------
Ran 1 rest in 0.088s
OK
Destroying test database for alias 'default'...

библиотека unittest Python 3 предоставляет более 32 утверждений.
методы. Django расширяет его более чем на 19 утверждений для конкретных фреймворков.

Не (повторно) тестируйте фреймворк: Django хорошо протестирован. Не проверяйте
Поиск URL, рендеринг шаблонов и другие связанные с фреймворком
функциональные возможности.
Не тестировать детали реализации: протестируйте интерфейс и оставьте
мелкие детали реализации. Это упрощает дальнейший рефакторинг без нарушения тестов.
Больше всего тестируйте моделей, меньше всего шаблонов: в шаблонах должно быть меньше всего
бизнес-логика, и они меняются чаще.
Избегайте проверки вывода HTML: тестовые представления используют свой контекст
вывод переменной, а не вывод в формате HTML.
Избегайте использования клиента веб-тестирования в модульных тестах: клиенты веб-тестирования вызывают
несколько компонентов и поэтому лучше подходят для интеграции
тесты.
Избегайте взаимодействия с внешними системами: если возможно, поиздевайтесь над ними.
База данных является исключением, поскольку тестовая база данных находится в памяти и
довольно быстро.

# Mocking
# profiles/tests.py
from django.test import TestCase
from unittest.mock import patch
from django.contrib.auth.models import User

class TestSuperHeroCheck(TestCase):
    def test_checks_superhero_service_obj(self):
        with patch("profiles.models.SuperHeroWebAPI") as ws:
            ws.is_hero.return_value = True
            u = User.objects.create_user(username="t")
            r = u.profile.is_superhero()
        ws.is_hero.assert_called_with('t')
        self.assertTrue(r)

##########
# use fixtures is anti-pattern

from django.test import TestCase

class PostTestCase(TestCase):
    fixtures = ['posts']

    def setUp(self):
        # Create additional common objects
        pass

    def test_some_post_functionality(self):
        # By now fixtures and setUp() objects are loaded
        pass

# use factory better

from django.test import TestCase
from .models import Post

class PostFactory:
    def make_post(self):
        return Post.objects.create(message="")

class PostTestCase(TestCase):
    def setUp(self):
        self.blank_message = PostFactory().makePost()

    def test_some_post_functionality(self):
        pass

#######
# rewrite
import factory
from django.test import TestCase
from .models import Post

class PostFactory(factory.Factory):
    class Meta:
        model = Post
    message = ""

class PostTestCase(TestCase):
    def setUp(self):
        self.blank_message = PostFactory.create()
        self.silly_message = PostFactory.create(message="silly")

    def test_post_title_was_set(self):
        self.assertEqual(self.blank_message.message, "")
        self.assertEqual(self.silly_message.message, "silly")


