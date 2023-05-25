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
