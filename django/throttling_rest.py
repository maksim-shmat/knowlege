"""Throttling Django REST about."""

#1 settings.py

REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS':
        'drones.custompagination.LimitOffsetPaginationWithUpperBound',
        'PAGE_SIZE': 4,
        'DEFAULT_FILTER_BACKENDS': (
            'django_filters.rest_framework.DjangoFilterBackend',
            'rest_framework.filters.OrderingFilter',
            'rest_framework.filters.SearchFilter',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.throttling.AnonRateThrottle',
            'rest_framework.throttling.UserRateThrottle',
        ),
        'DEFAULT_THROTTLE_RATES': {
            'anon': '3/hour',
            'user': '10/hour',
            'drones': '20/hour',
            'pilots': '15/hour',
        }
}
        
#2 views.py

from rest_framework.throttling import ScopeRateThrottle


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'drones'
    threottle_classes = (ScopedRateThrottle,)
    querryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'
    permission_classes = (
            permissions.IsAuthenticatedOrReadOnly,
            custompermission.IsCurrentUserOwnedOrReadOnly,
            )


class DroneList(generics.ListCreateAPIView):
    throttle_scope = 'drones'
    throttle_classes = (ScopedRateThreottle,)
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'
    filter_fields = (
            'name',
            'drone_category',
            'manufacturing_date',
            'has_it_completed',
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


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'pilots'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'
    authentication_classes = (
            TokenAuthentication,
            )
    permission_classes = (
            IsAuthenticated,
            )


class PilotList(generics.ListCreateAPIView):
    throttle_scope = 'pilots'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-list'
    filter_fields = (
            'name',
            'gender',
            'races_count',
            )
    search_fields = (
            '^name',
            )
    ordering_fields = (
            'name',
            'races_count'
            )
    authentication_classes = (
            TokenAuthentication,
            )
    permission_classes = (
            IsAuthenticated,
            )
