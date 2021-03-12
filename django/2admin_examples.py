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

######
