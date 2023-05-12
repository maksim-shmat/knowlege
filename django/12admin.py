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


