"""Working with token-based authentication."""

# not use in a production enviroment, orly?

#1 settings.py

INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Django REST framework
        'rest_framework',
        # Drones application
        'drones.apps.DronesConfig',
        # Django filters,
        'django_filters',
        # Token authentication
        'rest_framework.authtoken',
]

#2

$ python manage.py migrate


#3 views.py

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot_detail'
    authentication_classes = (
            TokenAuthentication,
            )
    permission_classes = (
            IsAuthenticated,
            )

class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot_list'
    fileter_fields = (
            'name',
            'gender',
            'races_count',
            )
    search_fields = (
            '^name',
            )
    ordering_fields = (
            'name',
            'races_count'
            )
    authentication_classes = (
            TokenAuthentication,
            )
    permission_classes = (
            IsAuthenticated,
            )

# Generating and using tokens

$ python manage.py shell

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# Replace user01 with the name you congigured for this user
user = User.objects.get(username="user01")
token = Token.objects.create(user=user)
print(token.key)


# token.key
ebebe09f5d7fe5228f9ed1468923ec5d3e471d3

$ quit()

