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

######
