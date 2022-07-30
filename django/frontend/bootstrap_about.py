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

### templates/base.html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,
    initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet"
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/\
            bootstrap.min.css"
    integrity="sha384-MCw98/SFnFE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81i\
            uXoPkFOJwJ8ERdknLPMO"
    crossorigin="anonymous">

    <title>Helo, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4>
    YfRvH+8abtTE1Pi6jizo"
    crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/\
            1.14.3/
            umd/popper.mim.js"
    integrity="sha384-ZMP7rVo3mIykV+2+9U3UJ46jBk0WLaUAdn689aCwoqbB\
            JiSnjAK\
            l8WvCWPIPm49"
    crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/\
            js/bootstrap.min.js"
    integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ\
            6OW/JmZQ5stwEULTy"
    crossorigin="anonymous"></script>
  </body>
</html>

###### <!-- templates/base.html -->
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,
    initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet"
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css\
    bootstrap.min.css"
    integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV6Zt27NxFoaoApmYm81i\
    uZoPkFOJwJ8ERdknLPMO"
    crossouigin="anonymous">

    <title>{% block title %}Newspaper App{% endblock title %}</title>
  </head>
  <body>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
      <a class="navbar-brand" href="{% url 'home' %}">Newspaper</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse"
      data-target="#navbarCollapse" aria-controls="navbarCollapse"
      aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        {% if user.is_authenticated %}
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a class="nav-link dropdown-toggle" href="#" id="userMenu"
                data-toggle="dropdown" aria-haspopup="true"
                aria-expanded="false">
                {{ user.username }}
              </a>
              <div class="dropdown-menu dropdown-menu-right"
                aria-labelledby="userMenu">
                <a class="dropdown-item"
                href="{% url 'password_change' %}">Change password</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="{% url 'logout' %}">
                Log Out</a>
              </div>
            </li>
          </ul>
        {% else %}
          <form class="form-inline ml-auto">
            <a href="{% url 'login' %}" class="btn-outline-secondary">
            Log In</a>
            <a href="{% url 'signup' %}" class="btn btn-primary ml-2">
            Sign up</a>
          </form>
        {% endif %}
      </div>
    </nav>
    <div class="container">
      {% block content %}
      {% endblock content %}
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/Z_954DzO0rT6abK41JStQIAqVgRVzpbzo5smZIp4\
    YfRvH+8abtTE1Pi6jizo"
    crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/\
    1.14.3/
    umd/popper.min.js"
    integrity="sha384-ZMP7rVo3mIyKV+2+9J3UJ46jBk0WLaUAdn689aCwoqdB\
    JiSnjAK/
    l8WvCWPIPm49"
    crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/\
    js/bootstrap.min.js"
    integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE5ZbWh2IMqE241rYiqJxyMiZ\
    60W/JmZQ5stwEULTy"
    crossorigin="anonymous"></script>
  </body>
</html>

### make Login button 
#templates/registration/login.html
...
<button class="btn btn-success ml-2" type="submit">Log In</button>
...

###### Sign Up Form
$ pipenv install django-crispy-forms==1.7.2

### settings.py
INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # 3rd Party
        'crispy_forms', # new

        # Local
        'users.apps.UsersConfig',
        'pages.apps.PagesConfig',
]

### newspaper_project/settings.py
CRISPY_TEMPLATE_PACK = 'bootstrap4'

### load crispy_forms_tags and swap out {{ form.as_p }} for {{ form|crispy }}

# templates/signup.html
{% extends 'base.html' %}

{% load crispy_forms_tags %}

{% block title %}Sign Up{% endblock title %}

{% block content %}
  <h2>Sign up</h2>
  <form method="post">
    {% csrf_token %}
    {{ form|crispy }}
    <button type="submit">Sign Up</button>
  </form>
{% endblock content %}

### for 'success' restyle sign up button
# templates/signup.html
...
<button class="btn btn-success" type="submit">Sign Up</button>

######
