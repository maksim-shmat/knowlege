""" From beginning django web app development."""

# django view method response alternatives
# Option 1)
from django.shortcuts import render

def detail(request,store_id='1',location=None):
    ...
    return render(request, 'stores/detail.html', values_for_template)

# Option 2)
from django.template.response import TemplateResponse

def detail(request, store_id='1', location=None):
    ...
    return TemplateResponse(request, 'stores/detail.html', values_for_template)

# Option 3)
from django.http import HttpResponse
from django.template import loader, Context

def detail(request, store_id='1', location=None):
    ...
    response = HttpResponse()
    t = loader.get_template('stores/detail.html')
    c = Context(values_for_template)
    return response.write(t.render(c))

###### HTTP content-type and HTTP status for view method responses
from django.shortcuts import render
# No method body(s) and only render() example provided for simplicity
# Returns content type text/plain, with default HTTP 200
return render(request, 'stores/menu.csv', values_for_template, content_type='text/plain')

# Return HTTP 404, with detault text/html
# NOTE: Django has a built-in shortcut & template 404 response, described in the next section
return render(request, 'custom/notfound.html', status=404)

# Return HTTP 500, with default text/html
# NOTE: Django has a built-in shortcut & template 500 response, described in the next section
return render(request, 'custom/internalerror.html',status=500)

# Return content type application/json, with default HTTP 200
# NOTE: Django has a built-in shortcut JSON response, described in the next section
return render(request, 'stores/menu.json', values_for_template, content_type='application/json')

######
