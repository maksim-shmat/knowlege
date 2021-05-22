"""Authentication about."""

### django/contrib/auth/urls.py
from django.contrib.auth import views
from django.urls import path

urlpatterns = [
        path('login/', views.LoginView.as_view(), name='login'),
        path('logout/', views.LogoutView.as_view(), name='logout'),
        
        path('password_change/', views.PasswordChangeView.as_view(),
            name='password_change'),
        path('password_change/done/', views.PasswordChangeDoneView.as_view(),
            name='password_change_done'),
        path('password_reset/', views.PasswordResetView.as_view(),
            name='password_reset'),
        path('password_reset/done/', views.PasswordResetDoneView.as_view(),
            name='password_reset_done'),
        path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
        path('reset/done/', views.PasswordResetCompleteView.as_view(),
            name='password_reset_complete'),
]

### next templates/registration/login.html
{% extends '_base.html' %}

{% block title %}Log In{% endblock title %}

{% block content %}

<h2>Log In</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Log In</button>
</form>

{% endblock content %}

### next settings.py
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

### next templates/home.html
{% extends '_base.html' %}

{% block title %}Home{% endblock title %}

{% block content %}
<h1>Homepage</h1>
{% if user.is_authenticated %}
  Hi {{ user.email }}!
  <p><a href="{% url 'logout' %}"Log Out</a></p>
{% else %}
  <p>You are not logged in</p>
  <a href="{% url 'login' %}">Log In</a>
{% endif %}
{% endblock content %}

### next users/urls.py
from django.urls import path
from .views import SignupPageView

urlpatterns = [
        path('signup/', SignupPageView.as_view(), name='signup'),
]

### next bookstore_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        # Django admin
        path('admin/', admin.site.urls),

        # User management
        path('accounts/', include('django.contrib.auth.urls')),

        # Local apps
        path('accounts/', include('users.urls')),
        path('', include('pages.urls')),
]

### next users/views.py
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

### next templates/signup/html
{% extends '_base.html' %}

{% block title %}Sign Up{% endblock title %}

{% block content %}
<h2>Sign Up</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Sign Up</button>
</form>
{% endblock content %}

### next templates/home.html
{% extends '_base.html' %}

{% block title %}Home{% endblock title %}

{% block content %}
<h1>Homepage</h1>
{% if user.is_authenticated %}
  Hi {{ user.email }}!
  <p><a href="{% url 'logout' %}">Log Out</a></p>
{% else %}
  <p>You are not logged in</p>
  <a href="{% url 'login' %}"Log In</a>
  <a href="{% url 'signup' %}">Sign Up</a>
{% endif %}
{% endblock content %}

###
