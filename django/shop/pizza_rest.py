"""Instructions."""

mkdir pizzavspizza
pipenv install django
django-admin startproject pizzaproject
python manage.py migrate
python manage.py createsuperuser

pipenv install djangorestframework
INSTALLED_APPS = [
        ...
        'rest_framework',
]

python manage.py startapp stores
INATALLED_APPS = [
        ...
        'stores',
]

make a pizza_model.py

pipenv install Pillow

After model.py change -> makemigrations and migrate

# next add our Model to the admin.py
admin.py
from django.contrib import admin
from .models import Pizzeria  # and then fool path - from stores.model import Pizzeria
admin.site.register(Pizzeria)

-----------------------
#add more to model.py
make data to the string in a model.py
def __str__(self):
    return "{}, {}".format(self.pizzeria_name, self.city)

-----------------------
#Now DjangoREST make serialization to JSON
tou
