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

####### techniques to add Django flash messages
from django.contrib import messages

# Generic add_message method
messages.add_message(request, messages.DEBUG, 'The following SQL statements were executed:%s' % sqlqueries) # Debug messages ignored by default
messages.add_message(request, messages.INFO, 'All items on this page havefree shipping.')
messages.add_message(request, messages.SUCCESS, 'Email sent successfully.')
messages.add_message(request, messages.WARNING, 'You will need to change your password in one week.')
messages.add_message(request, messages.ERROR, 'We could not process your request at this time.')

# Shortcut level methods
messages.debug(request, 'The following SQL statements were executed: %s' % sqlqueries) # Debug messages ingored by default
messages.info(request, 'All items on this page have free shipping.')
messages.success(request, 'Email sent successfully.')
messages.warning(request, 'You will need to change your password in one week.')
messages.error(request, 'We could not process your request at this time.')

########## set default Django message level globally in settings.py
# Reduce threshold to DEBUG level in settings.py
from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG

# Increase threshold to WARNING level in settings.py
from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.WARNING

###### set default Django message level on a request basis
# Reduce threshold to DEBUG level per request
from django.contrib import messages
messages.set_level(request, messages.DEBUG)

# Increase threshold to WARNING level per request
from django.contrib import messages
messages.set_level(request, messages.WARNING)

######### use of the fail_silently=True attribute to ignore errors
from django.contrib import messages

# Generic add_message method, with fail_silently=True
messages.add_message(request, messages.INFO, 'All items on this page have free shipping.',fail_silently=True)

# Shortcut level method, with fail_silently=True
messages.info(request, 'All items on this page have free shipping.',fail_silently=True)

######## boilerplate code to use template for flash msg
{% if messages %}
<ul class="messages">
  {% for msg in messages %}
  <li>
    <div class="alert alert-{{msg.level_tag}}" rele="alert">
    {{msg.message}}
    </div>
  </li>
  {% endfor %}
</ul>
{% endif %}

######### use the get_messages() method to access falash messages
from django.contrib import messages

the_req_messages = messages.get_messages(request)
for msg in the_req_messages:
    do_something_with_the_flash_message(msg)

######### class-based view inherited from TemplateView with url definition
# views.py
from django.views.generic import TemplateView

class AboutIndex(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # **kwargs contains keyword context initialization value (if any)
        # Call base implementation to get a context
        context = super(AboutIndex, self).get_context_data(**kwargs)
        # Add context data to pass to template
        context['aboutdata'] = 'Custom data'
        return context

### urls.py
from coffeehouse.about.views import AboutIndex

urlpatterns = [
        url(r'^about/index/',AboutIndex.as_view(),{'onsale':True}),
]

######### class-based view inherited from View with multiple HTTP handling
# view.py
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render

class ContactPage(View):
    mytemplate = 'contact.html'
    unsupported = 'Unsupported opration'

    def get(self, request):
        return render(request, self.mytemplate)

    def post(self, request):
        return HttpResponse(self.unsupported)

# urls.py
from coffeehouse.contact.views import ContactPage

urlpatterns = [
        url(r'^contact/$', ContactPage.as_view()),
]

#########
