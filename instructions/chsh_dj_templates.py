"""Cheat sheet django about."""

# Snippets for Django templates

autoescape  {% autoescape %} {% autoescape %}

block       {% block %} {% endblock %}

comment     {% comment %} {% endcomment %}

csrf        {% csrf_token %}

cycle       {% cycle %}

debug       {% debug %}

ext/extends {% extends "" %}

filter      {% filter %} {% endfilter %}

firstof     {% firstof %}

for         {% for in %} {% endfor %}

fore        {% for in %} {% empty %} {% endfor %}

if          {% if %} {% endif %}

if changed  {% ifchanged %} {% endifchanged %}

ife/ifelse  {% if %} {% else %} {% endif %}

ifeq/ifequal {% ifequal %} { % endifequal %}

ifnotequal  {% ifnotequal %} {% endifnotequal %}

inc/include {% include %}

load        {% load %}

now         {% now "" %}

regroup     {% regroup by as %}

spaceless   {% spaceless %} {% endspaceless %}

ssi         {% ssi %}

static      {% static %}

templatetag {% templatetag %}

url         {% url %}

verbatim    {% verbatim %} {% endverbatim %}

widthratio  {% widthratio %}

with        {% with as %} {% endwith %}

trans       {% trans %}

blocktrans  {% blocktrans with as %} {% endblocktrans %}

# Non-official snippets for templates

super       {{ block.super }}

extrahead   {% block extrahead %} {% endblock extrahead %}

extrastyle  {% block extrastyle %} {% endblock extrastyle %}

var         {{ }}

tag         {% %}

static url   {{ STATIC_URL }}

media url    {{ MEDIA_URL }}



