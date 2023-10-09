"""For Django REST examples."""

#1 check the email_ex
...
from rest_framework.serializers import (
        HyperlinkedModelSerializer,
        ModelSerializer
)


class SellerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Seller,
        #fields = '__all__',
        excude = ['groups', 'user_permissions']

#2 For Django REST authentication, first settings.py, second models.py, and then this

from django.contrib.auth.models import User


class UserDroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drone
        fields = (
                'url',
                'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    drones = UserDroneSerializer(
            many=True,
            read_only=True)

    class Meta:
        model = User
        fields = (
                'url',
                'pk',
                'username',
                'drone')


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    # Display the category name
    drone_category = 
    serializers.SlugRelatedField(queryset=DroneCategory.objects.all(),
            slug_field='name')
    # Display the owner's username (read-only)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Drone
        fields = (
                'url',
                'name',
                'drone_category',
                'owner',
                'manufacturing_date',
                'has_it_completed',
                'inserted_timestamp',)

#3
