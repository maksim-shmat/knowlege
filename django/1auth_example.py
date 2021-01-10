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
