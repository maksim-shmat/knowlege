"""Active link pattern about."""

#1 template

{% include "_navbar.html" with active_link='link2' %}

#
{# _navbar.html #}

<ul class="nav nav-pills">
  <li{% if active_link == "link1" %} class="active"{% endif %}><a href="{% url 'link1' %}">Link 1</a></li>
  <li{% if active_link == "link2" %} class="active"{% endif %}><a href="{% url 'link2' %}">Link 2</a></li>
  <li{% if active_link == "link3" %} class="active"{% endif %}><a href="{% url 'link3' %}">Link 3</a></li>
</ul>

#3 Custom tags

# add empty __init__.py file to app/templates/ directory
# app/templates/nav.py

from django.core.urlresolvers import resolve
from django.template import Library


register = Library()
@register.simple_tag
def active_nav(request, url):
    url_name = resolve(request.path).url_name
    if url_name == url:
        return "active"
    return ""

# settings.py
[
        'django.core.context_processing.request',
]

#

{# base.html #}
{% load nav %}
<ul class="nav nav-pills">
  <li class={% active_nav request 'active1' %}><a href="{% url 'active1' %}">Active 1</a></li>
  <li class={% active_nav request 'active2' %}><a href="{% url 'active2' %}">Active 2</a></li>
  <li class={% active_nav request 'active3' %}><a href="{% url 'active3' %}">Active 3</a></li>
</ul>
