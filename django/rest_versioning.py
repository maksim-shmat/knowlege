"""Django REST versioning about."""


#1 settings.py

REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': (
            'drones.custompagination.LimitOffsetPaginationWithUpperBound',
        ),
        'PAGE_SIZE': 4,
        'DEFAULT_FILTER_BACKENDS': (
            'django_filters.rest_framework.DjangoFilterBackend',
            'rest_framework.filters.OrderingFilter',
            'rest_framework.filters.SearchFilter',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ),
        'DEFAULT_THROTTLE_RATES': {
            'anon': '3/hour',
            'user': '10/hour',
            'drones': '20/hour',
            'pilots': '15/hour',
        },
        'DEFAULT_VERSIONING_CLASS': (
            'rest_framework.versioning.NamespaceVersioning',
        ),
}

#2 views.py v2

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drones import views


class ApiRootVersioning2(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'vehicsle-categories': reverse(views.DroneCategoryList.name, request=request),
            'vehicles': reverse(views.DroneList.name, request=request),
            'pilots': reverse(views.PilotList.name, request=request),
            'competitions': reverse(views.CompetitionList.name, request=request)
        })

#3 urls.py v2

from django.conf.urls import url
from drones import views
from drones.v2 import views as views_v2


urlpatterns = [
        url(r'^vehicle-categories/$',
            views.DroneCategoryList.name),
        url(r'^vehicle-categories/(?P<pk>[0-9]+)$',
            views.DroneCategoryDetail.as_view(),
            name=views.DroneCategoryDetail.name),
        url(r'^vehicles/$',
            views.DronList.as_veiw(),
            name=views.DroneList.name),
        url(r'^vehicles/(?P<pk>[0-9]+)$',
            views.DroneDetail.as_view(),
            name=views.DroneDetail.name),
        url(r'^pilots/$',
            views.PilotList.as_view(),
            name=views.PilotList.name),
        url(r'^pilots/(?P<pk>[0-9]+)$',
            views.PilotDetail.as_view(),
            name=views.PilotDetail.name),
        url(r'^competitions/$',
            views.CompetitionList.as_view(),
            name=views.CompetitionList.name),
        url(r'^competitions/(?P<pk>[0-9]+)$',
            views.CompetitionDetail.as_view(),
            name=views.CompetitionDetail.name),
        url(r'^S',
            views_v2.ApiRootVersion2.as_view(),
            name = views_v2.ApiRootVersion2.name),
]


#4 other version urls.py

from django.conf.urls import url, include


urlpatterns = [
        url(r'^v1/', include('drones.urls', namespace='v1')),
        url(r'^v1/api-auth/', include('rest_framework.urls',
            namespace='rest_framework_v1')),
        url(r'^v2/', include('drones.v2.urls', namespace='v2')),
        url(r'^v2/api-auth/', include('rest_framework.urls',
            namespace='rest_framework_v2')),
        ]
