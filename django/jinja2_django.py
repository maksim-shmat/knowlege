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

##############
