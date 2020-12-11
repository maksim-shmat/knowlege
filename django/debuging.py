""" in tdd.py - testing info, thats it each debuging. """

for debug templates:

TEMPLATE_DEBUB to True (in addition to DEBUG) in settings.py

{% debug %} is a tag of debug, insert in in code

<textarea onclick="this.focus();this.select()" style="width: 100%;">
    {% filter force_escape %}
        {% debug %}
    {% endfilter %}
</textarea>
# How inserted debug tag?
# templatetags/debug.py
import pudb as dbg    # change to any *db
from django.template import Library, Node

register = Library()

class PdbNode(Node):
    def render(self, context):
        dbg.set_trace()    # Debugger will stop here
        return ''

@ register.tag
def pdb(parser, token):
    return PdbNode()

########
{% load debug %}

{% for item in items %}
    {# Some place you want to break #}
    {% pdb %}
{% endfor %}
