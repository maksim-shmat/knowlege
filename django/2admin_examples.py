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

###### Django admin empty_value_display option global, class, or field-level configuration

# Option 1 - Globally set empty values to ???
# settings.py

from django.contrib import admin
admin.site.empty_value_display = '???'

# Option 2 - Set all fields in a class to 'Unknown Item field'
# admin.py to show "Unknown Item field" instead of '-' for NULL values in all Item fields
# NOTE: Item model in items app

class ItemAdmin(admin.ModelAdmin):
    list_display = ['menu','name','price']
    empty_value_display = 'Unknown Item field'

admin.site.register(Item, ItemAdmin)

# Option 3 - Set individual field in a class to 'No known price'
class ItemAdmin(admin.ModelAdmin):
    list_display = ['menu','name','price_view']
    def price_view(self, obj):
        return obj.price
    price_view.empty_value_display = 'No known price'

###### Django admin with admin_order_field option
# models.py

from django.db import models
from django.utils.html import format_html

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30,unique=True)
    city = models.CharField(max_lenght=30)
    state = models.CharField(max_length=2)
    def full_address(self):
        return format_html('%s - <b>%s,%s</b>' % (self.address,self.city,self.state))
    full_address.admin_order_field = 'city'

# admin.py
from django.contrib import admin
from coffeehouse.stores.models import Store

class StoreAdmin(admin.ModelAdmin):
    list_diplaty = ['name','full_address']

###### Django admin with list_display_links option

# Sample 1)
# admin.py
from django.contrib import admin
from coffeehouse.stores.models import Store

class Store Admin(admin.ModelAdmin):
    list_display = ['name','address','city','state']
    list_display_links = None

admin.site.register(Store, StoreAdmin)

# Sample 2)
# admin.py
from django.contrib import admin
from coffeehouse.items.models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['menu', 'name', 'price_view']
    list_display_links = ['menu', 'name']

admin.site.register(Item, ItemAdmin)

###### Django admin with list_editable option

# admin.py
from django.contrib import admin
from coffeehouse.stores.models import Store

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'state']
    list_editable = ['address', 'city', 'state']

admin.site.register(Store, StoreAdmin)

###### Django admin with list_per_page option

# admin.py
from django.contrib import admin
from coffeehouse.items.models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['menu', 'name', 'price']
    list_per_page = 5

admin.site.register(Item, ItemAdmin)

###### Django admin search_field option

from django.contrib import admin
from coffeehouse.stores.models import Store

class StoreAdmin(admin.ModelAdmin):
    search_field = ['city', 'state']

admin.site.register(Store, StoreAdmin)

###### Django admin list_filter option

from django.contrib import admin
from coffeehouse.items.models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['menu', 'name', 'price']
    list_filter = ['menu', 'price']

admin.site.register(Item, ItemAdmin)

###### Django admin list_display option with ManyToManyField field
# models.py

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

# admin.py
from django.contrib import admin
from coffeehouse.stores.models import Store

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'state', 'list_of_amenities']
    def list_of_amenities(self, obj):
        return ("%s" % ', '.join([amenity.name for amenity in obj.amenities.all()]))
    list_of_amenities.short_discription = 'Store amenities'

admin.site.register(Store, StoreAdmin)

###### Django admin admin_order_field option with ForeignKey field
# model.py

class Menu(models.Model):
    name = modes.CharField(max_length=30)
    creator = models.CharField(max_length=100,default='Coffeehouse Chef')
    def __str__(self):
        return u"%s" % (self.name)


class Item(models.Model):
    menu = models.ForeignKey(Menu)
    name = models.CharField(max_length=30)

# admin.py
from django.contrib import admin
from coffeehouse.stores.models import Store


class ItemAdmin(admin.ModelAdmin):
    list_display = ['menu', 'name', 'menu_creator']
    def menu_creator(self, obj):
        return obj.menu.creator
    menu_creator.admin_order_field = 'menu__creator'

admin.site.register(Item, ItemAdmin)

###### Django admin list_filter option with admin.RelatedOnlyFieldListFilter
# admin.py

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name','address','city','state','list_of_amenities']
    list_filter = [['amenities',admin.RelatedOnlyFieldListFilter]]
    def list_of_amenities(self, obj):
        return ("%s" % ','.join([amenity.name for amenity in obj.amenities.all()]))
    list_of_amenities.short_description = 'Store amenities'

###### Django admin fields option for Django admin fields

class StoreAdmin(admin.ModelAdmin):
    fields = ['address','city','state','email']

admin.site.register(Store, StoreAdmin)

###### Django admin readonly_fields option for Django admin forms

class StoreAdmin(admin.ModelAdmin):
    readonly_fields = ['name','amenities']

admin.site.register(Store, StoreAdmin)

###### Django admin readonly_fields option with callable for Django admin forms

from django.utils.safestring import mark_safe

class StoreAdmin(admin.ModelAdmin):
    fields = ['name','address',('city','state'),'email','custom_amenities_display']
    readonly_fields = ['name','custom_aminities_display']
    def custom_amenities_display(self, obj):
        return mark_safe("Amenities can only by modified by special request, please contact the ctore manager at %s to create a request" % (obj.email,obj.email))
    custom_amenities_display.short_description = "Amenities"

admin.site.register(Store, StoreAdmin)

###### Django admin fieldsets option for Django admin forms

from django.utils.safestring import mark_safe

class StoreAdmin(admin.ModelAdmin):
    fieldsets = [
            ['Store general information', {
                'fields': ['name', 'email']
            }],
            ['Store location options', {
                'classes': ['collapse'],
                'fields': ['address',('city', 'state')],
            }],
    ]

admin.site.register(Store, StoreAdmin)

###### Django admin formfield_overrides option for Django admin forms

from django.contrib import admin
from coffeehouse.items.models import Menu

class MenuAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.CharField: {'widget': forms.Textarea}
    }

admin.site.register(Menu, MenuAdmin)

###### Django admin formfield_overrides option for Django admin forms

from django.contib import admin
from coffeehouse.items.models import Menu

class MenuAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.CharField: {'widget': forms.Textarea}
    }

admin.site.register(Menu, MenuAdmin)

###### Django admin radio_fields opton for ForeignKey field

from django.contrib import admin
from coffeehouse.items.models import Item

# Option 1 (Hourizontal)

class ItemAdmin(admin.ModelAdmin):
    radio_fields = {"menu": admin.HORIZONTAL}

admin.site.register(Item, ItemAdmin)

# Option 2 (Vertical)

class ItemAdmin(admin.ModelAdmin):
    radio_fields = {"menu": admin.VERTICAL}

admin.site.register(Item, ItemAdmin)

###### Django admin inlines option for ForeignKey and ManyToManyField field
# admin.py (ForeignKey)

from django.contrib import admin
from coffeehouse.items.models import Item, Menu

class ItemInline(admin.TabularInline):
    model = Item


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [
            ItemInline,
    ]

admin.site.register(Menu, MenuAdmin)

# admin.py (ManyToManyField)

from django.contrib import admin
from coffeehouse.stores.models import Store, Amenity

class StoreInline(admin.StackedInline):
    model = Store.amenities.through


class AmenityAdmin(admin.ModelAdmin):
    inlines = [
            StoreInline,
    ]

admin.site.register(Amenity, AmenityAdmin)

###### Djnago admin django.contrib.admin.site object to customize fields

from django.conf.urls import url
from django.contrib import admin

admin.site.site_header = 'Coffeehouse admin'
admin.site.site_titlej = 'Coffeehouse admin'
admin.site.site_url = 'http://coffeehouse.com/'
admin.site.index_title = 'Coffeehouse administration'
admin.empty_value_display = '**Emply**'

urlpatterns = [
        url(r'^admin/', admin.site.urls),
]

###### Django admin class with Media class to define custom static resources

from django.contrib import admin
from coffeehouse.items.models Item

class ItemAdmin(admin.ModelAdmin):
    list_per_page = 5
    class Media:
        css = {
                "screen": ("css/items/items.css",)
        }
        js = ("js/items/items.js",)

admin.site.register(Item, ItemAdmin)

######
