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

#########
