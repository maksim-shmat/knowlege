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
# add more to model.py
make data to the string in a model.py
def __str__(self):
    return "{}, {}".format(self.pizzeria_name, self.city)

-----------------------
# Now DjangoREST make serialization to JSON
# touch serializers.py
from rest_framefork import serializers
from .models import Pizzeria

class PizzeriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
                'id',
                'logo_image',
                'pizzeria_name',
                'city',
                'zip_code',
                'absolute_url'
        ]


    class PizzeriaDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Pizzeria
            fields = [
                    'id',
                    'pizzeria_name',
                    'street',
                    'city',
                    'state',
                    'zip_code',
                    'website',
                    'phone_number',
                    'description',
                    'logo_image',
                    'email',
                    'active'
            ]

----------------------
# next make a view.py
from django.shortcuts import render
from rest_framework import generics
from .serializers import PizzeriaListSerializer, PizzeriaDetailSerializer
from .models import Pizzeria
# Create your views here.

class PizzeriaListAPIView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaListSerializer


class PizzeriaRetriveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaCreateAPIView(generics.CreateAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaRetriveUpdateAPIView(generics.RetriveUpdateAPIView):
    lookup_field = "id"
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaDestroyAPIView(generic.DestroyAPIView):
    lookup_field = "id"
    queryset = Pizzeria.objects.all()

----------------------
# next urls.py
from django.urls import path
from . import views

urlpatterns = [
        path('', views.PizzeriaListAPIView.as_view(), name='pizzeria_list'),
        path('<int:id>/', views.PizzeriaRetrieveAPIView.as_view(),
            name="pizzeria_detail"),
        path('create/', views.PizzeriaCreateAPIView.as_view(), name='pizzeria_create'),
        path('update/<int:id>/', views.PizzeriaRetrieveUpdateAPIView.
            as_view(), name="pizzeria_update"),
        path('delete/<int:id>/', views.PizzeriaDestroyAPIView.as_view(), name='pizzeria_delete'),
]

# next add path to main urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('stores.urls')),
]

-----------------------

# next update serializers.py
from rest_framework import serializers
from .models import Pizzeria
from rest_framework.reverse import reverse

class PizzeriaListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Pizzeria
        field = [
                'id',
                'pizzeria_name',
                'city',
                'zip_code',
                'absolute_url'
        ]

    def get_absolute_url(self, obj):
        return reverse('pizzeria_detail', args=(obj.pk,))

######
