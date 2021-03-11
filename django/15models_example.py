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

######
