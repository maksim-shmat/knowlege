""" About Django REST(Representational state transfer)."""

#1 first install it:
pip3 install djangorestframework
pip install markdown
pip install django-filter

#2 then add to the INSTALLED_APPS in settings.py with name

INSTALLED_APPS = [
        ...
        'rest_framework',
]
REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.
            DjangoModelPermissionsOrAnonReadOnly'
        ],
}

#3 Register the URL patterns
# urls.py
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
        path('admin/', admin.site.urls),
        path(
            '',
            TemiplateView.as_view(
                template_name = 'chapter_8/index.html'
            )
        ),
        path('api-auth/', include('rest_framework.urls'))
]

###### Serializer class based on Django REST framework

# cofeehouse.stores.serializers.py file
from rest_framework import serializers

class StoreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

###### Django view method decorated with Django REST framework

from coffeehouse.stores.models import Store
from coffeehouse.stores.serializers import StoreSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST','DELETE'])
def rest_store(request):
    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        ... # logic for HTTP POST operation
    elid request.method == 'DELETE':
        ... # logic for HTTP DELETE operation

###### Serializer class using Django model based on Django REST framework

from rest_framework import serializers
from coffeehouse.stores.models import Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

###### Django REST framework class-based views

from coffeehouse.stores.models import Store
from coffeehouse.stores.serializers import StoreSerializer

from rest_framework.views import APIVIew
from rest_framework.response import Response

class StoreList(APIView):

    def get(self, request, format=None):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        ...
        # logic for HTTP POST operation

    def delete(self, request, format=None):
        ...
        # logic for HTTP DELETE operation

###### Django URL definition linked to Django REST framework class-based views

from django.conf.urls import url
from coffeehouse.store import stores_views

urlpatterns = [
        url(r'^$',stores_views.index,name="index"),
        url(r'^rest/$',stores_views.StoreList.as_view(),name="rest_index"), ]

###### Django mixed_in generic class views in Django REST framework

from coffeehouse.stores.models import Store
from coffeehouse.stores.serializers import StoreSerializer

from rest_framework import generics

class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

###### Django viewset class in Django REST framework

from coffeehouse.stores.models import Store
from coffeehouse.stores.serializers import StoreSerializer

from rest_framework import viewsets

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

###### Django URL definition with Django REST framework router for view set 

from django.conf.urls import include, url
from coffeehouse.stores import views as stores_views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'stores', stores_views.StoreViewSet)

urlpatterns = [
        url(r'^rest/', include(router.urls,namespace="rest")),
        ]

###### Django REST framework set to restrict all services to authenticated users

REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        )
}

### Because DEFAULT is danger for sequrity 'rest_framework.pemissions.AllowAny' <--- Allow Any Carl! Allows access to anyone.

###### Django view method decorated with Django REST framework and @permission_classes decorator

from coffeehouse.stores.models import Store
from coffeehouse.stores.serializers import StoreSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET','POST','DELETE'])
@permission_classes((IsAuthenticated, ))
def rest_store(request):
    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

###### Django viewset class in Django REST framework and permission_classes field

from coffeehouse.stores.models import Store
from coffeehouse.stores.serializers import StoreSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets

class StoreViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

###### Django REST framework url declaration to enable log in

from django.conf.urls import include, url
urlpatterns = [
        url(r'^rest-auth/', include('rest_framework.urls',namespace='rest_framework')),
]

#100 Create serializers.py
from rest_framework.serializers import ModelSerializer
from ..chapter3.models import (
        Seller,
        Vehicle,
        Engine,
        VehicleModel
)

class EngineSerializer(ModelSerializer):
    class Meta:
        model = Engine,
        fields = '__all__'


class VehicleModelSerializer(ModelSerializer):
    class Meta:
        model = VehicleModel,
        fields = '__all__'


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle,
        fields = '__all__'


class SellerSerializer(ModleSerializer):
    class Meta:
        model = Seller,
        fields = '__all__'

#101 viewset classes
# views.py

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializer import (
        EngineSerializer,
        SellerSerializer,
        VehicleSerializer,
        VehicleModelSerializer
)
from ..chapter_3.models import(
        Engine,
        Seller,
        Vehicle,
        VehicleModel
)

class EngineViewSet(ModelViewSet):
    queryset = Engine.objects.all().order_by('name')
    serializer_class = EngineSerializer
    permission_classes = [IsAuthenticated]


class VehicleModelViewSet(ModelViewSet):
    queryset = VehicleModle.objects.all().order_by('name')
    serializer_class = VehicleModelSerializer
    permission_classes = [IsAuthenticated]


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all().order_by('price')
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]


class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsAuthenticated]

#102
