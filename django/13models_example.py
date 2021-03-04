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

######
    
