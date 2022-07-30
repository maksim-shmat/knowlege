"""Make templates for Django with Mako, how love Python."""

#1
from mako.template import Template

t = Template("My favorite ice cream is ${name}")
t.render(name="Herrell's")
# "My favorite ice cream is Herrell's"

context = {'name': "herrell's"}
t.render(**context)
# "My favorite ice cream is herrel's"

#2 with filters

from mako.template import Template

t = Template("My favorite ice cream is ${name | entity}")
t.render(name="Emack & Bolio's")
# My favorite ice cream is Emack & Bolio's

#3 for django

from mako.template import Template

def mako_view(request):
    t = Template("Your IP address is ${REMOTE_ADDR}")
    output = t.render(**request.META)
    return HttpResponse(output)

# need make method render_to_response. What?
# see to djangosnippets.org
