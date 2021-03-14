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

######
