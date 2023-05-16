""" About admin."""

### admin configuration about contact view

from django.contrib import admin
from contrib import models

class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Contact, ContactAdmin)

#1 Registering models using a statement

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ..chapter_3.models import Seller


class SellerAdmin(UserAdmin):
    pass
admin.site.register(Seller, SellerAdmin)

#1.1 Registering models using a decorator

from django.contrib import admin
from ..chapter_3.modles import (
        Engine,
        Seller,
        Vehicle,
        VehicleModel
)

@admin.register(Seller)
class SellerAdmin(UserAdmin):
    pass

#2 Changelist view-related options

actions_on_bottom = True
actions_on_top = True

actions_selection_counter = True

list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'name',
        'is_staff',
        'is_superuser',
)

list_display_links = (
        'username',
        'name',
)

list_editable = (
        'first_name',
        'last_name',
)

list_filter = (
        'is_staff',
        'is_superuser',
        'is_active',
        'name',
        'groups'
)

list_per_page = 20

ordering = ('username',)
ordering = ('-username',)

preserver_filters = False

search_fields = (
        'username',
        'first_name',
        'last_name',
        'name',
        'email'
)

exclude = ('first_name',)

fields = ('username', 'password', 'first_name', 'last_name',)
# fields not fredshiped with fieldsets
fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'usernae',
                'password',
            ),
        }),
        (('Personal Info'), {'fields': (
            'first_name',
            'last_name',
            'name',
            'email',
        )}),
        (('Permissions'), {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
        (('Important Dates'), {'fields': (
            'last_login',
            'date_joined',
        )}),
        (('Vehicles'), {
            'description': ('Vehicles that this user is selling.'),
            'fields': (
                'vehicles',
            ),
        }),
)

filter_horizontal = ('vehicles',)

filter_vertical = 

#3 Class StackedInline admin.py
...
from django.contrib.admin import ..., StackedInline


class VehicleInline(StackedInline):
    model = Vehicle
    extra = 1


class EngineAdmin(ModelAdmin):
    ...
    inlines = [VehicleInline,]

#4 Class TabularInline admin.py
...
from django.contrib.admin import ..., TabularInline


class VehicleInline(TabularInline):
    model = Vehicle
    extra = 1

#5 ManyToMany field inlines admin.py
...
from django.contrib.admin import ..., TabularInline


class VehiclesInline(TabularInline):
    model = Seller.vehicles.through
    extra = 1


class SellerAdmim(UserAdmin):
    inlines = [VehiclesInline,]

#6 Option - radio_field admin.py
...
from django.contrib import admin
from django.contrib.admin import ModelAdmin


class VehicleAdmin(ModelAdmin):
    radio_fields = {'engine': admin.HORIZONTAL,}  or VERTICAL

#7 More options

save_on_top = True

add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
            ),
        }),
        (('Personal Info'), {'fields': (
            'first_name',
            'last_name',
            'name',
            'email',
        )}),
)

prepopulated_fields = {
        'username': ('first_name', 'last_name',)
}

#8 Method - get_form()
# Create EngineForm, EngineSuperUserForm, AddEngineForm in forms.py with pass

from .forms import AddEngineForm, EngineForm
...

class EngineAdmin(ModelAdmin):
    ...
    #form = EngineForm

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            return EngineForm
        else:
            return AddEngineForm
    return super(EngineAdmin, self).get_form(request, obj, **kwargs)

# for superuser condition

from .forms import ..., EngineSuperUserForm
...

class EngineAdmin(ModelAdmin):
    ...
    def get_form(self, request, obj=None, **kwargs):
        if obj:
            if request.user.is_superuser:
                return EngineSuperUserForm
            else:
                return EngineForm
        else:
            return AddEngineForm

#9 Method - save_model()

class EngineAdmin(ModelAdmin):
    ...
    def save_model(self, request, obj, form, change):
        print(obj.__dict__)
        # Code actions before save here
        super().save_model(request, obj, form, change)
        # Code actions after save here

#10 Method - delete_model()

class EngineAdmin(self, request, obj):
    print(obj.__dict__)
    # Code actions before save here
    super().delete_model(request, obj)
    # Code actions after save here
