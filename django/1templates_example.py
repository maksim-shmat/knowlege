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

###########

