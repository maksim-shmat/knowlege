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

###### properties.models.Property

from django.db import models
from django_localflavor_us import models as us_models

class Property(models.Model):
    LISTED, PENDING, SOLD = range(3)
    STATUS_CHOICES = (
            (LISTED, 'Listed'),
            (PENDING, 'Pending Sale'),
            (SOLD, 'Sold'),
    )

    slug = models.SlugField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = us_models.USStateField()
    zip = models.CharField(max_length=255)
    square_feet = models.PositiveIntegerField(null=True, blank=True)
    acreage = models.FloatField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,
                                              null=True, blank=True)
    price = models.PositveIntegerField(null=True, blank=True)
    features = models.ManyToManyField('Feature', through='PropertyFeature')
    interested_parties = models.ManyToManyField(Contact, 
                                                through='InterestedParty')

    objects = PropertyManager()

    class Meta:
        verbose_name_plural = 'properties'

    def __unicode__(self):
        return u'%s, %s' % (self.address, self.city)

###
class PropertyManager(models.Manager):
    def listed(self):
        qs = super(PropertyManager, self).get_query_set()
        return qs.filter(models.Q(status=Property.LISTED)
                         models.Q(status=Property.PENDING))

###### properties.models.Feature

class Feature(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    definition = models.TextField()

    def __unicode__(self):
        return self.title

### properties.models.PropertyFeature

class PropertyFeature(models.Model):
    property = models.ForeignKey(Property)
    feature = models.ForeignKey(Feature)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return unicode(self.feature)

### property.models.InterestedParty

from contacts.models import Contact

class InterestedParty(models.Model):
    BUILDER, OWNER, BUYER, AGENT, INSPECTOR = range(5)
    INTEREST_CHOICES = (
            (BUILDER, 'Builder'),
            (OWNER, 'Owner'),
            (BUYER, 'Buyer'),
            (AGENT, 'Agent'),
            (INSPECTOR, 'Inspector'),
    )

    property = models.ForeignKey(Property)
    contact = models.ForeignKey(Contact)
    interest = models.PositiveSmallIntegerField(choices=INTEREST_CHOICES)

    class Meta:
        verbose_name_plural = 'interested parties'

        def __unicode__(self):
            return u'%s, %s' % (self.contact, self.get_interest_display())

######
from django.contrib import admin
from properties import models

class InterestedPartyInline(admin.TabularInline):
    model = models.InterestedParty
    extra = 1

class PropertyFeatureInline(admin.TabularInline):
    model = models.PropertyFeature
    extra = 1

### 
from django.contrib import admin
from django import forms
from django_localflavor_us import forms as us_forms

from properties import models

class InterestedPartyInline(admin.TabularInline):
    model = models.InterestedParty
    extra = 1

class PropertyFeatureInline(admin.TabularInline):
    model = models.PropertyFeature
    extra = 1

class PropertyFeatureInline(admin.TabularInline):
    model = models.PropertyFeature
    extra = 1

class PropertyForm(forms.ModelForm):
    state = us_forms.USStateField(widget=us_forms.USStateSelect)
    zip = us_forms.USZipCodeField(widget=forms.TextInput(attrs={'size': 10}))

    class Meta:
        model = models.Property



###
class PropertyAdmin(admin.ModelAdmin):
    form = PropertyForm
    fieldsets = (
            (None, {'fields': (('address', 'slug'),
                               ('city', 'state', 'zip'))}),
            ('Sales Information', {'fields': ('status', 'price')}),
            ('Size', {'fields': ('square_feet', 'acreage')}),
    )
    inlines = (
            PropertyFeatureInline,
            InterestedPartyInline,
    )
    prepopulated_fields = {'slug': ('address', 'zip')}

admin.site.register(models.Property, PropertyAdmin)
###
class FeatureAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {
                'fields': (('title', 'slug'), 'definition'),
            }),
    )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Feature, FeatureAdmin)

#1 fieldsets

class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
            ("Name", {"fileds": ("firstname", "lastname")}),
            ("Location", {"fields": ("city", "state")})
    ]

#2
