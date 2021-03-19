""" Authentication examples."""

# create the permission for model
from myapp.models import BlogPost
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(BlogPost)
permission = Permission.objects.create(
        codename='can_publish',
        name='Can Publish Posts',
        content_type=content_type,
)

########
# Permission caching

from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from myapp.models import BlogPost

def user_gains_perms(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('myapp.change_blogpost')

    content_type = ContentType.objects.get_for_model(BlogPost)
    permission = Permission.objects.get(
            codename='change_blogpost',
            content_type=content_type,
    )
    user.user_permissions.add(permission)

    # Checking the cached permission set
    user.has_perm('myapp.change_blogpost') # False

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('myapp.change_blogpost') # True
###########
# proxy models
class Person(models.Model):
    class Meta:
        permissions = [('can_eat_pizzas', 'Can eat pizzas')]

class Student(Person):
    class Meta:
        proxy True
        permissions = [('can_deliver_pizzas', 'Can deliver pizzas')]
"""
>>> # Fetch the content type for the proxy model.
>>> content_type = ContentType.objects.get_for_model(Student,
        for_concrete_model=False)
>>> student_permissions = Permission.objects.filter(content_type=content_type)
>>> [p.codename for p in student_permissions]
>>> for permission in student_permissions:
    user.user_permissions.add(permission)
>>> user.has_perm('app.add_permission')
>>> user.has_perm('app.can_eat_pizzas')
>>> user.has_perms(('app.add_student', 'app.can_deliver_pizzas'))
"""
###########
# log a user in
from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
##########
# log a user out
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.

###########
# limiting access to logged-in users
# and either redirect to a login page
from django.conf import settings
from django.shortcuts import redirect

def my_view(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    # ...

# or display an error message
from django.shortcuts import render

def my_view(request):
    if not request.user.is_authenticated:
        return render(request, 'myapp/login_error.html')
    # ...
###########
# use login_required decorator
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    ...
###
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='my_redirect_field')
def my_view(request):
    ...
###
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def my_view(request):
    ...
###
from django.contrib.auth import views as auth_views

path('accounts/login/', auth_views.LoginViewf.as_view()),

##############
# use LoginRequired mixin
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

###########
# limiting access to logged-in users that pass a test
from django.shortcuts import redirect

def my_view(request):
    if not request.user.email.endswith('@example.com'):
        return redirect('/login/?next=%s' % request.path)
    # ...

###
# user_passes_test as a shortcut
from django.contrib.auth.decorators import user_passes_test

def email_check(user):
    return user.email.endswith('@example.com')

@user_passes_test(email_check)
def my_view(request):
    ...

###
# UserPassesTestMixin ans test_func() or get_test_func()
from django.contrib.auth.mixins import UserPassesTestMixin

class MyView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.email.endswith('@example.com')

############
# use permission_required decorator
from django.contrib.auth.decorators import permission_required

@permission_required('polls.add_choice')
def my_view(request):
    ...

###
from django.contib.auth.decorators import permission_required

@permission_required('polls.add_choice', login_url='/loginpage/')
def my_view(request):
    ...

###
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('polls.add_choice', raise_exception=True)
def my_view(request):
    ...

##############
# session invalidation on password change
from django.contrib.auth import update_session_auth_hach

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        ...
##############
# use AuthenticationForm
from django.contrib.auth.form import AuthenticationForm

class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass
###
class PickyAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                    _("This account is inactive."),
                    code='inactive',
            )
        if user.username.startswith('b'):
            raise ValidationError(
                    _("Sorry, accounts starting with 'b' aren't welcome here."), code='no_b_users',
            )
#########
# password upgrading without requiring a login
# if you have an existing database with an older, weak hash such as MD5 or
# SHA1, you might want to upgrade those hashes youseld indstead of waiting for
# the upgrade to happen when a user logs in.
# account/hashers.py
from django.contrib.auth.hashers import(
        PBKDF2PasswordHasher, SHA1PasswordHasher,
)

class PBKDF2WrappedSHA1PasswordHasher(PBKDF2PasswordHasher):
    algorithm = 'pbkdf2_wrapped_sha1'

    def encode_sha1_hash(self.sha1_hash, salt, iterations=None):
        return super().encode(sha1_hash, salt, iterations)

    def encode(self, password, salt, iterations=None):
        _, _, sha1_hash = SHA1PasswordHasher().encode(password, salt).split('$', 2)
        return self.encode_sha1_hash(sha1_hash, salt, iterations)

### account/migrations/0002_migrate_sha1_passwords.py
from django.db import migrations
from ..hashers import PBKDF2WrappedSHA1PasswordHasher

def forwards_func(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    user = User.objects.filter(password__startswith='sha1$')
    hasher = PBKDF2WrappedSHA1PasswordHasher()
    for user in users:
        algorithm, salt, sha1_hash = user.password.split('$', 2)
        user.password = hasher.encode_sha1_hash(sha1_hash, salt)
        user.save(update_fields=['password'])

class Migration(migrations.Migration):
    dependancies = [
            ('accounts', '0001_initial'),
            # replace this with the latest migration in contrib.auth
            ('auth', '###_migration_name'),
    ]

    operations = [
            migrations.RunPython(forwards_func),
    ]
### mysite/settings.py
PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'accounts.hashers.PBKDR2WrappedSHA1PasswordHasher',
]
#############
# writing own validator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class MinimumLengthValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                    _("This password must contain at least %(min_length)d
                    characters."),
                    code='password_too_short',
                    params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _(
                "Your password must contain at least %(min_length)d characters."
                % {'min_length': self.min_length}
        )
###########
# writing an authentication backend
from django.contrib.auth.backends import BaseBackend

class MyBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        # Check the username/password and return a user.
        ...

###
from django.contrib.auth.backend import BaseBackend

class MyBackend(BaseBackend):
    def authenticate(self, request, token=None):
        # Check the token and return a user.
        ...
###########
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class SettingsBackend(BaseBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.
    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD =
    'pbkdf2_sha256$300000$....'
    """

    def authenticate(self, request, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
##########
# extending the existing User model
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = model.CharField(max_length=100)

###
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from my_user_profile_app.models import Employee

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

#############
# referencing the User model
from django.conf import settings
from django.db import models

class Article(models.Model):
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
    )
###
from django.conf import settings
from django.db.models.signals import post_save

def post_save_receiver(sender, instance, created, **kwargs):
    pass

post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)

###

from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.dispatch import receiver

@receiver(setting_changed)
def user_model_swapped(**kwargs):
    if kwargs['setting'] == 'AUTH_USER_MODEL':
        apps.clear_cache()
        from myapp import some_module
        some_module.UserModel = get_user_model()

###########
# custom users and the built-in auth forms
from django.contrib.auth.forms import UserCreationForm
from myapp.models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.field + ('custom_field',)
###
# admin-compliant custom user app
# models.py
from django.db import models
from django.contrib.auth.models import (
        BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of birth
        and password.
        """
        if not emaila:
            raise ValueError('Users must have an email address')
        user = self.model(
                email=self.normalize_email(email),
                date_of_birth=date_of_birth,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Create and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
                email,
                password=password,
                date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
            verbose_name='email address',
            max_length=255,
            unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

### admin.py
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from customauth.models import MyUser

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
            widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'date_of_birth')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Personal info', {'fields': ('date_of_birth',)}),
            ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standart ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('email', 'date_of_birth', 'password1', 'password2'),
                }),
    )
    search_fields = ('email',)
    ordering = ('email', )
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# .... and, since we're not using Django's built-in permission,
# unregister the Group model from admin.
admin.site.unregister(Group)

### settings.py
AUTH_USER_MODEL = 'customauth.MyUser'

#Mar 18.21##### User Account
# blog_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        path('admin/', admin.site.urls),
        path('accounts/' include('django.contrib.auth.urls')), # new
        path('', include('blog.urls')),
]

###
$ mkdir templates/registration
$ touch templates/registration/login.html

# templates/registration/login.html
{% extends 'base.html' %}

{% block content %}
<h2>Log In</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Log In</button>
</form>
{% endblock content %}

### settings.py
LOGIN_REDIRECT_URL = 'home'

###### update base.html and add auth
# templates/base.html
{% load static %}
<html>
  <head>
    <title>Django blog</title>
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400"
    rel="stylesheet">
    <link href="{% static 'css/base.css' %}" rel="stylesheet">
  </head>
  <body>
    <div>
      <header>
        <div class="nav-left">
          <h1><a href="{% url 'home' %}">Django blog</a></h1>
        </div>
        <div class="nav-right">
          <a href="{% url 'post_new' %}">+ New Blog Post</a>
        </div>
      </heder>
      {% if user.is_authenticated %}
        <p>Hi {{ user.username }}!</p>
      {% else %}
        <p>You are not logged in.</p>
        <a href="{% url 'login' %}">Log In</a>
      {% endif %}
    {% block content %}
    {% endblock content %}
    </div>
  </body>
</html>

###### Log out link
# templates/base.html

{% if user.is_authenticated %}
  <p>Hi {{ user.username }}!</p>
  <p><a href="{% url 'logout' %}">Log out</a></p>
{% else %}
...

### blog_project/settings.py
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home' # new

######
