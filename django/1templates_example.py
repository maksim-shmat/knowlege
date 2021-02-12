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

##########
