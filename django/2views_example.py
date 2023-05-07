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

######### custom Django context processor method
def onsale(request):
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    # web services of social APIs
    sale_items = {'Monday': 'Mocha 2x1', 'Tuesday': 'Latte 2x1'}
    return {'SALE_ITEMS': sale_items}

### template context processor definition in context_processors in OPTIONS of TEMPLATES
'OPTIONS': {
        'context_processors': [
            'coffeehouse.stores.processors.onsale',
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
}

######## django custom filter with no arguments
from django import template
register = template.Library()

@register.filter()
def boldcoffee(value):
    '''Returns input wrapped in HTML tags'''
    return '<b>%s</b>' % value

### django custom filter with arguments
@register.filter()
def coffee(value,arg="muted"):
    '''Returns input wrapped in HTML tags with a CSS class'''
    '''Defaults to CSS class 'muted' from Bootstrap'''
    return '<span class="%s">%s</span>' % (arg,value)

######### django custom filter that detects autoescape setting
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(needs_autoescape=True)
def smartcoffee(value, autoescape=True):
    '''Returns input wrapped in HTML tags'''
    '''and also detects surrounding autoescape on filter (if any) and escapes '''
    if autoescape:
        value = escape(value)
    result = '<b>%s</b>' % value
    return mark_safe(result)

######## django management command class with no agruments
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    help = 'Send test emails'

    def handle(self, *args, **options):
        for admin_name, email in settings.ADMINS:
            try:
                self.stdout.write(self.style.WARNING("About to send emailto %s" % (email)))
                # Logic to send email here
                # Any other Python logic can also go here
                self.stdout.write(self.style.SUCCESS('Successfully sent email to "%s"' % email))
                raise Exception
            except Exception:
                raise CommandError('Failed to send test email')

########## django management task class with arguments
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    help = 'Clean up stores'

    def add_arguments(self, parser):
        # Positional argument are standalone name
        parser.add_argument('store_id')

        # Named (optional) arguments start with --
        parser.add_argument(
                '--delete',
                default=False,
                help='Delete store instead of cleaning it up',
        )

    def handle(self, *args, **options):
        # Access arguments inside **options dictionary
        # options={'store_id': '1', 'settings': None, 'pythonpath': None,
        #          'verbosity': 1, 'traceback': False, 'no_color': False,
        #          'delete': False}

########## django management automation with call_command()
from django.core import management

# Option 1, no arguments
management.call_command('sendtestemails')

# Option 2, no pause to wait for input
management.call_command('collectstatic', interactive=False)

# Option 3, command input with Command()
from django.core.management.commands import loaddata
management.call_command(loaddata.Command(), 'stores', verbosity=0)

# Option 4, positional and named command arguments
management.call_command('cleanupdatastores', 1, delete=True)

########## django form class with backing processing view method
from django import forms
from django.shortcuts import render

class ContactForm(forms.Form):
    name = form.CharField(required=False)
    email = forms.EmailField(label='Your email')
    comment = forms.CharField(widget=forms.Textarea)

def contact(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # Reference is now a bound instance with user data sent in POST
        # process data, insert into DB, generate email, redirect to a newURL, etc
    else:
        # GET, generate blank form
        form = ContactForm()
        # Reference is now an unbound (empty) form
    # Reference form instance (bound/unbound) is sent to template for rendering
    return render(request,'about/contact.html',{'form':form})

######### django form instance with initial argument declared in view method
def contact(request):
    ...
    ...
    else:
        # GET, generate blank form
        form = ContactForm(initial={'email':'johndoe@coffeehouse.com','name':'John Doe'})
        # Form is now initialized for first presentation to display thesevalues
# Reference form instance (bound/unbound) is sent to template for rendering
    return render(request, 'about/contact.html',{'form':form})

########## django form fields with initial argument
from django import forms

class ContactForm(forms.Form):
    name = form.CharField(required=False,initial='Please provide your name')
    email = forms.EmailField(label='Your email',initial='We need your email')
    comment = forms.CharField(widget=forms.Textarea)

def contact(request):
    ...
    ...
    else:
        # GET, generate blank form
        form = ContactForm()
        # Form is now initialized for first presentation and is filled with initial values in form definition
    # Reference form instance (bound/unbound) is sent to template for rendering
    return render(request, 'about/contact.html', {'form': form})

######### django form initialized with __init__ method
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = froms.EmailField(label='Your email')
    comment = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        # Get 'initial' argument if any
        initial_arguments = kwargs.get('initial', None)
        updated_initial = {}
        if initial_arguments:
            # We have initial arguments, fetch 'user' placeholder variable if any
            user = initial_arguments.get('user',None)
            # Now update the form's initial value if user
            if user:
                updated_initial['name'] = getattr(user, 'first_name', None)
                updated_initial['email'] = getattr(user, 'email', None)
        # You can also initialize form field with hardcoded values
        # of perform complex DB logic here to then perform initialization
        updated_initial['comment'] = 'Please provide a comment'
        # Finally update the kwargs initial reference
        kwargs.update(initial=updated_initial)
        super(ContactForm, self).__init__(*args, **kwargs)

def contact(request):
    ...
    ...
    else:
        # GET, generate blank form
        form = ContactForm(initial={'user':request.user,'otherstuff':'othrstuff'})
        # Form is now initialized via the form's __init__ method
    # Reference form instance (bound/unbound) is sent to template for rendering
    return render(request, 'about/contact.html', {'form':form})

#1 views.py

from django.views.generic.edit import FormView
from .forms import ContactForm


class FormClassView(FormView):
    template_name = 'chapter_5/form-class.html'
    form_class = ContactForm
    success_url = '/chapter-5/contact-form-success/'

# Dummy code for urls.py
from django.urls import reverse
from django.views.generic.edit import FormView


class FormClassView(FormView):
    ...
    def get_success_url(self, **kwargs):
        return reverse('pattern_name', args=(value,))

# urls.py

from django.urls import re_path
from django.views.generic import (
                                  TemplateView
                                )
from .views import FormClassView


urlpatterns = [
        re_path(
            r'^chapter-5/form-class/?$',
            FormClassView.as_view()
        ),

        re_path(
                r'^chapter-5/contact-form-class/?$',
                TemplateView.as_view(
                    template_name = 'chapter_5/contact-success.html')
                ),
                kwargs = {
                    'title': 'FormatClassView Success Page',
                    'page_id': 'form-class-success',
                    'page_class': 'form-class-success-page',
                    'h1_tag': 'This is the FormClassView Success
                    Page Using ContactForm',
                    },
                ]

#2 HTTP request methods - get()
...
from django.views.generic.edit import FormView
from django.template.response import (
                                      TemplateResponse
                                      )

class FormClassView(FormView):
    ...
    def get(self, request, *args, **kwargs):
        initial = {
                'full_name': 'FirstName LastName',
                'email_1': 'example1@example.com',
                # Add A Value For Every Field...
                }
        return TemplateResponse(
                request,
                self.template_name,
                {
                    'title': 'FormClassView Page',
                    'page_id': 'form-class-id',
                    'page_class': 'form-class-page',
                    'h1_tag': 'This is the FormClassView Page
                    Using ContactForm',
                    'form': self.form_class,
                }
        )

#3 post()
...
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.template.response import (
                                      TemplateResponse
                                      )

class FormClassView(FormView):
    ...
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(
                    self.success_url
            )
        else:
            return TemplateResponse(
                    request,
                    self.template_name,
                    {
                        'title': 'FormClassView Page - Please Correct
                        The Errors Below',
                        'page_id': 'form-class-id',
                        'page_class': 'form-class-page errors-found',
                        'h1_tag': 'This is the FormClassView Page
                        Using ContactForm<br /><small class="error-msg">Errors Found</small>',
                        'form': form,
                    }
                    )
#4 From Django 4.0? New form?
# Linking a model to a form
# forms.py

...
from django.forms import Form, ModelForm
from ..chapter_3.models import Vehicle


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = [
                'vin',
                'sold',
                'price',
                'make',
                'vehicle_model',
                'endine',
        ]

# View class - CreateView

# view.py
...
from django.http import HttpResponseRedirect
from django.views.generic.edit import (...,
                                       CreateView
                                    )
from django.template.response import (
                                      TemplateResponse
                                    )
from .forms import ContactForm, VehicleForm


class ModelFormClassCreateView(CreateView):
    template_name = 'chapter_5/model-form-class.html'
    form_class = VehicleForm
    success_ulr = '/chapter-5/vehicle-form-success/'

    def get(self, request, *args, **kwargs):
        return TemplateResponse(
                request,
                self.template_name,
                {
                    'title': 'ModelFormClassCreateView Page',
                    'page_id': 'model-form-class-id',
                    'page_class': 'model-form-class-page',
                    'h1_tag': 'This is the
                    ModelFormClassCreateView Class Page Using VehicleForm',
                    'form': self.form_class(),
                }
            )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            vehicle = form.instance
            vehicle.save()
            return HttpResponseRedirect(
                    self.success_url
            )
        else:
            return TemplateResponse(
                    request,
                    self.template_name,
                    {
                        'title': 'ModelFormClassCreateView 
                        Page - Please Correct The Errors Below',
                        'page_id': 'model-form-class-id',
                        'page_class': 'model-form-class-page-error-found',
                        'h1_tag': 'This is the
                        ModelFormClassCreateView Page Using VehicleForm<br/
                        ><small class="error-msg">Errors Found</small>',
                        'form': form,
                    }
            )

# urls.py

from django.urls import re_path
from django.views.generic import (
                                  TemplateView
                                )
from .views import (
                    FormClassView,
                    ModelFormClassCreateView
                )

urlpatterns = [
        ...,
        re_path(
            r'^chapter-5/model-form-class/?$',
            ModelFormClassCreateView.as_view(),
        ),
        re_path(
            r'^chapter-5/vehicle-form-success/?$',
            TemplateView.as_view(
                template_name = 'chapter_5/vehicle-success.html'
            ),
            kwargs = {
                'title': 'ModelFormClass Success Page',
                'page_id': 'model-form-class-success',
                'page_class': 'model-form-class-success-page',
                'h1_tag': 'This is the ModelFormClass Success Page Using
                VehicleForm',
            }
        ),
    ]

#5 View class - UpdateView

# urls.py

from django.urls import re_path
from .views import (
                    ...,
                    ModelFormClassUpdateView
                )
...
urlpatterns = [
        ...,
        re_path(
            'chapter-5/model-form-class/(?P<id>[0-9])/?$',
            ModelFormClassUpdateView.as_view(),
            name = 'vehicle_detail'
        ),
    ]

# views.py
...
from django.http import HttpResponseRedirect
from django.template.response import (
                                      TemplateResponse
                                    )
from django.view.generic.edit import (
                                      ...,
                                      UpdateView
                                    )
from .forms import VehicleForm
from ..chapter_3.models import Vehicle


class ModelFormClassUpdateView(UpdateView):
    template_name = 'chapter_5/model-form-class.html'
    form_class = VehicleForm
    success_url = '/chapter-5/vehicle-form-success/'

    def get(self, request, id, *args, **kwargs):
        try:
            vehicle = Vehicle.object.get(pk=id)
        except Vehicle.DoesNotExist:
            form = self.form_class()
        else:
            form = self.form_class(instance=vehicle)

        return TemplateResponse(
                request,
                self.template_name,
                {
                    'title': 'ModelFormClassUpdateView Page',
                    'page_id': 'model-form-class-id',
                    'page_class': 'model-form-class-page',
                    'h1_tag': 'This is the
                    ModelFormClassUpdateView Class Page Using VehicleForm',
                    'form': form,
                }
            )

    def post(self, request, id, *args, **kwargs):
        # Use the same code as we did for the ModelFormClassCreateView class

#6 Formset function - formset_factory

# forms.py

from django import forms
from django.forms import Form, ModelForm
from django.forms import (
                          ...,
                          formset_factory
                        )
...


class ProspectiveBuyerForm(Form):
    first_name = forms.CharField(
            label = 'First Name',
            help_text = 'Enter your first name only',
            required = True,
            error_messages = {
                'required': 'Please provide us with a first name',
            }
    )
    last_name = forms.CharField(
            label = 'Last Name',
            help_text = 'Enter your last name only',
            required = True,
            error_messages = {
                'required': 'Please provide us with a last name',
            }
    )

ProspectiveBuyersFormSet = formset_factory(  # or modelformset_factory()
        ProspectiveBuyerForm,
        extra = 1
)

# views.py

...
from django.http import HttpResponseRedirect
from django.template.respnse import (
                                     TemplateResponse
                                    )
from django.views.generic.edit import (
                                       ...,
                                       CreateView
                                      )
from .forms import ..., ProspectiveBuyerFormSet
from ..chapter3.models import Vihicle


class ModelFormClassCreateView(CreateView):
    ...
    def get(self, request, *args, **kwargs):
        buyer_formset = ProspectiveBuyerFormSet()
        return TemplateResponse(
                request,
                self.template_name,
                {
                    ...
                    'form': self.form_class(),
                    'buyer_formset': buyer_formset,
                }
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        buyer_formset = ProspectiveBuyerFormSet(
                request.POST
        )
        if form.is_valid():
            ...
        else:
            return TemplateResponse(
                    request,
                    self.template_name,
                    {
                        ...
                        'form': form,
                        'buyer_formset': buyer_formset,
                    }
            )

# model-form-class.html
...
{% extends 'chapt_5/base/base_template_1.html' %}
{% load static %}
...
{% block body_content %}
  ...
  <form method="post" id="form">
    {% csrf_token %}
    {{ form }}
    {% if buyer_formset %}
      <h3>Prospective Buyers</h3>
      {{ buyer_formset.non_form_errors }}
      {{ buyer_formset.management_form }}

      {% for form in buyer_formset %}
        <div class="formset-container {{ buyer_formset.prefix }}">
          <div class="first-name">
            {{ form.first_name.label }}: {{ form.first_name }}
          </div>
          <div class="last-name">
            {{ form.last_name.label }}: {{ form.last_name }}
          </div>
        </div>
      {% endfor %}
    {% endif %}

    <button id="add-formset" type="button">Add Another Prospective Buyer</button>
    <input type="submit" value="Save Vehicle">
  </form>
{% endblock %}

#7 Dynamic inline formsets

#/templates/chapter_5/base/base_template_1.html
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
    <head>
      ...
      <script defer type="text/javascript" src="{{
      base_url }}{% static 'chapter_5/js/site-js.js' %}"></
      script>
    </head>
      ...
</html>

# /static/chapter_5/js/site-js.js
let formsetContainer = document.querySelectorAll(
        '.formset-container'
),
form = document.querySelector('#form'),
addFormsetButton = document.querySelector(
        '#add-formset'
),
totalForms = document.querySelector(
        '#id_form-TOTAL_FORMS'
),
formsetNum = formsetContainer.length - 1;

addFormsetButton.addEventListener(
        'click',
        $addFormset
);

furnction $addFormset(e) {
        e.preventDefault();

        let newForm = fromsetContainer[0].cloneNode(true),
            formRegex = RegExp(`form-(\\d){1}-`,'g');

        formsetNum++
        newForm.innerHTML = newForm.innerHTML.replace(
            formRegex,
            'form-${formsetNum}-'
        );
        form.insertBefore(newForm, addFormsetButton);

        totalForms.setAttribute(
            'value',
            '${formsetNum + 1}'
        );
}

#8
