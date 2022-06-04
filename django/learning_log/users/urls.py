"""Make url scheme for users."""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
        # Make URL authorization by default
        path('', include('django.contrib.auth.urls')),

        # Page of registration
        path('register/', views.register, name='register'),
]
