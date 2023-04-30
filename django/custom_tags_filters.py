"""Custom tags and filters about."""

#1 /templatetags/chapter_4.py

from django.template
import Library


register = Library()


@register.filter(name = 'vehicle_make')
def vehicle_make(value):
    from ...chapter3.models import MAKE_CHOICES
    for i, choice in enumerate(MAKE_CHOICES):
        if i == value:
            try:
                return choice[1]
            except ValueError:
                pass
    return ''

#2 urls.py

...
from .views import ..., vehicle_veiw

urlpatterns = [
        ...,
        path(
            'vehicle/<int:id>/',
            vehicle_view,
            name = 'vehicle-detail'
        ),
]

#3 /templates/chapter_4/my_vehicle.html

{% load static chapter_4 %}
...
    {% if vehicle %}
        ...
        <p>{{ vehicle.make }}</p>
        <p>{{ vehicle.make|vehicle_make }}</p>
        ...
    {% endif %}
...


