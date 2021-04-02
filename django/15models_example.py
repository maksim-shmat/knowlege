""" Fifth chapter about django models."""

###### Permission check in view method with @user_passes_test and @permission_required
# Method check to see if User belongs to group called 'Barista'

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

@user_passes_test(lambda u: Group.objects.get(name='Baristas') in u.groups.all())
def dashboard(request):
    # Logic for dashboard

# Explicit method check, if User is authenticated and has prmissions to change Store model

# Explicit method with test
def user_of_stores(user):
    if user.is_authenticated() and user.has_perm("stores.change_store"):
        return True
    else:
        return False

    # Method check using method
    @user_passes_test(user_of_stores)
    def store_manager(request):
        # Logic for store_manager

    # Method check to see if User has permissions to add Store model
    
    from django.contrib.auth.decorators import permission_required

    @permission_required('stores.add_store')
    def store_creator(request):
        # Logic for store_creator

###### Model with extra user fields related to default Django user model

from django.contrib.auth.models import User
from django.db import models

class UserExtra(models.Model):
    user = models.ForeignKey(User)
    age = models.IntegerField(blank=True,null=True)
    telephone = models.CharField(max_length=15,blank=True,null=True)

###### Custom User model to override default Djnago User model
# models.py (app registration)

from django.contrib.auth.models import AbstractUser
from django.db import models


class CoffeehouseUser(AbstractUser):
    age = models.IntegerField(blank=True,null=True)
    telephone = models.CharField(max_length=15,blank=True,null=True)

# admin.py (app registration)
from django.contrib import admin
from .models import CoffeehouseUser


class CoffeehouseUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(CoffeehouseUser, CoffeehouseUserAdmin)

# settings.py
AUTH_USER_MODEL = 'registration.CoffeehouseUser'

###### Custom authentication back end to support authentication with email
# models.py (registration app)

from django.contrib.auth import get_user_model

class EmailBackend(object):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            if getattr(user, 'is_active', False) and user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesExist:
            return None

# setting.py
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend', 'coffeehouse.registration.models.EmailBackend']

###### contacts.models.contact

from django.db import models
from django.contrib.auth.models import User
from django_localflavor_us import models as us_models

class Contact(models.Model):
    user = models.OneToOneField(User)
    phone_number = us_models.PhoneNumberField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = us_models.USStateField()
    zip_code = models.CharField(max_length=255)

    class Meta:
        ordering = ('user__last_name', 'user__first_name')

    def __unicode__(self):
        return self.user.get_full_name()

###
@property
def first_name(self):
    return self.user.first_name

@property
def last_name(self):
    return self.user.last_name

def get_full_name(self):
    return self.user.get_full_name()

######
