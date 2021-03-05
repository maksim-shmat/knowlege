""" About django's models."""

####### Django model use of validation clean_unique() method with Meta unique_together

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30,unique=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    email = models.EmailField()
    class Meta:
        unique_together = ("name", "email")

# Create instance to show use of validate_unique() via Meta option
store_downtown_horton = Store(name='Downtown', address'Horton Plaza',
                              city='San Diego', state='CA',
                              email='downtown@coffeehouse.com')

# Save instance to show use of validate_unique() via Meta option
store_downtown_horton = Store(name='Downtown',address'Horton Plaza',
                              city='San Diego', state='CA',
                              email='downtown@coffeehouse.com')

# Save instance to DB
store_downtown_horton.save()

# Create additional instance that violated unique_together rule in Metaclass
store_downtown_fv = Store(name='Downtown',address'Fashion Valley',
                          city='San Diego',state='CA',
                          email='downtown@coffeehouse.com')

# You could call save() and let the database reject the instance but let use validate_unique
store_downtown_fv.validate_unique()
Traceback (most recent call last):
    ValidationError: {'__all__': [u'Store with this Name and Email already exists.']}

###### Django model with custom method

class Store(model.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)

    def latitude_longitude(self):
        # Call remote service to get latitude & longitude
        latitude, longitude = geocoding_method(self.address, self.city,self.state)
        return latitude, longitude

###### Django default model manager renamed

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    mgr = models.Manager()

###### Django model with meta class and index option

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)

    class Meta:
        indexes = [
                models.Index(fields=['city','state']),
                models.Index(fields=['city'],name='city_idx')
        ]

###### Django model abstract option

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    class Meta:
        abstract = True

class Drink(Item):
    mililiters = models.IntegerField()

###### One to many Django model relationship

from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=30)

class Item(models.Model):
    menu = models.ForeignKey(Menu)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

###### Many to many Django model relationship

from django.db import models

class Amenity(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    email = models.EmailField()
    amenities = models.ManyToManyField(Amenity,blank=True)

###### One to one Django models relationship

from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=30)

class Item(models.Model):
    menu = models.ForeignKey(Menu)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    calories = models.IntegerField()
    price = models.FloatField()

class Drink(models.Model):
    item = models.OneToField(Item,on_delete=models.CASCADE,primary_key=True)
    caffeine = models.IntegerField()

###### One to many Django model relationship with self-referencing model

from django.db import models

class Category(models.Model):
    menu = models.ForeignKey('self')

class Person(models.Model):
    relatives = models.ManyToManyField('self')

###### One to many Django model relationship with reverse relationship references

from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=30)

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_lenght=100)
    price = models.FloatField(blank=True,null=True)

breakfast = Menu.objects.get(name='Breakfast')
# Direct access
all_items_with_breakfast_menu = Item.objects.filter(menu=breakfast)

# Reverse access through instance
same_all_items_with_breakfast_menu = breakfast.item_set.all()

### One to many Django model relationship with reverse relationship queries
# Direct access, Item records with price higher than 1
Item.objects.filter(price__gt=1)

# Reverse access query, Menu records with Item price higher than 1
Menu.objects.filter(item__price__gt=1)

###### Selectively activate and deactivate atomic requests with @non_atomic_requests and @ atomic 

from django.db import transaction

# When ATOMIC_REQUESTS=True you can individually disable atomic requests
@transaction.non_atomic_requests
def index(request):
    # Data operations with transactions commit/rollback individually
    # Failure of one operation does not influence other
    data_operation_1()
    data_operation_2()
    data_operation_3()

# When ATOMIC_REQUESTS=True you can individually disable atomic requests

@transaction.atomic
def detail(request):
    # Start transaction.
    # Failure of any operation, rollbacks other operations
    data_operation_1()
    data_operation_2()
    data_operation_3()
    # Commit transaction if all operation successful

###### Transactions with context managers

from django.db import transaction

def login(request):
    # With AUTO_COMMIT=True and ATOMIC_REQUEST=False
    # Data operation runs in its own transaction due to AUTO_COMMIT=True
    data_operation_standalone()

    # Open new transaction with context manager
    with transaction.atomic():
        # Start transaction.
        # Failure of any operation, rollbacks other operations

        data_operation_1()
        data_operation_2()
        data_operation_3()
        # Commit transaction if all operation successful

    # Data operation runs in its own transaction due to AUTO_COMMIT=True
    data_operation_standalone2()

###### Load initial data with hard_coded data in Django migration file
# _*_ coding: utf-8 _*_

from __future__ import unicode_literals
from django.db import models, migrations

def load_stores(apps, schema_editor):
    Store = apps.get_model("stores", "Store")
    store_corporate = Store(id=0,name='Corporate',
                            address='624 Broadway',
                            city='San Diego',
                            state='CA',
                            email='corporate@coffeehouse.com')
    stote_corporate.save()
    store_downtown = Store(id=1,name='Downtown',
                           address='Horton Plaza',
                           city='San Diego',
                           state='CA',
                           email='downtown@coffeehouse.com')
    store_downtown.save()
    store_uptown = Store(id=2,name='Uptown',
                         address='1240 University Ave',
                         city='San Diego',
                         state='CA',
                         email='midtown@coffeehouse.com')
    stote_uptown.save()
    store_midtown = Store(id=3,name='Midtown',
                          address='784 W Washington St',
                          city='San Diego',
                          state='CA',
                          email='midtown@coffeehouse.com')
    store_midtown.save()

def delete_stores(apps, schema_editor):
    Store = apps.get_model("stores", "Store")
    Store.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
            ('stores', '0001_initial'),
    ]

    operations = [
            migrations.RunPython(load_stores,delete_stores)<
    ]

###### load initial data with SQL script in Django migration file

from __future__ import unicode_literals
from django.db import models, migrations

def load_stores_from_sql():
    from coffeehouse.settings import PROJECT_DIR
    import os
    sql_statements = open(os.path.join(PROJECT_DIR,'stores/sql/store.sql'), 'r').read()
    return sql_statements

def delete_stores_with_sql():
    return 'DELETE from stores_store;'

class Migration(migrations.Migration):

    dependencies = [
            ('stores', '0001_initial'),
    ]

    operations = [
            migrations.RunSQL(load_stores_from_sql(), delete_stores_with_sql()),
    ]

###### Django fixture file with JSON structure
[{
    "fields": {
        "city": "San Diego",
        "state": "CA",
        "email": "corporate@coffeehouse.com",
        "name": "Corporate",
        "address": "624 Broadway"
    },
    "model": "stores.store",
    "pk": 0
},
{
    "fields": {
        "city": "San Diego",
        "state": "CA",
        "email": "downtown@coffeehouse.com",
        "name": "Downtown",
        "address": "Horton Plaza"
    },
    "model": "stores.store",
    "pk":1
}]

###### Load initial data from Django fixture file in Django migration file

from __future__ import unicode_litereals
from django.db import models, migrations

def load_stores_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "store")

def delete_stores(apps, schema_editor):
    Store = apps.get_model("stores", "Store")
    Store.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
            ('stores', '0001_initial'),
    ]

    operations = [
            migrations.RunPython(load_stores_from_fixture,delete_stores),
    ]

###### Basic syntax to listen for Django signals

from django.dispath import receiver

@receiver(<signal_to_listen_for_from_django_core_signals>,sender=<model_class_to_listen_to>)
def method_with_logic_to_run_when_signal_is_emitted(sender, **kwargs):
    # Logic when signal is emitted
    # Access sender & kwargs to get info on medel that emitted signal

###### Listen for Django pre_save signal on Item model in signals.py

from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.dispatch import receiver
import logging

stdlogger = logging.getLogger(__name__)

@receiver(pre_save, sender='items.Item')
def run_before_saving(sender, **kwargs):
    stdlogger.info("Start pre_save Item in signals.py under items app")
    stdlogger.info("sender %s" % (sender))
    stdlogger.indo("kwargs %s" % str(kwargs))

###### Emit custom signals in Django Model Signals

from django.dispatch import Signal

order_complete = Signal(providing_args=["customer","barista"])

store_closed = Signal(providing_args=["employee"])

### Django model emitting custom signal

from django.db import models
from coffeehouse.stores.signals import store_closed

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30,unique=True)
    ...
    def closing(self,employee):
        store_closed.send(sender=self.__class__, employee=employee)

###
@receiver(store_closed)
def run_when_store_is_closed(sender,**kwargs):
    stdlogger.info("Start store_closed Store in signals.py under storesapp")
    stdlogger.info("sender %s" % (sender))
    stdlogger.info("kwargs %s" % str(kwargs))

###### Django database router to store core app models in devops database and all other models in default database

class DatabaseForDevOps(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label in ['auth','admin','session','contenttypes']:
            return 'devops'
        # Returning None is no opinion, defer to other routers or default database
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ['auth','admin','sessions','contenttypes']:
            return 'devops'
        # Returning None is no opinion, defer to other routers of default database
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations between two models that are both Django core app models
        if obj1._meta.app_label in ['auth','admin','sessions','contenttypes'] and obj2._meta.app_label in ['auth','admin','sessions','contenttypes']:
            return True
        # If neither object is in a Django core app model (defer to other routers or default database)
    elif obj1._meta.app_label not in ['auth','admin','sessions','contenttypes'] or obj2._meta.app_label not in ['auth','admin','sessions','contenttypes']:
        return None
    return None

def allow_migrate(self, db, app_label, model_name=None, **hints):
    if db == 'devops':
        # Migrate Django core app models if current database is devops
        if app_label in ['auth','admin','sessions','contenttypes']:
            return True
        else:
            # Non Django core app models should not be migrated if database is devops
            return False
    # Other database should not migrate Django core app models
    elif app_label in ['auth','admin','sessions','contenttypes']:
        return False
    # Otherwise no opinion, defer to other routers or default database
    return None

###### Crate a single record with model save() method
# Import Django model class

from coffeehouse.stores.models import Store

# Create a model Store instance
store_corporate = Store(name='Corporate',address='624 Broadway',state='CA',email='corporate@coffeehouse.com')
# Assign attribute value to instance with Python dotted notation
store_corporate.city = 'San Diego'
# Invoke the save() method to create the record
store_corporate.save() # If successful, record reference has id
store_corporate.id

###### Create a single record with create() method
# Import Django model class

from coffeehouse.stores.models import Store

# Create a model Store instance which is saved automatically
store_corporate = Store.objects.create(name='Corporate',address='624 Broadway',city='San Diego',state='CA',email='corporate@coffeehouse') # Ifsuccessful, record reference has id
store_corporate.id

###### Read model record with get() method
# Import Django model class

from coffeehouse.stores.models import Store

# Get the store with the name "Downtown" or equivalent SQL: 'SELECT...WHERE
name = "Downtown"
downtown_store = Store.objects.get(name="Downtown")

# Define uptown_email for the query
uptown_email = "uptown@coffeehouse.com"
# Get the store with the email value uptow_email or equivalent SQL: 'SELECT...WHERE
email = "uptown@coffeehouse.com"
uptown_email_store = Store.objects.get(email=uptown_email)

# Once the get() method runs, you can access an object's attributes
# either in logging statements, functions of templates
downtown_store.address
downtown_store.email

# Note you can access the object without attributes.
# If the Django model has a __str__ method definition, the output is based on this method
# If the Django model has no __str__ method definition, the output is just <object>
print(uptown_email_store)

###### Read or create model record with get_or_create() method
# Import Django model class

from coffeehouse.items.models import Menu

# Get or create a menu instance with name="Breakfast"
menu_target, created = Menu.objects.get_or_create(name="Breakfast")

###### Replicate get_or_create() method with explicit try/except block and save method

from django.core.exceptions import ObjectDoesExist
from coffeehouse.items.models import Menu

try:
    menu_target = Menu.objects.get(name="Dinner")
    # If get() throws an error you need to handle it.
    # You can use either the generic ObjectDoesNotExist or
    # <model>.DoesNotExist which inherits from
    # django.core.exceptions.ObjectDoesNotExist, so you can target multiple
    # DoesNotExist: # or the generic "exception ObjectDoesNotExist:"
    menu_target = Menu(name="Dinner")
    menu_target.save()

###### Update model record with the save() method
# Import Django model class

from coffeehouse.stores.models import Store

# Get the store with the name "Downtown" or equivalent SQL: 'SELECT...WHERE name = "Downtown"

downtown_store = Store.objects.get(name="Downtown")

# Update the name value
downtown_store.name = "Downtown (Madison)"

# Call save() with the update_fields arg and a list of record fields to update selectively
downtown_store.save(update_fields=['nam'])

# Or you can call save() without any argument and all record fields are updated downtown_store.save()

###### Update model record with the update() method

from coffeehouse.stores.models import Store

Store.objects.filter(id=1).update(name="Downtown (Madison)")

from coffeehouse.items.models import Item
from django.db.models import f
Item.objects.filter(id=3).update(stock=F('stock') +100)

###### Update or create model record with the update_or_create() method
# Import Django model class

from coffeehouse.stores.models import Store

values_to_update = {'email': 'downtown@coffeehouse.com'}

# Update  for record with name='Downtown' and city='San Diego' is found, otherwise create record
obj_store, created = Store.objects.update_or_create(
        name='Downtown',city='San Diego', defaults=value_to_update)

####### Update model record from database with the refresh_from_db() method

from coffeehouse.stores.models import Store

store_corporate = Store.objects.get(id=1)
store_corporate.name = 'Not sure about this name'

# Update from db again
store_corporate.refresh_from_db() # Model record name now reflects value in database again
store_corporate.name

# Multiple edits
store_corporate.name = 'New store name'
store_corporate.email = 'newemail@coffeehouse.com' store_corporate.address = 'To be confirmed'

# Update from db again, but only address field
# so store name and email remain with local values
store_corporate.refresh_from_db(fields=['address'])

###### Delete model record with the delete() method
# Import Django model class

from coffeehouse.stores.models import Store

# Get the store with the name "Downtown" or equivalent SQL: 'SELECT...WHERE
name = "Downtown"

downtown_store = Store.objects.get(name="Downtown")
# Call delete() to delete the record in the database
downtown_store.delete()

###### Delete model record with the delete() method on query

from coffeehouse.items.models import Menu

Menu.objects.filter(id=1).delete()

###### Create multiple records of a Django model with the bulk_create() method
# Import Django model class

from coffeehouse.stores.models import Store

# Create model Store instances
store_corporate = Store(name='Corporate',address='624 Broadway',city='San Diego',state='CA',email='corporate@coffeehouse.com')
store_downtown = Store(name='Downtown',address='Horton Plaza',city='San Diego',state='CA',email='downtown@coffeehouse.com')
store_uptown = Store(name='Uptown',address='240 University Ave',city='San Diego',state='CA',email='uptown@coffeehouse.com')
store_midtown = Store(name='Midtown',address='784 W Washington St',city='San Diego',state='CA',email='midtown@coffeehouse.com')

# Create store list
store_list = [store_corporate,store_downtown,store_uptown,store_midtown]

# Call bulk_create to create records in a single call
Store.objects.bulk_create(store_list)

### Create multiple records with the save() method
# Loop over each store and invoke save() on each entry # save() method called on each list member to create record

for store in store_list:
    store.save()

###### Create multiple records with save() method in a single transaction
# Import Django model and transaction class

from coffeehouse.stores.models import Store
from django.db import transaction

first_store_list = [store_corporate,store_downtown]
second_store_list = [store_uptown,store_midtown]

# Trigger atomic transaction so long is executed in a single transaction with transaction.atomic():
    # Loop over each store and invoke save() on each entry
    for store in first_store_list:
        # save() method called on each member to create record
        store.save()

# Mithod decorated with @transaction.atomic to ensure logic is executed in single transaction
@transaction.atomic
def bulk_store_creator(store_list):
    # Loop over each store and invoke save() on each entry
    for store in store_list:
        # save() method called on each member to create record
        store.save()

# Call bulk_store_creator with Store list
bulk_store_creator(second_store_list)

###### Read multiple records with all(), filter(), and exlude() methods
# Import Django model class

from coffehouse.stores.models import Store

# Query with all() method or equivalent SQL: 'SELECT * FROM ...'
all_stores = Store.objects.all()

# Query with include() method or equivalent SQL: 'SELECT...WHERE city = "San Diego"'
san_diego_stores = Store.objects.filter(city='San Diego')

# Query with exlude() method or equivalent SQL: 'SELECT...WHERE NOT (city = "San Diego")'
non_san_diego_stores = Store.objects.exclude(city='San Diego')

# Query with include() and exlude() methods or equivalent SQL: 'SELECT...WHERE STATE='CA' AND NOT (city = "San Diego")'
ca_stores_without_san_diego = Store.objects.filter(state='CA').exclude(city='San Diego')

###### view the actual SQL

from coffeehouse.stores.models import Store

import logging
stdlogger = logging.getLogger(__name__)

# Get the Store records with city San Diego
san_diego_stores = Store.objects.filter(city='San Diego')
stdlogger.debug("Query %s" % str(san_diego_stores.query))
# You can also use print(san_diego_stores.query)

###### Read multiple records with in_bulk() method
# Import Django model class

from coffeehouse.stores.models import Store

# Query with in_bulk() all
Store.objects.in_bulk()
# Outputs: {1: <Store: Corporate (San Diego,CA)>, 2: <Store: Downtown (San Diego,CA)>, 3: <Store: Uptown (San Diego,CA)>, 4: <Store: Midtown (San Diego,CA)>}

# Compare in_bulk query to all() that produces QuerySet
Store.objects.all()

# Outputs: <QuerySet {<Store: Corporate (San Diego,CA)>, <Store: Downtown (San Diego, CA)>, <Store: Uptown (San Diego,CA)>, <Store: Midtown (San Diego,CA)>]>

# Query to get single Store by id
Store.objects.in_bulk([1])
# Outputs: {1: <Store: Corporate (San Diego, CA)>}

# Query to get multiple Stores by id
Store.objects.in_bulk([2,3])
# Outputs: {2: <Store: Downtown (San Diego,CA)>, 3: <Store: Uptown (San Diego,CA)>}

###### Chained model methods to illustrate concept of QuerySet lazy evaluation
# Import Django model class

from coffeehouse.stores.models import Store

# Query with all() method
stores = Store.objects.all()
# Chain filter() method on query
stores = sotes.filter(state='CA')
# Chain exlude() method on query
stores = stores.exclude(city='San Diego')

###### QuerySet caching behavior
# Import Django model class

from coffeehouse.stores.models import Store

# CACHE USING SEQUENCE
# Query awaiting evaluation
lazy_stores = Store.objects.all()
# Iteration triggers evaluation and hits database
store_emails = [store.email for store in lazy_stores]
# Uses QuerySet cache from lazy_stores, since lazy_stores is evaluated in previous line
store_names = [store.name for store in lazy_stores]

# NON-CACHE SEQUENCE
# Iteration triggers evaluation and hits database
heavy_store_emails = [store.email for store in Store.objects.all()]
# Iteration triggers evaluation and hits database again, because it uses another QuerySet ref
heavy_store_names = [store.name for store in Store.objects.all()]

# CACHE USING SEQUENCE
# Query wrapped as list() for immediate evaluation
stores = list(Store.objects.all())
# Uses QuerySet cache from stores
first_store = stores[0]
# Uses QuerySet cache from stores
second_store = sotes[1]
# Uses QuerySet cache from stores, set() is just used to eliminate duplicates
store_states = set([store.state for store in stores])
# Uses QuerySet cache from stores, set() is just used to eliminate duplicates
store_cities = set([store.city for store in stores])

# NON-CACHE SEQUENCE
# Query awaiting evaluation
all_stores = Store.objects.all()
# list() triggers evaluation and hits database
store_one = list(all_stores[0:1])
# list() triggers evaluation and hits database again, because partially evaluating a QuerySet does not populate the cache
store_one_again = list(all_stores[0:1])

# CACHE USING SEQUENCE
# Query awaiting evaluation
coffee_stores = Store.objects.all()
# Iteration triggers evaluation and hits database
[store for store in coffee_stores]
# Uses QuerySet cache from coffee_stores, because it's evaluated fully in previous line
store_1 = coffee_stores[0]
# Uses QuerySet cache from coffee_stores, because it's already evaluated in full
store_1_again = coffee_stores[0]

###### Read performance with defer() and only() to selectively read record fields

from coffeehouse.stores.models import Store
from coffeehouse.item.models import Item

# Item names on the breakfast menu
breakfast_item = Item.objects.filter(menu__name='Breakfast').only('name')
# All Store records with no email
all_stores = Store.objects.defer('email').all()

# Confirm loaded fields on overall query
breakfast_items.query.get_loaded_field_names()

# Outputs: {<class 'coffeehouse.items.models.Item'>: {'id','name'}}
all_stores.query.get_loaded_names()
# Outputs: {<class 'coffeehouse.stores.models.Store'>: {'id','address','state','city','name'}}

# Confirm deferred fields on individual model records breakfast_items[0].get_deferred_fields()
# Outputs: {'calories','stock','price','menu_id','size','description'}
all_stores[1].get_deferred_fields()
#Outputs: {'email'}

# Access deferred fields, note each call on a deferred field implies a database hit
breakfast_items[0].price
breakfast_items[0].size
all_stores[1].email

###### Read performance with values() and values_list() to selectively read record fields

from coffeehouse.stores.models import Store
from coffeehouse.item.models import Item

# Item names on the breakfast menu
breakfast_items = Item.objects.filter(menu__name='Breakfast').values('name')
print(breakfast_items)
# Outputs: <QuerySet[{'name': 'Whole-Grain Oatmeal'}, {'name': 'Bacon, Egg & Cheese Biscuit'}]>

# All Store records with no email
all_stores = Store.objects.values_list('email','name','city').all()
print(all_stores)
# Outputs: <QuerySet [('corporate@coffeehouse.com', 'Corporate', 'San Diego'), ('downtown@coffeehouse.com', 'Downtown', 'San Diego'), ('uptown@coffeehouse.com', 'Uptown', 'San Diego'), ('midtown@coffeehouse.com', 'Midtown', 'San Diego')]>

all_stores_flat = Store.objects.values_list('email', flat=True).all()
print(all_stores_flat)
# Outputs: <QuerySet ['corporate@coffeehouse.com', 'downtown@coffeehouse.com', 'midtown@coffeehouse.com', 'uptown@coffeehouse.com']>

# It isn't possible to access undeclared model field with values() and values_list()
breakfast_items[0].price #ERROR
# Outputs AttributeError: 'dict' object has no attribute 'price'

###### Read performance with iterator(), exists(), and none()

from cofeehouse.stores.models import Store

# All Store with iterator()
stores_on_iterator = Store.objects.all().iterator()

print(stores_on_iterator)
# Outputs: <generator object __iter__ at 0x4r2864db8fc0>

# Advance through iterator with __next__()
stores_on_iterator.__next__()
# Outputs: <Store: Corporate (San Diego,CA)>

# Check if Store object with id=5 exists
Store.objects.filter(id=5).exists()
# Outputs: False

# Create empty QuerySet on Store model
Store.objects.none()
# Outputs: <QuerySet []>

###### Update multiple records with the update() method

from coffeehouse.stores.models import Store

Store.objects.all().update(email="contact@coffeehouse.com")

from coffeehouse.items.models import Item
from django.db.models import F

Item.objects.all().update(stock=F('stock') +100)

###### Update multiple records with a Django model with the select_for_update() method
# Import Django model class

from coffeehouse.stores.models import Store
from django.db import transaction

# Trigger atomic transaction so loop is executed in a single transaction 
with transaction.atomic():

    store_list = Store.objects.select_for_update().filter(state='CA')
    # Loop over each store to update and invoke save() on each entry
    for store in store_list:
        # Add complex update logic here for each store
        # save() method called on each member to update
        store.save()

# Method decorated with @transaction.atomic to ensure logic is executedin single transaction
@transaction.atomic
def bulk_store_update(store_list):
    store_list = Store.objects.select_for_update().exlude(state='CA')
    # Loop over each store and invoke save() on each entry
    for store in store_list:
        # Add complex update logic here for each store
        # save() method called on each member to update
        store.save()

# Call bulk_store_update to update store records
bulk_store_update(store_list_to_update)

###### Delete model record with the delete() method

from coffeehouse.stores.models import Store

Store.objects.filter(city='San Diego').delete()

###### One to many ForeignKey direct query read operations

class Menu(models.Model):
    name = models.CharField(max_length=30)

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

# Get the Menu of a given Item
Item.objects.get(name='Whole-Grain Oatmeal').menu.name

# Get Item elements that belong to the Menu with name 'Drinks'
Item.objects.filter(menu__name='Drinks')

###### One to many ForeignKey reverse query read operations with _set syntax

from coffeehouse.items.models import Menu, Item

breakfast_menu = Menu.objects.get(name='Breakfast')

# Fetch all Item records for the Menu
breakfast_menu.item_set.all()

# Get the total Item count for the Menu
breakfast_menu.item_set.count()

# Fetch Item records that match a filter for the Menu
breakfast_menu.item_set.filter(name__startswith='Whole')

###### One to many ForeignKey reverse query create, update, delete operations with _set syntax

from coffeehouse.items.models import Menu, Item

breakfast_menu = Menu.objects.get(name='Breakfast')

# Create an Item directly on the Menu
# NOTE: Django also supports the get_or_create() and update_or_create() operations
breakfast_menu.item_set.create(name='Bacon, Egg & Cheese Biscuit',description='A fresh buttermilk biscuit...',calories=450)

# Create an Item separately and then add it to the Menu
new_menu_item = Item(name='Grilled Cheese',description='Flat bread or whole wheat...',calories=500)
# Add item to menu using add()
# NOTE: bulk=False is necessary for new_menu_item to be saved by the Item model manager first
# it isn't possible to call new_menu_item.save() directly because it lacks a menu instance
breakfast_menu.item_set.add(new_menu_item,bulk=False)

# Create copy of breakfast items for later
breakfast_items = [bi for bi in breakfast_menu.item_set.all()]

# Clear menu references from Item elements (i.e. reset the Item elements menu field to null)
# NOTE: This requires the ForeignKey definition to have null=True
# (e.g. models.ForeignKey(Menu, null=True)) so the key is allowed to beturned null
# otherwise the error 'RelatedManager' object has no attribute 'clear' is thrown
breakfast_menu.item_set.clear()

# Verify Item count is now 0
breakfast_menu.item_set.count()
0

# Reassign Item set from copy of breakfast items
breakfast_menu.item_set.set(breakfast_items)

# Verify Item count is now back to original count
breakfast_menu.item_set.count()
3

# Clear men reference from single Item element (i.e. reset an Item element menu field to null)
# NOTE: This requires the ForeignKey definition to have null=True
# (e.g. models.ForeignKey(Menu, null=True)) so the key is allowed to be turned null
# otherwise the error 'RelatedManager' object has no attribute 'remove' is thrown
item_grilled_cheese = Item.objects.get(name='Grilled Cheese')
breakfast_menu.item_set.remove(item_grilled_cheese)

# Delete the Menu element along with its associated Item elements
# NOTE: This requires the ForeignKey definition to have blank=True and on_delete=models.CASCADE (e.g. models.ForeignKey(Menu, blank=True, on_delete=models.CASCADE))
breakfast_menu.delete()

###### Many to many ManyToManyField direct query read operations

class Amenity(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30,unique=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    email = models.EmailField()
    amenities = models.ManyToManyField(Amenity,blank=True)

# Get the Amenity elements of a given Store
Store.objects.get(name='Downtown').amenities.all()

# Fetch store named Midtown
midtown_store = Store.objects.get(name='Midtown')

# Create and add Amenity element to Store
midtown_store.amenities.create(name='Laptop Lock',description='Ask our baristas..')

# Get all Store elements that have amenity id=3
Store.objects.filter(amenities__id=3)

######
