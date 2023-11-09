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

#3 Saving information about users that make request
# view.py

class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'
    filter_fields = (
            'name',
            'drone_category',
            'manufacturing_date',
            'has_it_copleted',
            )
    search_fields = (
            '^name',
            )
    ordering_fields = (
            'name',
            'manufacturing_date',
            )
    permission_classes = (
            permissions.IsAuthenticatedOrReadOnly,
            custompermission.IsCurrentUserOwnerOrReadOnly,
            )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#4 Setting permission policies
# view.py

class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'
    permission_classes = (
            permissions.IsAuthenticatedOrReadOnly,
            custompermission.IsCurrentUserOwnerOrReadOnly,
            )

#5 serializer.py

from rest_framework import serializers
from posts import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ("posted_by_id", "message")

# apiviews.py

from rest_framework.views import APIView
from rest_framework.response import Response

from posts import models
from .serializers import PostSerializer


class PublicPostList(APIView):
    """Retrurn the most recent public posts by all users."""
    def get(self, request):
        msgs = models.Post.objects.public_posts()[:5]
        data = PostSerializer(msgs, many=True).data
        return Response(data)

# urls.py

path('api/public/',
        apiviews.PublicPostList.as_view(), name="api_public")

# go to http://127.0.0.1:8000/api/public/

#6 Hiding th IDs

class PostSerializer(serializer.ModelSerializer):
    posted_by = serializers.SerializerMethodField()

    def get_posted_by(self, obj):
        return obj.posteed_by.username

    class Meta:
        model = models.Post
        fields = ("posted_by", "message",)

#7 Human browsable interface

# urls.py

from rest_framework.decumentation import include_docs_urls

urlpatterns = [
        path('api-docs/', include_docs_urls(title='My API')),
]

#8  
