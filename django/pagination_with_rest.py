"""Pagination with Django REST framework."""

#1 Configuring pagination classes
# on the settings

REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 4
}

#2
