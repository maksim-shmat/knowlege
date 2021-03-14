""" About Django REST(Representational state transfer)."""

# first install it:
pip3 install djangorestframework

# then add to the INSTALLED_APPS in settings.py with name
rest_framework

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

######
