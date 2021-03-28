""" html for example in Django. """

# base_site.html
Then, edit file and replace {{ site_header|default:_('Django administration') }} with your own site`s name as you see fit. You should end up with a section
of code like:

{% block branding % }
<h1 id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a>
</h1>
{% endblock %}

########### min template for illustrates a bew basics
{% extends "base_generic.html" %}

{% block title %}{{ section.title }}{% endblock %}

{% block content %}
<h1>{{ section.title }}</h1>

{% for story in story_list %}
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}

########## template tags
# for 
<ul>
{% for athlete in athlete_list %}
  <li>{{ athlete.name }}</li>
{% endfor %}
</ul>

### if, elif, else
{% if athlete_list %}
  Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
  Athletes should be out of the locker room soon!
{% else %}
  No athletes.
{% endif %}

###
{% if athlete_list|length > 1 %}
  Team: {% for athlete in athlete_list %} ... {% endfor %}
{% else %}
  Athlete: {{ athlete_list.0.name }}
{% endif %}

########### template inheritance
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="style.css">
  <title>{% block title %}My amazing site{% endblock %}</title>
</head>

<body>
  <div id="sidebar">
    {% block sidebar %}
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/blog/">Blog</a></li>
    </ul>
    {% endblock %}
  </div>

  <div id="content".
    {% block content %}{% endblock %}
  </div>
</body>
</html>

###
{% extends "base.html" %}

{% block title %}My amazing blog{% endblock %}

{% block content %}
{% for entry in blog_entries %}
  <h2>{{ entry.title }}</h2>
  <p>{{ entry.body }}</p>
{% endfor %}
{% endblock %}

###
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="style.css">
  <title>My amazing blog</title>
</head>

<body>
  <div id="sidebar">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/blog/">Blog</a></li>
    </ul>
  </div>

  <div id="content">
    <h2>Entry one</h2>
    <p>This is my first entry.</p>

    <h2>Entry two</h2>
    <p>This is my second entry.</p>
  </div>
</body>
</html>

############# template cycle
{% for o in some_list %}
  <tr class="{% cycle 'row1' 'row2' %}">
    ...
  </tr>
{% endfor %}

###
{% for o in some_list %}
  <tr class="{% cycle rowvalue1 rowvalue2 %}">
    ...
  </tr>
{% endfor %}

###
{% for o in some_list %}
  <tr class="{% autoescape of %{% cycle rowvalue1 rowvalue2 %}{%
  endautoescape %}">
    ...
  </tr>
{% endfor %}

###
{% for o in some_list %}
  <tr class="{% cycle 'row1' rowvalue2 'row3' %}">
    ...
  </tr>
{% endfor %}

###
{% cycle 'row1' 'row2' as rowcolors %}

###
<tr>
  <td class="{% cycle 'row1' 'row2' as rowcolors %}">...</td>
  <td class="{{ rowcolors }}">...</td>
</tr>
<tr>
  <td class="{% cycle rowcolors %}">...</td>
  <td class="{{ rowcolors }}">...</td>
</tr>

###
<tr>
  <td class="row1">...</td>
  <td class="row1">...</td>
</tr>
<tr>
  <td class="row2">...</td>
  <td class="row2">...</td>
</tr>

###
{% for obj in some_list %}
  {% cycle 'row1' 'row2' as rowcolors silent %}
  <tr class ="{{ rowcolors }}">{% include "subtemplate.html" %}</tr>
{% endfor %}

###
{% cycle 'row1' 'row2' as rowcolors silent %}
{% cycle rowcolors %}

########### template for 
<ul>
{% for athlete in athlete_list %}
  <li>{{ athlete.name }}</li>
{% endfor %}
</ul>

###
{% for x, y in points %}
  There is a point at {{ x }}, {{ y }}
{% endfor %}

########## template for ... empty
<ul>
{% for athlete in athlete_list %}
  <li>{{ athlete.name }}</li>
{% empty %}
  <li>Sorry, no athletes in this list.</li>
{% endfor %}
</ul>

###
<ul>
  {% if athlete_list %}
    {% for athlete in athlete_list %}
      <li>{{ athlete.name }}</li>
    {% else %}
      <li>Sorry,no athletes in this list.</li>
    {% endif %}
</ul>

########## templates ifchanged
<h1>Archive for {{ year }}</h1>

{% for date in days %}
  {% ifchanged %}<h3>{{ date|date:"F" }}</h3>{% endifchanged %}
  <a href="{{ date|date:"M/d"|lower }}/">{{ date|date:"j" }}</a>

###
{% for date in days %}
  {% ifchanged date.date %} {{ date.date }} {% endifchanged %}
  {% ifchanged date.hour date.date %}
    {{ date.hour }}
  {% endifchanged %}
{% endfor %}

###
{% for match in matches %}
  <div style="background-color:
    {% ifchanged match.ballot_id %}
      {% cycle "red" "blue" %{
    {% else %}
      gray
    {% endifchanged %}
  ">{{ match }}</div>
{% endfor %}

########### template regroup
{% regroup cities by country as country_list %}
<ul>
{% for country in country_list %}
  <li>{{ country.grouper }}
  <ul>
    {% for city in country.list %}
      <li>{{ city.name }}: {{ city.population }}</li>
    {% endfor %}
  </ul>
  </li>
{% endfor %}
</ul>

###
{% regroup cities by country as country_list %}
<ul>
{% for country, local_cities in country_list %}
  <li>{{ country }}
  <ul>
    {% for city in local_cities %}
      <li>{{ city.name }}: {{ city.population }}</li>
    {% endfor %}
  </ul>
  </li>
{% endfor %}
</ul>

########### template resetcycle
{% for coach in coach_list %}
  <h1>{{ coach.name }}</h1>
  {% for athlete in coach.athlete_set.all %}
    <p class="{% cycle 'odd' 'even' %}">{{ athlete.name }}</p>
  {% endfor %}
  {% resetcycle %}
{% endfor %}

###
{% for item in list %}
  <p class="{% cycle 'odd' 'even' as stripe %} {% cycle 'major' 'minor' 'minor' 'minor' 'minor' as tick %}">
    {{ item.data }}
  </p>
  {% ifchanged item.category %}
    <h1>{{ item.category }}</h1>
    {% if not forloop.first %}{% resetcycle tick %}{% endif %}
  {% endifchanged %}
{% endfor %}

########## using request context
from django.http import HttpResponse
from django.template import RequestContext, Template

def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

def client_ip_view(request):
    template = Template('{{ title }}: {{ ip_address }}')
    context = RequestContext(request, {
        'title': 'Your IP Address',
    }, [ip_address_processor])
    return HttpResponse(template.render(context))

########## django {% static %} tag to reference static resources
{% load static %}

# For static resource at about/img/logo.png
<img src="{% static 'about/img/logo.gif' %}">

# For static resource at bootstrap/bootstrap.css
<link href="{% static 'bootstrap/bootstrap.css' %}" rel="stylesheet">

# For static resource at jquery/jquery.min.js
<script src="{% static 'jquery/jquery.min.js' %}"></script>

######## django collectstatic command to copy all static resources
[user@coffeehouse ~]$ python manage.py collectstatic

You have requested to collect static files at the destination
location as specified in your settings:

    /www/STORE/coffeestatic

This will overwrite existing files!
Are you sure you want to do this?

Type 'yes' to continue, or 'no' to cancel: yes
yes
Copying '/www/STORE/website-static-default/sitemap.xml'
Copying '/www/STORE/website-static-default/robots.txt'
Copying '/www/STORE/website-static-default/favicon.ico'
...
...
...
Copying '/www/STORE/coffeehouse/about/static/css/custom.css'

732 static files copied to '/www/STORE/coffeestatic'.

############# Permission checks in templates

{% if user.is_authenticated %}
  {# Content for authenticated users #}
{% endif %}

{% if perms.stores.add_store %}
  {# Content for users that can add stores #}
{% endif %}

{% for group in user.groups.all %}
  {% if group.name == 'Baristas' %}
    {# Content for users with 'Baristas' group #}
  {% endif %}
{% endfor %}

###### Content Tokens

from django.template import Lexer
template = 'This is {# only #}{ a }}{% test %}'
for token in Lexer(template, 'shell').tokenize():
    print('%s: %s' % (token.token_type, token.contents)

# 0: This is
# 3: only
# 1: a
# 2: test

###### Simple variable resolution for template context

from django.template.context import Context
c = Context({'a': 1, 'b': 2})
c['a'], c['b']
# (1, 2)
c.push()
c['a'], c['b']
# (1, 2)
c['b'] = 3
c['a'], c['b']
# (1, 3)
c.pop()
# {'b': 3}
c['a'], c['b']
# (1, 2)

######
