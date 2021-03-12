""" Second part of admin.py examples."""

###### Register models in admin.py file

from django.contrib import admin
from coffeehouse.stores.models import Store

# Option 1 = Basic
admin.site.register(Store)

# Option 2 Allows customizing Django admin behavior
class StoreAdmin(admin.ModelAdmin):
    pass

admin.site.registr(Store,StoreAdmin)

# Option 3 - Decorator
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass

###### Django admin list_display option

from django.contrib import  admin
from coffeehouse.stores.models import Store

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name','address','city','state']

admin.site.register(Store, StoreAdmin)

###### Django admin list_display option with callables

from django.contrib import admin
from coffeehouse.stores.models import Store

# Option 1
# admin.py
def upper_case_state(obj):
    return ("%s %s" % (obj.sity, obj.state)).upper()
upper_case_city_state.short_description = 'City/State'


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name','address','upper_case_city_state']

# Option 2
# admin.py
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name','address','upper_case_city_state']
    def upper_case_city_state(self, obj):
        return ("%s %s" % (obj.city, obj.state)).upper()
    upper_case_city_state.short_description = 'City/State'

# Option 3
# models.py
from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    def email_domain(self):
        return self.email.split("@")[-1]
    email_domain.short_description = 'Email domain'

# admin.py
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'email_domain']

###### Django admin list_display option with callable and format_html
# models.py

from django.db import models
from django.utils.html import format_html

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30,unique=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    def full_address(self):
        return format_html('%s - <b>%s,%s</b>' % (self.address,self.city,self.state))

# admin.py
from django.contrib import admin
from coffeehouse.stores.models import Store

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name','full_address']

######
