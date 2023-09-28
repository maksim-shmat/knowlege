"""Pagination with Django REST framework."""

#1 Configuring pagination classes
# on the settings

REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 4
}

#2 other side
# custompagination.py

from rest_framework.pagination import LimitOffsetPagination

class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
    # Set the maximum limit value to 8
    max_limit = 8

# settings.py

REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS':
        'drones.custompagination.LimitOffsetPaginationWithUpperBound',
        'PAGE_SIZE': 4
}

#3
