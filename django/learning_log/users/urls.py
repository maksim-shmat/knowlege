"""Make url scheme for users."""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
        # Make URL authorization by default
        path('', include('django.contrib.auth.urls')),
]
