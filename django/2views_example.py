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

###### custom views to override built-in HTTP view method
from django.shortcuts import render

def page_not_found(request):
    # Dict to pass to template, data could come from DB query
    values_for_template = {}
    return render(request, '404.html', values_for_template, status=404)

def server_error(request):
    # Dict to pass to template, data could come from DB query
    values_for_template = {}
    return render(request, '500.html', values_for_template, status=500)

def bad_request(request):
    # Dict to pass to template, data could come from DB query
    values_fot_template = {}
    return render(request, '400.html', values_for_template, status=400)

def perission_denied(request):
    # Dict to pass to template, data could come from DB query
    values_for_template = {}
    return render(request, '403.html', values_for_template, status=403)

###### HttpResponse with template and custom CSV file download
from django.http import HttpRespnse
from django.utils import timezone
from django.template import loader, Context

response = HttpResponse(content_type='text/csv')
response['Content-Disposition'] = 'attachment; filename=Users_%s.csv' %(timezone.now().today())
t = loader.get_template('dashboard/users_csvexport.html')
c = Context({'users': sorted_user,})
response.write(t.render(c))
return response

###### django middleware class structure
class CoffeehouseMiddleware(object):
    
    def __init__(self, get_response):
        self.get_response = get_response
        # One_time configuration and initializtion on start_up

    def __call__(self, request):
        # Logic executed on a request before the view (and other middleware) is called.
        # get_response call triggers next phase
        response = self.get_response(request)

        # Logic executed on response after the view is called.
        # Return response to finish middleware sequence
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Logic executed before a call to view
        # Gives access to the view itself & arguments

    def process_exception(self, request, exception):
        # Logic executed if an exception/error occurs in the view

    def process_template_response(self, request, response):
        # Logic executed after the view is called,
        # ONLY IF vew response is TemplateResponse

#######
