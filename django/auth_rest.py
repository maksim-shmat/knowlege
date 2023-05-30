"""Authenticating with tokens."""

#1 settings.py

INATALLED_APPS = [
        ...
        'rest_framework',
        'rest_framework.authtoken',
]

REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.
            TokenAuthentication',
            'rest_framework.authentication.
            SessionAuthentication',
            ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.
            DjangoModelPermissionsOrAnonReadOnly'
        ],
}

#2 
(virtual_env) python manage.py drf_create_token test

copy the token key

#3 views.py
...
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.viwes import APIView
from .serializers import SellerSerializer
from ..chapter_3.models import ..., Seller
...

class GetSellerWithTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, id=0, *args,
            **kwargs):
        seller = None
        req_user = request._user

        if req_user.has_perm('chapter_3.view_seller'):
            perm_granted = True

            try:
                seller = Seller.objects.get(id=id)
            except Seller.DoesNotExist:
                pass
        else:
            perm_granted = False
            
            context = {
