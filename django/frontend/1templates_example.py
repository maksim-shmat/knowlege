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

###### Complex Variable Lookup

from django.template import Variable
c = Context({'var': [1, 2, {'spam': u'eggs'}]})
var = Variable('var')
zero = Varible('var.0')
one = Variable('var.1')
spam = Variable('var.2.spam')

var.resolve(c)
# [1, 2, {'spam': u'eggs'}]
zero.resolve(c)
# 1
one.resolve(c)
# 2
spam.resolve(c)
# u'eggs'

##### django.template.loader.select_template(template_name_list)

from django.template import loader
t = loader.get_template('property/listing.html')
t.name
# error
#django.template.TemplateDoesNotExist: properyty/listing_123.html
t = loader.select_template(['property/listing_123.html',
                            'property/listing.html'])
t.name
# 'property/listing.html'

###### Variable Filters

from django.template import Library
from django.template.defaultfilters import stringfilter

register = Library()

@register.filter
@stringfilter
def firts(value, count=1):
    """
    Returns the first portion of a string, according to the count provided.
    """
    return value[:count]

###### A Simple Tag

from django.template import Library, Node, Variable

register = Library()

class FirstNode(Node):
    def __init__(self, var, count):
        self.var = var
        self.count = count

    def render(self, context):
        value = self.var.resolve(context)
        return value[:self.count]

###
@register.tag
def first(parser, token):
    var, count = token.split contents()[1:]
    return FirstNode(Variable(var), int(count))

### a shortcut for Simple Tags
from django.template import Library

register = Library()

@register.simle_tag
def first(value, count):
    return value[:count]

###### Converting a Token to a String 

from django import template

def string_from_token(token):
    """
    Converts a lexer token back into a string for use with Jinja.
    """
    if token.token_type == template.TOKEN_TEXT:
        return token.contents
    elif token.token_type == template.TOKEN_VAR:
        return '%s %s %s' % (
                template.VARIABLE_TAG_START,
                token.contents,
                template.VARIABLE_TAG_END,
        )

    elif token.token_type == template.TOKEN_BLOCK:
        return '%s %s %s' % (
                template.BLOCK_TAG_START,
                token.contents,
                template.BLOCK_TAG_END,
        )
    elif token.token_type == template.TOKEN_COMMENT:
        return u'' # Django doesn't store the content of comments

###### Setting Up the Models

from django.db import models
from django import template
from django.contrib.auth.models import User
from themes.managers import ThemeManager

class Theme(models.Model, template.Template):
    EDITING, PENDING, APPROVED = range(3)
    STATUS_CHOICES = (
            (EDITING, u'Editing'),
            (PENDING, u'Pending Approval'),
            (APPROVED, u'Approved'),
    )
    author = models.ForeignKey(User, related_name='authored_themes')
    title = models.CharField(max_length=255)
    template_string = models.TextField()
    css = models.URLField(null=True, blank=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=EDITING)
    is_default = models.BooleanField()

    objects = ThemeManager()

    def __init__(self, *args, **kwargs):
        # super() won't work here, because the two __init__()
        # method signatures accept different sets of arguments
        models.Model.__init__(self, *args, **kwargs)
        template.Template.__init__(self, self.template_string,
                                   origin=repr(self), name=unicode(self))

    def save(self):
        if self.is_default:
            # Since only one theme can be the site-wide default, any new modelthat
            # is defined as default must remove the default setting from any other
            # theme before committing to the database.
            self.objects.all().update(is_default=False)
        super(Theme, self).save()
    
    def __unicode__(self):
        return self.title

### theme for only one user
class Theme(models.Model):
    ... # All the other fields shown above
    users = models.ManyToManyField(User, through='SelectedTheme')
    ... # All the other methods shown above

class SelectedTheme(models.Model):
    user = models.OneToOneField(User)
    theme = models.ForeignKey(Theme)

### theme manager
from django.db import models
from django.conf import settings

class ThemeManager(models.Manager):
    def by_author(self, user):
        """
        A convenience method for retrieving the themes a user has authored.
        Since the only time we'll be retrieving themes by author is when
        they're being edited, this also limits the query to those themes
        that haven't yet been submitted for review
        """
        return self.filter(author=self, status=self.model.EDITING)

    def get_current_theme(self, user):
        return SelectedTheme.objects.get(user=user).theme

##### Supporting Site-Wide Themes
# it is use context processor without middleware
from django.conf import settings
from themes.models import Theme

def theme(request):
    if hasattr(request, 'use') and request.user.is_authenticated():
        # A valid user is logged in, so use the manager method
        theme = Theme.objects.get_current_theme(request.user)
    else:
        # The user isn't logged in, so fall back to the default
        theme = Theme.objects.get(is_default=True)
    name = getattr(settings, 'THEME_CONTEXT_NAME', 'theme')
    return {name: theme}

##### Validating and Securing Themes

from django import forms
from django.import template
from django.template.loader_tags import BlockNode, ExtendsNode
from django.conf import settings
from theme import models

class ThemeForm(form.ModelForm):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

    def clean_body(self):
        try:
            tpl = template.Template(self.cleaned_data['body'])
        except template.TemplateSyntaxError as e:
            # The template is invalid, which is an input error.
            raise forms.ValidationError(unicode(e))

        if [type(n) for n in tpl.nodelist] != [ExtendsNode] or \
                tpl.nodelist[0].parent_name != settings.TEME_EXTENDS:
                    # No 'extends' tag was found
                    error_msg = u"Template must extend '%s'" % settings.THEME_EXTENDS
                    raise forms.ValidationError(error_msg)

        if [type(n) for n in tpl.nodelist[0].nodelist] != [BlockNode] or \
                tpl.nodelist[0].nodelist[0].name != settings.THEME_CONTAINER_BLOCK:
                    # Didn't find exactly one block tat with the required name
                    error_msg = u"Theme needs exactly one '%s' block" % \
                            settings.THEME_CONTAINER_BLOCK
                    raise forms.ValidationError(error_msg)

        required_blocks = list(settings.THEME_BLOCKS[:])
        for node in tpl.nodelist[0].nodelist[0].nodelist:
            if type(node) is BlockNode:
                if node.name not in required_blocks:
                    error_msg = u"'%s' is not valid for themes." % node.name)
                    raise forms.ValidationError(error_msg)
                    required_blocks.remove(node.name)
                    if node.nodelist:
                        error_msg = u"'%s' block must be empty." % node.name)
                        raise forms.ValidationError(error_msg)
                    elif type(node) is template.TextNode:
                        # Text nodes between blocks are acceptable.
                        pass
                    else:
                        # All other tags, including variables, are invalid.
                        error_msg = u"Only 'extends', 'block' and plain text are allowed."
                        raise forms.ValidationError(error_msg)

                if required_blocks:
                    # Some blocks were missing from the template.
                    blocks = ', '.join(map(repr, required_blocks))
                    error_msg = u"The following blocks must be defined: %s" % blocks
                    raise forms.ValidationError(error_msg)

            class Meta:
                model = models.Theme

###### An Example Theme for site

THEME_EXTENDS = 'base.html'
THEME_CONTEXT_NAME = 'theme'
THEME_CONTAINER_BLOCK = 'theme'
THEME_BLOCK = (
        'title',
        'sidebar',
        'links',
)

# the base.html template at eh root of the inheritance chain might look like
<html>
<head>
<title>{% block title %}{% endblock %}</title>
<link rel="stylesheet" type="text/css" href="/style.css"/>
</head>
<body>{% block theme %}{% endblock %}</body>
<html>

# exemplar THEME model
{% extends 'base.html' %}

{% block theme %}
<h1>{% block title %}{% endblock %}</h1>
<ul id="links">{% block links %}{% endblock %}</ul>
<div id="content">{% block content %}{% endblock %}</div>
{% endblock %}

# consider the template for the root of a real estate site
{% extends theme %}

{% block title %}Acme Real Estate{% endblock %}

{% block links %}
<li><a href="{% url home_page %}">Home</a></li>
<li><a href="{% url property_list %}">Properties></a></li>
<li><a href="{% url about_page %}">About</a></li>
{% endblock %}

{% block content %}
<p>Welcome to Acme Real Estate!</p>
{% endblock %}

# and loading full HTML
<html>
<head>
<title>Acme Real Estate</title>
<link rel="stylesheet" type="text/css" href="/style.css"/>
</head>
<body>
<h1>Acme Real Estate</h1>
<ul id="links">
<li><a href="/">Home</a></li>
<li><a href="/properties/">Properties</a></li>
<li><a href="/abut/">About</a></li>
</ul>
<div id="content".
<p>Welcome to Acme Real Estate!</p>
</div>
</body>
</html>

######
