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

######
