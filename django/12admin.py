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

#11 models.py for change admin site logic

class Sighting(model.Model):
    superhero = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    power = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    sighted_on = models.DateTimeField()

    def __str__(self):
        return "{}'s power {} sighted at: {} on {} {}".format(
                self.superhero,
                self.power,
                self.location.country,
                self.sighted_on)

    def get_absolute_url(self)
    from django.urls import reverse
    return reverse('sighting_details', kwargs={'pk': self.id})


    class Meta:
        unique_together = ("superhero", "power")
        ordering = ["-sighted_on"]
        verbose_name = "Sighted & Encounter"
        verbose_name_plural = "Sighteds & Encounters"


# admin.py

class SightingAdmin(admin.ModelAdmin):
    list_display = ('superhero', 'power', 'location', 'sighted_on')
    date_hierarchy = 'sighted_on'
    search_fields = ['superhero']
    ordering = ['superhero']

admin.site.register(models.Sighting, SightingAdmin)

# admin/base_site.html

{% block extrastyle %}
  <link href='http://fonts.googleapis.com/css?family=Special+Elite'
  rel='stylesheet' type='text/css'>
  <style type="text/css">
  body, td, th, input {
          font-family: 'Special Elite', cursive;
  }
  </style>
{% endblock %}

# Adding a rich-text editor
# templates/admin/posts/change_form.html

{% extends "admin/change_form.html" %}

{% block footer %}
  {{ block.super }}
  <script
src="//cdn.ckeditor.com/4.4.4/standard/ckeditor.js"></script>
  <script>
  CKEDITOR.replace("id_message", {
      toolbar:[
          ['Bold', 'Italic', '-', 'NumberedList', 'BulletedList'],],
      width: 600,
  });
  </script>
  <style type="text/css">
  .cke { clear: both; }
  </style>
{% endblock %}

#12 castomize admin site with trubles, admin.py

from django.contrib.admin import AdminSite
from reviews.models import (Publisher, Contrivutor, Book,
        BookContributor, Review)


class BookrAdminSite(AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Bookr site admin'

admin_site = BookrAdminSite(name='bookr')

# Register your models here.
admin_site.register(Publisher)
admin_site.register(Contributor)
admin_site.register(Book)
admin_site.register(BookContributor)
admin_site.register(Review)

# urls.py

from reviews.admin import admin_site
import reviews.views
from django.urls import include, path


urlpatterns = [
        path("admin/", admin_site.urls),
        path("book-search", reviews.views.book_search),
        path("", include("reviews.urls")),
]

#13 customize admin site without breaking auto-discovery or any of its other default features
# put new admin.py at the top level of the Bookr project directory

from django.conrib import admin


class BookrAdminSite(admin.AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Bookr site admin'

# reviews/adminconfig.py

from django.contrib.admin.apps import AdminConfig


class ReviewsAdminConfig(AdminConfig):
    default_site = 'admin.BookrAdminSite'

# settings.py

INSTALLED_APPS = [
        'reviews.adminconfig.ReviewsAdminConfig',  # <-- replace to this
        'django.contrib.auth',
        'dango.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'reviews']

# other admin.py how beneathe?

from django.contrib import admin
from reviews.models import (Publisher, Contributor,
        Book, BookContributor, Review)

# Register your model here.
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)  #<--
admin.site.register(BookContributor)
admin.site.register(Review)

#14
