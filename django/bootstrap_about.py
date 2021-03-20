"""Make a beauty."""

###### $ python manage.py startapp pages

### settings.py
INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'users.apps.UsersConfig',
        'pages.apps.PagesConfig', # new
]

### newspaper_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        path('admin/', admin.site.urls),
        path('users/', include('users.urls')),
        path('users/', include('django.contrib.auth.urls')),
        path('', include('pages.urls')), # new  # go up str?
]

### $ touch pages/urls.py
from django.urls import path

from . import views

urlpatterns = [
        path('', views.HomePageView.as_view(), nae='home'),
]

### pages/views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

###
