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

