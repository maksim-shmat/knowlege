"""Filetering with Django RESTful, about."""

#1 settings.py

REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS':
        'drones.custompagination.LimitOffsetPaginationWithBound',
        'PAGE_SIZE': 4,
        'DEFAULT_FILTER_BACKENDS': (
            'django_filters.rest_framework.DjangoFilterBackend',
            'rest_framework.filters.OrderingFilter',
            'rest_framework.filters.SearchFilter',
        ),
}

INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Django REST Framework
        'rest_framework',
        # Drones application
        'drones.apps.DronesConfig',
        # Django Filters,
        'django_filters',
]

#2 views.py

class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-list'
    filter_fields = (
            'name',
            'gender',
            'races_count',
            'drone_category',
            'manufacturing_date',
            'has_it_competed',
            )
    search_fields = (
            '^name',
            )
    ordering_fields = (
            'name',
            'races_count'
            'manufacturing_date',
            )


class CompetitionFilter(filters.FilterSet):
    from_achivement_date = DateTimeFilter(
            name='distance_achivement_date', lookup_expr='gte')
    to_achivement_date = DateTimeFilter(
            name='distance_achivement_date', lookup_expr='lte')
    min_distance_in_feet = NumberFilter(
            name='distance_in_feet' = lookup_expr='gte')
    max_distance_in_feet = NumberFilter(
            name='distance_in_feet' = lookup_expr='lte')
    drone_name = AllValuesFilter(
            name='dron__name')
    pilot_name = AllValuesFilter(
            name='pilot__name')

    class Meta:
        model = Competition
        fields = (
                'distance_in_feet',
                'from_achievement_date',
                'to_achievement_date',
                'min_distance_in_feet',
                'max_distance_in_feet',
                # drone__name will be accessed as drone_name
                'drone_name',
                # pilot__name will be acdessed as pilot_name
                'pilot_name',
                )

#3
