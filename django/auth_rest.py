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
                    'request': request,
                    'seller': seller,
            }

            seller = SellerSerializer(
                    seller,
                    context = context
            )

            new_context = {
                    'seller': seller.data,
                    'perm_granted': perm_granted
            }

            return JsonResponse(new_context)

#4 site-js.js
function $gotoSPA_Page() {
        ...
        var url = `/chapter-8/sellertoken/${id}/`;

        fetch(url, {
            method: `GET`,
            headers: {
                `Content-Type`: `application/json`,
                `Authorization`: `Token your_token`,
                `User`: `test`
        }}).token(async(response) => {
            return await response.text();
        }).then(async(data) => {
            container.innerHTML = await data;
        });
}

#5 urls.py
from .view import ..., GetSellerView, GetSellerHTMLView,
GetSellerWithTokenView
...
urlpatterns = [
        ...
        path(
            'chapter-8/get-seller/',
            GetSellerView.as_view(),
            name = 'get-seller'
        ),
        path(
            'chapter-8/seller/<int:id>/',
            GetSellerHTMLView.as_view(),
            name = 'seller-detail'
        ),
        path(
            'chapter-8/sellertoken/<int:id>/',
            GetSellerWithTokenView.as_view(),
            name = 'seller-token-detail'
        ),
]
