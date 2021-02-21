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

#########
