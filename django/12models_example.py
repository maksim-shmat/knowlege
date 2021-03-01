""" About models django."""

# Making queries
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Autor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

##############
# Querying JSONField
from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name

##########
# One-to-one relationships

class EntryDetail(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)
    details = models.TextField()

ed = EntryDetail.objects.get(id=2)
ed.entry  # Returns the related Entry object.

###########
# Aggregation

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Publisher(models.Model):
    name = models.CharField(max_length=300)

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

##########
# Using routers
class AuthRouter:
    """
    A router to control all database operations on models in the auth and
    contenttypes applications.
    """
    route_app_labels = {'auth', 'contenttypes'}
    
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'auth_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'auth_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contnttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'auth_db'
        return None

#############
# And we also want a router that sends all other apps to the primary/replica
# configuration, and randomly chooses a replica to read from:

import random

class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen replica.
        """
        return reandom.choice(['replica1', 'replica2'])

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        return 'primary'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_set = {'primary', 'replica1', 'replica2'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True

############
# Tablespaces
class TablespaceExample(model.Model):
    name = models.CharField(max_length=30, db_index=True,
db_tablespace="indexes")
    data = models.CharField(max_length=30, db_index=True)
    shortcut = models.CharField(max_length=7)
    edges = models.ManyToManyField(to="self", db_tablespace="indexes")

    class Meta:
        db_tablespace = "tables"
        indexes = [models.Index(field=['shortcut'],
db_tablespace='other_indexes')]

############
# Query logger
import time

class QueryLogger:
    def __init__(self):
        self.queries = []

    def __call__(self, execute, sql, params, many, context):
        current_query = {'sql': sql, 'params': params, 'many': many}
        start = time.monotonic()
        try:
            result = execute(sql, params, many, context)
        except Exception as e:
            current_query['status'] = 'error'
            current_query['exception'] = e
            raise
        else:
            current_query['status'] = 'ok'
            return result
        finally:
            duration = time.monotonic() - start
            current_query['duration'] = duration
            self.queries.append(current_query)

###
# To use this, you would create a logger object and install it as a wrapper.
from django.db import connection

ql = QueryLogger()
with connection.execute_wrapper(ql):
    do_queries()
# Now we can print the log.
print(ql.queries)

#############
# Many-to-many relationships

from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline

###########
# Many-to-one realationships

from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Articlt(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']

###########
# One-to-one relationships

from django.db import models

class Place(models.Model):
    name = model.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name

class Restaurant(model.Model):
    place = models.OneToOneField(
            Place,
            on_delete=models.CASCADE,
            primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)

#############
# Set of models for example.
from django.db import models
from django.forms import ModelForm

TITLE_CHOICES = [
        ('MR', 'Mr.'),
        ('MRS', 'Mrs.'),
        ('MS', 'Ms.'),
]

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        field = ['name', 'title', 'birth_date']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']

# And this go to form
from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField(
            max_length=3,
            widget=forms.Select(choices=TITLE_CHOICES),
    )
    birth_date = forms.DateField(required=False)

class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

##########
# Model forms
# models.py
from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.Model):
        name = models.CharField(max_length=200)

        def get_absolute_url(self):
            return reverse('author-detail', kwargs={'pk': self.pk})
# views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from myapp.models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = ['nam']

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
###
# urls.py
from django.urls import path
from myapp.views import AuthorCreate, AuthorDelete, AuthorUpdate

urlpatterns = [
        # ...
        path('author/add/', AuthorCreate.as_view(), name='author-add'),
        path('author/<int:pk>/', AuthorUpdate.as_view(), name='author-update'),
        path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
]
##########
# Models and request.user
# models.py
from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeighKey(User, on_delete=models.CASCADE)
    #...
###
# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    field = ['name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
#############
# writing custom model fields
class Hand:
    """A hand of cards (bridge style)"""

    def __init__(self, north, east, south, west):
        # Input parameters are lists of cards ('Ah', '9s', etc.)
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    # ... (other possibly useful methods omitted) ...

###
example = MyModel.objects.get(pk=1)
print(example.hand.north)

new_hand = Hand(north, east, south, west)
example.hand = new_hand
example.save()

#############
# writing a field subclass
from django.db import models

class HandField(models.Field):
    description = "A hand of cards (bridge style)"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 104
        super().__init__(*args, **kwargs)

### field deconstruction
from django.db import models

class HandFiled(models.Field):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 104
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

###
from django.db import models

class CommaSepField(models.Field):
    "Implements comma-separated storage of lists"

    def __init__(self, separator=",", *args, **kwargs):
        self.separator = separator
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # Only include kwargs if it's not the default
        if self.separator != ",":
            kwargs['separator'] = self.separator
        return name, path, args, kwargs

############ model field reference
# choices
from django.db import models

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
            (FRESHMAN, 'Freshman'),
            (SOPHOMORE, 'Sophomore'),
            (JUNIOR, 'Junior'),
            (SENIOR, 'Senior'),
            (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
            max_length=2,
            choices=YEAR_IN_SCHOOL_CHOICES,
            default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}

######### enumerated types
from django.urils.translation import gettext_lazy as _

class Student(models.Model):

    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR', _('Freshman')
        SOPHOMORE = 'SO', _('Sophomore')
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')
        GRADUATE = 'GR', _('Graduate')

    year_in_school = models.CharField(
            max_length=2,
            choices=YearInSchool.choices,
            default=YearInSchool.FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {
                self.YearInSchool.JUNIOR,
                self.YearInSchool.SENIOR,
        }

############ IntegerChoices class
class Card(models.Model):

    class Suit(models.IntegerChoices):
        DIAMOND = 1
        SPADE = 2
        HEART = 3
        CLUB = 4

    suit = models.IntegerField(choices=Suit.choices)

###
class MoonLandings(datetime.date, models.Choices):
    APOLLO_11 = 1969, 7, 20, 'Apollo 11 (Eagle)'
    APOLLO_12 = 1969, 11, 19, 'Apollo 12 (Intrepid)'
    APOLLO_13 = 1971, 2, 5, 'Apollo 14 (Antares)'
    APOLLO_15 = 1971, 7, 30, 'Apollo 15 (Falcon)'
    APOLLO_16 = 1972, 4, 21, 'Apollo 16 (Orion)'
    APOLLO_17 = 1972, 12, 11, 'Apollo 17 (Challenger)'

###
class Answer(models.IntegerChoices):
    NO = 0, _('No')
    YES = 1, _('Yes')

    __empty__ = _('(Unknown)')

############### Field types: FileField
class MyModel(models.Model):
    # file will be upload to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='uploads/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

###
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)

############## Field.default
def contact_default():
    return {"email": "to1@example.com"}

contact_info = JSONField("ContactInfo", default=contact_default)

### FilePathField
import os
from django.conf import settings
from django.db import models

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class MyModel(models.Model):
    file = models.FilePathField(path=images_path)

############ indexes define on th model
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        indexes = [
                models.Index(fields=['last_name', 'first_name']),
                models.Index(fields=['first_name'], name='first_name_idx'),
        ]

############ constraints to define on the model
from django.db import models

class Customer(models.Model):
    age = models.IntegerField()

    class Meta:
        constraints = [
                models.CheckConstraint(check=models.Q(age__gte=18),
name='age_gte_18'),
        ]

################ rather than overriding __init__
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        # do something with the book
        return book

    book = Book.create("Pride and Prejudice")

###
class BookManager(models.Manager):
    def create_book(self, title):
        book = self.create(title=title)
        # do something with the book
        return book

class Book(bodels.Model):
    title = models.CharField(max_length=100)

    objects = BookManager()

book = Book.objects.create_book("Pride and Prejudice")

############ customizing model loading
from django.db.models import DEFERRED

@classmethod
def from_db(cls, db, field_names, values):
    # Default implementation of from_db() (subject to change and could
    # be replaced with super()).
    if len(values) != len(cls._meta.concrete_fields):
        values.reverse()
        values = [
                values.pop() if f.attname in field_names else DEFERRED
                for f in cls._meta.concrete_fields
        ]
    instance = cls(*values)
    instance._state.adding = False
    instance._state.db = db
    # customization to store the original field values on the instance
    instance._loaded_values = dict(zip(field_names, values))
    return instance

def save(self, *args, **kwargs):
    # Check how the current values differ from ._loaded_values. For example,
    # prevent changing the creator_id of the model. (This example doesn't
    # support cases where 'creator_id' is deferred).
    if not self._state.adding and(
            self.creator_id != self._loaded_values['creator_id']):
        raise ValueError("Updating the value of creator isn't allowed")
    super().save(*args, **kwargs)

############ refreshing objects from database
def test_update_result(self):
    obj = MyModel.objects.create(val=1)
    MyModel.objects.filter(pk=obj.pk).update(val=F('val') + 1)
    # At this point obj.val is still 1, but the value in the database
    # was updated to 2. The objectc's updated value needs to be reloaded
    # from the database.
    obj.refresh_from_db()
    self.assertEqual(obj.val, 2)

###
class ExampleModel(models.Model):
    def refresh_from_db(self, using=None, fields=None, **kwargs):
        # fields contains the name of the deferred field to be
        # loaded.
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            # If any deferred field is going to be loaded
            if fields.intersection(deferred_fields):
                # then load all of them
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

############ validating objects
from django.core.exception import ValidationError
try:
    article.full_clean()
except ValidationError as e:
    # Do something based on the errors contained in e.message_dict.
    # Display them to a user, or handle them programmatically.
    pass

### Model.clean()
import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    ...
    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError(_('Draft entries may not have a publication
            date.'))
            # Set the pub_date for published items if it hasn't been set already.
            if self.status == 'published' and self.pub_date is None:
                self.pub_date = datetime.date.today()

### 
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
try:
    article.full_clean()
except ValidationError as e:
    non_field_errors = e.message_dict[NON_FIELD_ERRORS]

###
class Article(models.Model):
    ...
    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError({'pub_date': _('Draft entries may not have a
            publication date.')})
            ...

###
raise ValidationError({
    'title': ValidationError(_('Missing title.'), code='required'),
    'pub_date': ValidationError(_('Invalid date.'), code='invalid'),
})

###
class Article(models.Model):
    ...
    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if self.status == 'draft' and self.pub_date is not None:
            if exlude and 'status' in exlude:
                raise ValidationError(
                        _('Draft entries may not have a publication date.')
                )
            else:
                raise ValidationError({
                    'status': _(
                        'Set status to draft if there is not a '
                        'publication date.'
                    ),
                })

############ __str__()
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

### __eq__()
from django.db import models

class MyModel(models.Model):
    id = models.AutoField(primary_key=True)


class MyProxyModel(MyModel):
    class Meta:
        proxy = True

class MultitableInherited(MyModel):
    pass

# Primary keys compared
MyModel(id=1) == MyModel(id=1)
MyModel(id=1) != MyModel(id=2)
# Primary keys are None
MyModel(id=None) != MyModel(id=None)
# Same instance
instance = MyModel(id=None)
instance == instance
# Proxy model
MyModel(id=1) == MyProxyModel(id=1)
# Multi-table inheritance
MyModel(id=1) != MultitableInherited(id=1)

############ Django model class definition in models.py

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class Store(models.Model):
    #id = models.AutoField(primary_key=True)  # Added by default, not required explicitly
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    #objects = models.Manager()  # Added by default, to required explicitly
    def __str__(self):
        return "%s (%s,%s)" % (self.name, self.city, self.state)

###### Django model default option use

def default_city():
    return "San Diego"

clss Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30,default=default_city)
    state = models.CharField(max_length=2,default='CA')

###### Django model default options for dates and times, as well as auto_now and auto_now_add use

from datetime import date
from django.utils import timezone

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    date = models.DateField(default=date.today)
    datetime = models.DateTimeField(default=timezone.now)
    date_lastupdated = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)

###### Django model choices option
ITEM_SIZES = (
             ('S','Small'),
             ('M','Medium'),
             ('L','Large'),
             ('P','Portion'),
             )

class Menu(models.Model):
    name = models.CharField(max_length=30)

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    size = models.CharField(choices=ITEM_SIZES,max_length=1)

###### Django model help_text option

ITEM_SIZES = (
             ('S','Small'),
             ('M','Medium'),
             ('L','Large'),
             ('P','Portion'),
             )

class Menu(models.Model):
    name = models.CharField(max_length=30)

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    discription = models.CharField(max_length=100,help_text="Ensure youprovide some description of the ingredients")
    size = models.CharField(choices=ITEM_SIZES,max_length=1)
    calories = models.IntegerField(help_text="Calorie count should reflect <b>size</b> of the item")

###### Django model field validators option with built-in and custom validator

ITEM_SIZES = (
             ('S','Small'),
             ('M','Medium'),
             ('L','Large'),
             ('P','Portion'),
             )

# Import built-in validator
from django.core.validators import MinLengthValidator

# Create custom validator
from django.core.exceptions import ValidationError

def calorie_watcher(value):
    if value > 5000:
        raise ValidationError(
                ('Whoa! calories are %(value)s ? We try to serve healthy food, try something less than 5000!'),
                parama={'value': value},
        )
    if value < 0:
        raise ValidationError(
                ('Strange calories are %(value)s ? This can\'t be, value must be greater than 0'),
                params={'value': value},
        )


class Menu(models.Model):
    name = models.CharField(max_length=30)


class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,validators=[MinLengthValidator(5)])
    description = models.CharField(max_length=100)
    size = models.CharField(choices=ITEM_SIZES,max_length=1)
    calories = models.IntegerField(validators=[calorie_watcher])

###### Django model use of the save() method

# Import Django model class
from coffeehouse.stores.models import Store

# Create a model Store instance
store_corporate = Store(name='Corporate',address='624 Broadway',city='San Diego',state='CA',email='corporate@coffeehouse.com')

#Invoke the save() method to create/save the record
# No record id reference, so a create operation is made and the reference is updated with id store_corporate.save()

# Change field on instance
store_corporate.city='625 Broadway'

# Invoke the save() method to update/save the record
# Record has id reference from prior save() call, so operation is update store_corporate.save()

######
