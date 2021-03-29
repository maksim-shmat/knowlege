"""Jinja template configuration in Django."""

# settings.py
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.jinja2.Jinja2',
            'DIRS': ['%s/jinjatemplates/'% (PROJECT_DIR),],
            'APP_DIRS': True,
            },
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates'
            'DIRS': []
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
]

########### jinja disable auto-escaping in django
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.jinja2.Jinja2',
            'DIRS': ['%s/jinjatemplates/'% (PROJECT_DIR),],
            'APP_DIRS': True,
            'OPTIONS': {
                'autoescape': False
            },
        }
]

######## generate error for invalid variables in Jinja with jinja2.StructUndefined
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

import jinja2

TEMPLATES = [
        {
            'BACKEND':'django.template.backends.jinja2.Jinja2',
            'DIRS': ['%s/jinjatemplates/'% (PROJECT_DIR),],
            'APP_DIRS': True,
            'OPTIONS':{
                'undefined':jinja2.StrictUndefined
            },
        }
]

######## jinja template with {% block %} tags
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Default title{% endblock title %}</title>
    <meta name="description" content="{% block metadescription %}{%endblock metadescription %}">
    <meta name="keywords" content="{% block metakeywords %}{% endblock metakeywords %}">

########## jinja template with {% extends %} and {% block %} tag
{% if user %}{% extends "base.html" %}{% else %}{% extends "signup_base.html" %}{% endif %}
{% block title %}Coffeehouse home page{% endblock %}

######### jinja templates use of super() with reusable templates
# base.html template
<p>{% block breadcrumb %}Home{% endblock %}</p>

# index.html template
{% extends "base.html" %}
{% block breadcrumb %}Main{% endblock %}

# detail.html template
{% extends "index.html" %}
{% block breadcrumb %} {{super()}} : Detail {% endblock %}

######### jinja {% macro %} definition and use of {% import %}
# base.html template
{% macro coffeestore(name, id='', address='', city='San Diego', state='CA', email=None) %}
  <a in="{{id}}"></a>
  <h4>{{name}}</h4>
  <p>{{address}} {{city}},{{state}}</p>
  {% if email %}<p><a href='mailto:{{email}}'>{{email}}</a></p>{% endif %}{% endmacro %}

# index.html template calls inherited macro directly
{% extends "base.html" %}
{{coffeestore('Downtown',1,'Horton Plaza','San Diego','CA','downtown@coffeehouse.com')}}

# detail.html template with no extends, uses {% import %} to access macroin base.html
{% import 'base.html' as base %}
{{base.coffeestore('Downtown',1,'Horton Plaza','San Diego','CA','downtown@coffeehouse.com')}}

# otherdetail.html template with no extends, uses {% from import %} to access macro in base.html
{% from 'base.html' import coffeestore as mycoffeestoremacro %}
{{mycoffeestoremacro('Downtown',1,'Horton Plaza','San Diego','CA', 'downtown@coffeehouse.com')}}

########## jinja {% call %}and{% macro %} use
# macro definition
{% macro contentlist(adcolumn_with=3,contentcolumn_with=6) %}
  <div class="col-md-{{adcolumn_width}}">
    Sidebar ads
  </div>
  <div class="col-md-{{contentcolumn_width}}">
    {{ caller() }}
  </div>
  <div class="col-md-{{adcolumn_width}}">
    Sidebar ads
  </div>
{% endmacro %}

# macro call/invocation
{% call contentlist() %}
  <ul>
    <li>This is my list</li>
  </ul>
{% endcall %}

# rendering
<div class="col-md-3">
  Sidebar ads
</div>
<div class="col-md-6">
  <ul>
    <li>This is my list</li>
  </ul>
</div>
<div class="col-md-3">
  Sidebar ads
</div>

############## jinja {% call %} and {% macro %} recursive calls
# macro definition
{% macro contentlist(itemlist,adcolumn_width=3,contentcolumn_width=6) %}
  <div class="col-md-{{adcolumn_width}}">
    Sidebar ads
  </div>
  <div class="col-md={{contentcolumn_width}}">
    {% for item in itemlist %}
      {{ caller(item) }}
    {% endfor %}
  </div>
  <div class="col-md-{{adcolumn_width}}">
    Sidebar ads
  </div>
{% endmacro %}

# variable definition
{% set coffeestores=[{'id':0,'name':'Corporate','address':'624 Broadway','city':'San Diego','state':'CA','email':'corporate@coffeehouse.com'},{'id':1,'name':'Downtown','address':'Horton Plaza','city':'San Diego','state':'CA','email':'downtown@coffeehouse.com'},{'id':2,'name':'Uptown','address':'1240 University Ave','city':'San Diego','state':'CA','email':'uptown@coffeehouse.com'},{'id':3,'name':'Midtown','address':'784 W Washington St','city':'San Diego','state':'CA','email':'midtown@coffeehouse.com'}] %}

# macro call/invocation
{% call(item) contentlist(coffeestores) %}
  <a id="{{item.id}}"></a>
  <h4>{{item.name}}</h4>
  <p>{{item.address}} {{item.city}},{{item.state}}</p>
  {% if item.email %}<p><a href='mailto:{{item.email}}'>{{item.email}}</a></p>{% endif %}
{% endcall %}

# rendering
<div class="col-md-3">
  Sidebar ads
</div>
<div class="col-md-6">
  <a id="O"></a>
  <h4>Corporate</h4>
  <p>624 Broadway San Diego,CA</p>
  <p><a href="mailto:corporate@coffeehouse.com">corporate@coffeehouse.com</a></p>

  <a id="1"></a>
  <h4>Downtown</h4>
  <p>Horton Plaza San Diego,CA</p>
  <p><a href="mailto:downtown@coffeehouse.com">downtown@coffeehouse.com</a></p>

  <a id="2"></a>
  <h4>Midtown</h4>
  <p>784 W Washington St San Diego,CA</p>
  <p><a href="mailto:midtown@coffeehouse.com">midtown@coffeeouse.com</a></p>
</div>
<div class="col-md-3">
  Sidebar ads
</div>

############ custom jinja environment with global variable
from jinja2.environment import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

class JinjaEnvironment(Environment):
    def __init__(self,**kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.globals['static'] = staticfiles_storage.url
        self.globals['reverse'] = reverse

########## configure custom jinja env in django settings.py
TEMPLATES = [
        {
            'BACKEND':'django.template.backends.jinja2.Jinja2',
            'DIRS': ['%s/templates/'% (PROJECT_DIR),],
            'APP_DIRS': True,
            'OPTIONS': {
                'environment': 'coffeehouse.jinja.env.JinjaEnvironment'
                }
            },
]

######### define a reference variable with {% set %} before entering the
# child loop to gain access to the parent loop
<ul>
{% for chapter in chapters %}
  {% set chapterloop = loop %}
  {% for section in chapter %}
    <li>"{{ chapterloop.index }}.{{ loop.index }}">{{ section }}</li>
  {% endfor %}
{% endfor %}
</ul>

########## jinja {% for %} statement with recursive keyword
# Dictionary definition
coffees={
        'espresso':{'nothing else': 'Espresso',
                    'water': 'Americano',
                    'steamed milk': {'more steamed milk than milk foam':'Latte',
                                     'chocolate syrup': {'Whipped cream': 'Mocha'}
                    },
                    'more milk foam steamed milk': 'Capuccino'
                    }
        }

# Template definition with for and recursive
{% for ingredient,result in coffees.iteritems() recursive %}
  <li>{{ ingredient }}
  {% if result is mapping %}
    <ul>{{ loop(result.iteritems()) }}</ul>
  {% else %}
    YOU GET: {{ result }}
  {% endif %}</li>
{% endfor %}

# Output
espresso
  water YOU GET: Americano
  steamed milk
    more steamed milk than milk foam YOU GET: Latte
    chocolate syrup
      Whipped cream YOU GET: Mocha
  more milk foam than steamed milk YOU GET: Capuccino
  nothing else YOU GET: Espresso

############# jinja cycler function
{% set row_class = cycler('white', 'lightgrey','grey') %}

<ul>
{% for item in items %}
  <li class="{{ row_class.next() }}">{{ item }}</li>
{% endfor %}
{% for otheritem in moreitems %}
  <li class="{{ row_class.next() }}">{{ otheritem }}</li>
{% endfor %}

# Output
<ul>
  <li class="white">Item 1</li>
  <li class="lightgrey">Item 2</li>
  <li class="grey">Item 3</li>
  <li class="white">Item 4</li>
  <li class="lightgrey">Item 5</li>
  <li class="grey">Other item 1</li>
  <li class="white">Othe item 2</li>
</ul>

########## jinja joiner function
{% set slash_joiner = joiner("/ ") %}

User: {% if username %} {{ slash_joiner() }}
  {{username}}
{% endif %}
{% if alias %} {{ slash_joiner() }}
  {{alias}}
{% endif %}
{% if nickname %} {{ slach_joiner() }}
  {{nickname}}
{% endif %}

# Output
# If all variables are defined
User: username / alias / nickname
# If only nickname is defined
User: nickname
# If only username and alias is defined
User: username / alias
# Etc, the joiner function avoids any unnecessary preceding slash because it doesn't print anything the first time its called

######## spacing and special characters
# default space rendering in jinja template
<div>
  {% for drink in drinks %}
    {{drink}}
  {% endfor %}
</div>

<div>  {% if drinks_on_sale %} Drinks on sale! {% endif %}

### space rendering in jinja template with single -
<div>
  {% for drink in drinks -%}
    {{drinks}}
</div>

<div>  {% if drinks_on_sale -%} Drinks on sale! {% endif %}

### space rendering in jinja template with double -
<div>
  {% for drink in drinks -%}
    {{drink}}
  {%- endfor %}
</div>

<div>  {% if drinks_on_sale -%} Drinks on sale! {%- endif %}

### space rendering in jinja template with trim_blocks
<div>
  {% for drink in drinks %}
    {{drink}}
  {% endfor %}
</div>

<div>  {% if drinks_on_sale %} Drinks on sale! {% endif %}

### space rendering in jinja template with both trim_blocks and lstrip_blocks set to True
<div>
  {% for drink in drinks %}
    {{drink}}
  {% endfor %}
</div>

<div>  {% if drinks_on_sale %} Drinks on sale! {% endif %}

########## jinja defined test
{% if variable is defined %}
  value of variable: {{ variable }}
{% else %}
  variable is not definde
{% endif %}

########### jinja groupby filter
# Dictionary definition
stores = [
        {'name': 'Downtown', 'street': '385 Main Street', 'city': 'San Diego'},
        {'name': 'Uptown', 'street': '231 Highland Avenue', 'city': 'San Diego'},
        {'name': 'Midtown', 'street': '85 Balboa Street', 'city': 'San Diego'},
        {'name': 'Downtown', 'street': '1407 Broadway Street', 'city': 'Los Angeles'},
        {'name': 'Downtown', 'street': '50 1st Street', 'city': 'San Francisco'},
]

<ul>
{% for group in stores|groupby('city') %}
  <li>{{ group.grouper }}
  <ul>
    {% for item in group.list %}
      <li>{{ item.name }}: {{ itme.street }}</li>
    {% endfor %}
  </ul>
  </li>
{% endfor % }
</ul>

# Output
Los Angeles
  Downtown: 639 Spring Street
  Midtown: 1407 Broadway Street
San Diego
  Downtown: 385 Main Street
  Uptown: 231 Highland Avenue
  Midtown: 85 Balboa Street
San Francisco
  Downtown: 50 1st Street

# Alternate shortcut syntax, produces same output
<ul>
{% for grouper, list in stores|groupby('city') %}
  <li>{{ grouper }}
  <ul>
    {% for item in list %}
      <li>{{ item.name }}: {{ item.street }}</li>
    {% endfor %}
  </ul>
  </li>
{% endfor %}
</ul>

########### jinja wordwrap filter
# Variable definition
Coffeehouse started as a smaoo store

# Template definition with wordwrap filter for every 12 characters
{{variable|wordwrap(12)}}

# Output
Coffeehouse
started as a
small store

########## django xmlattr filter
# Variable definition
{% set stores = [
    {'id': 123, 'name': 'Downtown', 'street': '385 Main Street', 'city': 'San Diego'},
    {'id': 243, 'name': 'Uptown', 'street': '231 Highland Avenue', 'city': 'San Diego'},
    {'id': 357, 'name': 'Midtown', 'street': '85 Balboa Street', 'city': 'San Diego'},
    {'id': 478, 'name': 'Downtown', 'street': '639 Spring Street', 'city': 'Los Angeles'},
    {'id': 529, 'name': 'Midtown', 'street': '1407 Broadway Street', 'city': 'Los Angeles'},
    {'id': 653, 'name': 'Downtown', 'street': '50 1st Street', 'city': 'San Francisco'},
] %}

# Template definition
<ul>
{% for store in stores %}
  <li {{ {'id':'%d'|format(store.id),'class':'%s'|format(store.city|lower|replace(' ','-'))}|xmlattr }}> {{store.city}} {{store.name}}</li>
{% endfor %}
</ul>

# Output
<ul>
  <li id="123" class="san-diego"> San Diego Downtown</li>
  <li id="243" class="san-diego"> San Diego Uptown</li>
  <li id="357" class="san-diego"> San Diego Midtown</li>
  <li id="478" class="los-angeles"> Los Angeles Downtown</li>
  <li id="529" class="los-angeles"> Los Angeles Midtown</li>
  <li id="653" class="san-francisco"> San Francisco Downtown</li>
</ul>

########### backing Python methods for Jinja custom filters and tests
import jinja2

def customcoffee(value,arg="muted"):
    return jinja2.Markup('%s' % (arg,value))

import math

def squarerootintext(value):
    return "The square root of %s is %s" % (value,math.sqrt(value))

def startswithvowel(value):
    if value.lower().startswith(("a", "e", "i", "o", "u")):
        return True
    else:
        return False

############ custom jinja environment with custom filters and tests
from jinja2.environment import Environment
from coffeehouse.jinja.filters import customcoffee, squarerootintext, strtswithvowel

class JinjaEnvironment(Environment):
    def __init__(self, **kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.filters['customcoffee'] = customcoffee
        self.filters['squarerootintext'] = squarerootintext
        self.filters['startswithvowel'] = startswithvowel
        self.tests['startswithvowel'] = startwithvowel

########### configure custom jinja environment in Django settings.py
TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.jinja2.Jinja2',
            'DIRS': ['%s/templates/'% (PROJECT_DIR),],
            'APP_DIRS': True,
            'OPTIONS': {
                'environment': 'coffeehouse.jinja.env.JinjaEnvironment'
                }
            },
]

######### jinja extension configuration in Django
TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.jinja2.Jinja2',
            'DIRS': ['%s/templates/'% (PROJECT_DIR),],
            'APP_DIRS': True,
            'OPTIONS': {
                'extensions': [
                    'jinja2.ext.loopcontrols',
                    'jdj_tags.extensions.DjangoCompat',
                    'coffeehouse.jinja.extensions.DjangoNow',
                    ],
            }
        }
]

########## jinja custom extension for Jinja {% now %} statement
from jinja2 import lexer, nodes
from jinja2.ext import Extension
from django.utils import timezone
from django.template.defaultfilter import date
from django.conf import settings
from datetime import datetime

class DjangoNow(Extension):
    tags = set(['now'])

    def _now(self, date_format):
        tzinfo = timezone.get_current_timezone() if settings.USE_TZ else None
        formatted = date(datetime.now(tz=tzinfo), date_format)
        return formatted

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        token = parser.stream.expect(lexer.TOKEN_STRING)
        date_format = nodes.Const(token.value)
        call = self.call_method('_now', [date_format], lineno=lineno)
        token = parser.stream.current
        if token.test('name:as'):
            next(parser.stream)
            as_var = parser.stream.expect(lexer.TOKEN_NAME)
            as_var = nodes.Name(as_var.value, 'store', lineno=as_var.lineno)
            return nodes.Assign(as_var, call, lineno=lineno)
        else:
            return nodes.Output([call], lineno=lineno)

########### custom jinja environvent with policies
from jinja2.environment import Environment
from coffeehouse.jinja.filters import customcoffee, squarerootintext, startswithvowel

class JinjaEnvironvent(Environment):
    def __init__(self, **kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.policies['truncate.leeway'] = 0

########## Calculate the value before sending it to the tmplate

{% load jinja %}

{% for property in object_list %}
Address: {{ property.address }}
Internal area: {{ property.square_feet }} square feet
Lot size: {{ property.lot_width }}' by {{ property.lot_depth }}'

{% jinja %}
Lot area: {{ property.lot_width * property.lot_depth / 43560 }} acres
{% endjinja %}
{% endfor %}

###### Compiling a Node

import jinja2
from django import template
from django.base import TemplateSyntaxError

register = template.Library()

def jinja(parser, token):
    """
    Define a block that gets rendered by Jinja, rather than Django's templates.
    """
    bits = token.contents.split()
    if len(bits) != 1:
        raise TemplateSyntaxError("'%s' tag doesn't take any arguments." % bits[0])
    # Manually collect tokens for the tag's content, so Django's template
    # parser doesn't try to make sense of it.
    contents = []
    while 1:
        try:
            token = parser.next_token()
        except IndexError:
            # Reached the end of the template without finding the end tag
            raise TemplateSyntaxError("'endjinja' tag is required.")
        if token.token_type == template.TOKEN_BLOCK and \
                token.contents == 'endjinja':
                    break
        contents.append(string_from_token(token))
    contents = ''.join(contents)

    return JinjaNode(jinja2.Template(contents))
jinja = register.tat(jinja)

###### Preparing the Jinja Template

import jinja2

class JinjaNode(template.Node):
    def __init__(self, template):
        self.template = template

    def render(self, django_context):
        # Jinja can't use Django's Context objects, so we have to
        # flatten it out to a single dictionary before using it.
        jinja_context = {}
        for layer in django_context:
            for key, value in layer.items():
                if key not in jinja_context:
                    jinja_context[key] = value
        return self.template.render(jinja_context)

######
