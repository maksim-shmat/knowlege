""" Examples how write models. """

class Sighting(models.Model):
    superhero = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    power = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    sighted_on = models.DateTimeField()

    def __str__(self):
        return "{}'s power {} sighted at: {} on {}".format(
                self.superhero,
                self.power,
                self.location.country,
                self.sighted_on)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('sighting_details', kwargs={'pk': self.id})

    class Meta:
        unique_together = ("superhero", "power")
        ordering = ["-sighted_on"]
        verbose_name = "Sighting & Encounter"
        verbose_name_plural = "Sightings & Encounters"

#############
# This example from django site, it is site-anketa.
from django.db import models

class Question(models.Model):
    """ Make a field for ask a question. """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() -
    datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    """ Make a field for get answer. """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

##########
# after tests he talk change it
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
##########
# from django site
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)  # make a field
    last_name = models.CharField(max_length=30)

#######
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeighKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

##########
# choices field
from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
            ('S', 'Small')
            ('M', 'Medium'),
            ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
# check it in shell
>>> p = Person(name= 'Fred Flinstone', shirt_size="L")
>>> p.save()
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
'Large'

##########
# with classes
from django.db import models

class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices,
            max_length=10)

###########
# ForeighKey, ManyToManyField and OneToOneField require the first argument to
# be a model class
poll = model.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        verbose_name="the related poll",
)
sites = models.ManyToManyField(Site, verbose_name="list of sites")
place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        verbose_name="related place",
)
##########
# Many-to-one relationships
from django.db import models

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...

##########
# Many-to-many relationships
from django.db import models

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)

############
# Many-to-many with extra fields
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

##########
# add metadata
from django.db import models

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"

########
# add custom methods
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Return the person's baby_boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre_boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)

##########
# overriding methods for save
form djnago.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        do_something_else()

#############
# overriding methods prevent saving
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        if self.name == "Yoko Ono's blog":
            return # Yoko shall never have her own blog!
        else:
            super().save(*args, **kwargs) # Call the "real" save() method.

############
# Abstract base class for make one a table in db for all
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True  # Check abstract class

class Student(CommonInfo):    # Inheritance
    home_group = models.CharField(max_length=5)

###
from django.db import models

class CommonInfo(models.Model):
    # ...
    class Meta:
        abstract = True    # inherit from Meta abstract
        ordering = ['nam'] # and add new 

class Student(CommonInfo):
    # ...
    class Meta(CommonInfo.Meta):
        db_table = 'student_info' # add new 

###########
# Need sets abstract=True, else Django set False default
from djaango.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']

class Unmanaged(models.Model):
    class Meta:
        abstract = True
        managed = False

class Student(CommonInfo, Unmanaged):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta, Unmanaged.Meta):
        pass
#############
# Be careful with related_name and related_query_name
from django.db import models

class Base(models.Model):
    m2m = models.ManyToManyField(
            OtherModel,
            related_name="%(app_label)s_%(class)s_related",
            related_query_name="%(app_label)s_%(class)ss",
    )
    
    class Meta:
        abstract = True

    class ChildA(Base):
        pass

    class ChildB(Base):
        pass
# Along with another app rare/models.py:
from common.models import Base

class ChildB(Base):
    pass

##############
# Multi-table inheritance
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    server_hot_dogs = models.BooleanField(default=False)
    server_pizza = models.BooleanField(default=False)

##############
# Proxy model
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MyPerson(Person):
    class Meta:
        proxy = True    # check the proxy

    def do_something(self):
        # ...
        pass

###
class OrderedPerson(Person):
    class Meta:
        ordering = ["last_name"]
        proxy = True

###########
# Proxy model managers
from django.db import models

class NewManager(models.Manager):
    # ...
    pass

class MyPerson(Person):
    objects = NewManager()

    class Meta:
        proxy = True

###########
# Create an abstract class for the new manager.
class ExtraManagers(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True

class MyPerson(Person, ExtraManagers):
    class Meta:
        proxy = True

#######
# Multiple inheritance
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    ...

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    ...

class BookReview(Book, Article):
    pass

#######
# Use a commmon ancestor to hold the AutoField
class Piece(models.Model):
    pass

class Article(Piece):
    article_piece = models.OneToOneField(Piece, on_delete=models.CASCADE,
            parent_link=True)
    ...

class Book(Piece):
    book_piece = models.OneToOneField(Piece, on_delete=models.CASCADE,
            parent_link=True)
    ...

class BookReview(Book, Article):
    pass

##########
Organizing models in a package
To do so, create a models package. Remove models.py and create a myapp/models/
directory with an __init__.py file and the files to store your models. You
most import the models in the __init__.py file.

Explicitly important each model rather than using from .models import * has
the advantages of not cluttering the namespace, making code more readable, 
and keeping code tools useful.

##############
# Interaction with default ordering or order_by()
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=10)
    data = models.IntegerField()

    class Meta:
        ordering = ["name"]

##########
# Custom managers.
# Adding extra manager methods

from django.db import models

class PollManager(models.Manager):
    def with_counts(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT p.id, p.question, p.poll_date, COUNT(*)
            FROM polls_opinionpoll p, polls_response r
            WHERE p.id = r.poll_id
            GROUP BY p.id, p.question, p.poll_date
            ORDER BY p.poll_date DESC""")
        result_list = []
        for row in cursor.fetchall():
            p = self.model(id=row[0], question=row[1], poll_date=row[2])
            p.num_responses = row[3]
            result_list.append(p)
    return result_list

class OpinionPoll(models.Model):
    question = models.CharField(max_length=200)
    poll_date = models.DateField()
    objects = PollManager()

class Response(models.Model):
    poll = models.ForeignKey(OpinionPoll, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=50)
    response = models.TextField()

###########
# Modifying managers's initial QuerySet
# A Mangager's base QuerySet returns all objects in the system.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

# the following model has two Managers - one that returns all objects, and
# one that returns only the books by Roald Dahl

# First, define the Manager subclass.
class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author='Roald Dahl')

# Then hook it into the Book model explicitly.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    objects = models.Manager()  # The default manager.
    dahl_objects = DahlBookManager()  # The Dahl-specific manager.

############
# Using multiple managers on the same model

class AuthorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='A')

class EditorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='E')

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=[('A', _('Author')), ('E',
        _('Editor'))])
    people = models.Manager()
    authors = AuthorManager()
    editors = EditorManager()

##############
# Calling custom QuerySet methods from the manager

class PersonQuerySet(models.QuerySet):
    def authors(self):
        return self.filter(role='A')

    def editors(self):
        return self.filter(role='E')

class PersonManager(models.Manager):
    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)

    def authors(self):
        return self.get_queryset().authors()

    def editors(self):
        return self.get_queryset().editors()

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=[('A', _('Author')), ('E',
        _('Editor'))])
    people = PersonManager()

##############
# Creating a manager with QuerySet methods

class CustomQuerySet(models.QuerySet):
    # Available on both Manager and QuerySet.
    def public_method(self):
        return

    # Available only on QuerySet
    def _private_method(self):
        return

    # Available only on QuerySet.
    def opted_out_public_method(self):
        return
    opted_out_public_method.queryset_only = True

    # Available on both Manager and QuerySet.
    def _opted_in_private_method(self):
        return
    _opted_in_private_method.queryset_only = False

##############
# from_queryset()
class CustomManager(models.Manager):
    def manager_only_method(self):
        return

class CustomQuerySet(models.QuerySet):
    def manager_and_queryset_method(self):
        return

class MyModel(models.Model):
    objects = CustomManager.from_queryset(CustomQuerySet)()

# You may also store the generated class into a variable
MyManager = CustomManager.from_queryset(CustomQuerySet)
class MyModel(models.Model):
    objects = MyManager()

#############
# Custom managers and model inheritance

class AbstractBase(models.Model):
    # ...
    objects = CustomManager()

    class Meta:
        abstract = True

class ChildA(AbstractBase):
    # ...
    # This class has CustomManager as the default manager.
    pass

class ChildB(AbstractBase):
    # ...
    # An explicit default manager.
    default_manager = OtherManager()

class ExtraManager(models.Model):
    extra_manager = OtherManager()

    class Meta:
        abstract = True

class ChildC(AbstractBase, ExtraManager):
    # ...
    # Default manager is CustomManager, but OtherManager is
    # also available via the "extra_manager" attribute.
    pass

###########
# Executing custom SQL directly

from django.db import connection

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()
    return row

# To protect against SQL injection, you must not include quotes around the %s
# placeholders in the SQL string. Note that if you want to include literal
# percent signs in the query, you have to double them in the case you are
# passing parameters:
cursor.execute("SELECT foo FROM bar WHERE baz = '30%'")
cursor.execute("SELECT foo FROM bar WHERE baz = '30%%' AND id = %s", [self.id])

#########
# Generic views of objects
# models.py
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_lenght=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    salution = model.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeighKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

### And view.py
from django.views.generic import ListView
from books.models import Publisher

class PublisherList(ListView):
    model = Publisher

### And urls.py
from django.urls import path
from books.views import PublisherList

urlpatterns = [
        path('publishers/', PublisherList.as_view()),
]
##########
# Performing extra work
# models.py
from django.db import models

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')
    last_accessed = model.DateTimeField()
###
from django.urls import path
from books.views import AuthorDetailView

urlpatterns = [
        #...
        path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]
###
from django.utils import timezone
from django.views.generic import DetailView
from books.models import Author

class AuthorDetailView(DetailView):
    queryset = Author.objects.all()

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj
#########
# Useing files in models
from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars')

##############
# The built-in filesystem storage class
from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage(location='/media/photos')

class Car(models.Model):
    ...
    photo = models.ImageField(storage=fs)
##########


