""" Views from django site clearly."""

# A simple view
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

#########
# Returning errors
from django.http import HttpResponse, HttpResponseNotFound

def my_view(request):
    # ...
    if foo:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</hq>')
###
# Creata a return class for any status code you like.
from django.http import HttpResponse

def my_view(request):
    # ...
    # Return a "created" (201) response code.
    return HttpResponse(status=201)
#######
# The Http 404 exception
from django.http import Http404
from django.shortcuts import render
from polls.models import Poll

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'polls/detail.html', {'poll': p})
##########
# Castomizing error views
handler404 = 'mysite.views.my_custom_page_not_found_view' # page_not_found()
handler500 = 'mysite.views.my_custom_error_view' # server_error()
handler403 = 'mysite.views.my_custom_permission_denied_view' # permission_denied()
handler400 = 'mysite.views.my_custom_bad_request_view' # bad_request()
#########
# Testing custom error views
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.urls import path

def response_error_handler(request, exception=None):
    return HttpResponse('Error handler content', status=403)

def permission_denied_view(request):
    raise PermissionDenied

urlpatterns = [
        path('403/', permission_denied_view),
]
handler403 = response_error_handler

# ROOT_URLCONF must specify the module that contains handler403 = ...
@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(SimpleTestCase):
    def test_handler_renders_template_response(self):
        response = self.client.get('/403/')
        # Make assertions on the response here. For example:
        self.assertContains(response, 'Error handler content', status_code=403)
###########
# Async views

import datetime
from django.http import HttpResponse

async def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.</body></html>' %now
    return HttpResponse(html)
##########
# decorators
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass
###########
# Basic file upload
# forms.py
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

###
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from somewhere import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = uploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
###
# might handle an uploaded file
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

##########
# Handling uploaded files with a model

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ModelFormWithField

def upload_file(request):
    if request.method == 'POST':
        form = ModelFormWithFiled(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})
###
# You can assign the file object from request.FILES to the file field in the
# model:
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .model import ModelWithFileField

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ModelWithFileField(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

##########
# Uploading multiple files
# forms.py
from django import forms

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

# Then override the post method of your FormView subclass to handle
# multiple file uploads:
# views.py
from django.views.generic.edit import FormView
from .forms import FileFieldForm

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse()

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

#######
# render(), Django does not provide a shortcut function which returns a
# TemplateResponse 
# The following example renders the template myapp/index.html
from django.shortcuts import render

def my_view(request):
    # View code here...
    return render(request, 'myapp/index.html', {
        'foo': 'bar',
        }, content_type = 'application/xhtml+xml')
# This example is equivalent to:
from django.http imprt HttpResponse
from django.template import loader

def my_view(request):
    # View code here...
    t = loader.get_template('myapp/index.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request),
            content_type='application/xhtml+xml')
##########
# Middleware asynchronous support
import asyncio
from django.utils.decorators import sync_and_async_middleware

@sync_and_async_middleware
def simple_middleware(get_response):
    # One-time configuration and initialization goes here.
    if asyncio.iscoroutinefunction(get_response):
        async def middleware(request):
            # Do something here!
            response = await get_response(request)
            return response
    else:
        def middleware(request):
            # Do something here!
            response = get_response(request)
            return response
    return middleware

#############
# This simplistic view sets a has_commented variable to True after a user
# posts a comment. It doesn't let a user post a comment more than once:
def post_comment(request, new_comment):
    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")
    c = comments.Comment(comment=new_comment)
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')

# This simplistic view logs in a "member" of the site:
def login(request):
    m = Member.objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['member_id'] = m.id
        return HttpResponse("You're logged in.")
    else:
        return HttpResponse("Your username and password didn't match.")

# And this one logs a member out, according to login() above:
def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
#######
# Settings test cookies
from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse("You're logged in.")
        else:
            return HttpResponse("Please enable cookies and try again.")
    request.session.set_test_cookie()
    return render(request, 'foo/login_form.html')
##########
# The example shows a custom database-backed session engine that include as
# additional database column to store an account ID(thus providing an option
# to query the database for all active sessions for an account)
from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.contrib.sessions.base_session import AbstractBaseSession
from django.db import models

class CustomSession(AbstrctBaseSession):
    account_id = models.IntegerField(null=True, db_index= True)

    @classmethod
    def get_session_store_class(cls):
        return SessionStore

class SessionStore(DBStore):
    @classmethod
    def get_model_class(cls):
        return CustomSession

    def create_model_instance(self, data):
        obj = super().create_model_instance(data)
        try:
            account_id = int(data.get('_auth_user_id'))
        except (ValueError, TypeError):
            account_id = None
        obj.account_id = account_id
        return obj

############
# Field data.
# views.py
from django.core.mail import send_mail

if form.is_valid():
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    sender = form.cleaned_data['sender']
    cc_myself = form.cleaned_data['cc_myself']

    recipients = ['info@example.com']
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    return HttpResponseRedirect('/thanks/')

###############
# Using a model formset in a view.
from django.forms import modelformset_factory
from django.shortcuts import render
from myapp.models import Author

def manage_authors(request):
    AuthorFormSet = modelformset_factory(Author, fields=('name', 'title'))
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = AuthorFormSet()
    return render(request, 'manage_authors.html', {'formset': formset})

#########
# Subclassing generic views
# some_app/views.py
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "about.html"

###
# urls.py
from django.urls import path
from some_app.views import AboutView

urlpatterns = [
        path('about/', AboutView.as_view()),
]
##########
# Supporting other Http methods
# urls.py
from django.urls import path
from books.views import BookListView

urlpatterns = [
        path('books/', BookListView.as_view()),
]
###
# views.py
from django.http import HttpResponse
from django.views.generic import ListView
from books.models import Book

class BookListView(ListView):
    model = Book

    def head(self, *args, ** kwargs):
        last_book = self.get_queryset().latest('publication_date')
        response = HttpResponse()
        # RFC 1123 date format
        response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H: %M:%S GMT')
        return response
########
# Using class-based views
# view function
from django.http import HttpResponse

def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('result')

### In a class-based view, this would become:
from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')
### urls.py
from django.urls import path
from myapp.views import MyView

urlpatterns = [
        path('about/', MyView.as_view()),
]
###########
from django.http import HttpResponse
from django.views import View

class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)

###
class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"

###
urlpatterns = [
        path('about/', GreetingView.as_view(greeting="G'day")),
]
############
# Handling forms with class-based views
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MyForm

def myview(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
        else:
            form = MyForm(initial={'key': 'value'})
        return render(request, 'form_template.html', {'form': form})
###
# A similar class-based view might look like:
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import MyForm

class MyFormView(View):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})
############
# Decorating in URLconf
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

from .view import VoteView

urlpatterns = [
        path('about/',
            login_required(TemplateView.as_view(template_name="secret.html"))),
        path('vote/', permission_required('polls.can_vote')(VoteView.as_view())),
]
###########
# Decorating the class
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

class ProtectedView(TemplateView):
    template_name = 'sectet.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
###
# or more succinctly
@method_decorator(login_required, name='dispatch')
class ProtectedView(TemplateView):
    template_name = 'secret.html'
###
# These two classes are equivalent
decorators = [never_cache, login_required]

@method_decorator(decorators, name='dispatch')
class ProtectedView(TemplateView):
    template_name = 'secret.html'

@method_decorator(never_cache, name='dispatch')
@method_decorator(login_required, name='dispatch')
class ProtectedView(TemplateView):
    tmplate_name = 'secret.html'
#########
# Making "friendly" template contexts.
# views.py
from django.views.generic import ListView
from books.models import Publisher

class PublisherList(ListView):
    model = Publisher
    context_object_name = "my_favorite_publishers"

##########
# Adding extra context
from django.views.generic import DetailView
from books.models import Book, Publisher

class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context

###########
# Viewing subsets of objects
# using th queryset argument
from django.views.generic import DetailView
from books.models import Publisher

class PublisherDetail(DetailView):
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()
###
from django.views.generic import ListView
from books.models import Book

class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'
###
from django.views.generic import ListView
from books.models import Book

class AcmeBookList(ListView):
    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='ACME Publishing')
    template_name = 'books/acme_list.html'

###############
# Dynamic filtering
# urls.py
from django.urls import path
from books.views import PublisherBookList

urlpatterns = [
        path('books/<publisher>/', PublisherBookList.as_view()),
]
###
# views.py
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from books.models import Book, Publisher

class PublisherBookList(ListView):
    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher,
                name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)
###
def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)
    # Add in the publisher
    context['publisher'] = self.publisher
    return context
############
# Content negatiation example
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from myapp.models import Author

class JsonableResponseMixin:
    """
    Mixin to add JSON support to a form.
    Must be used with an object_based FormView (e.g. CreateView)
    """
    def from_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.accepts('text/html'):
            return response
        else:
            return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.accepts('text/html'):
            return response
        else:
            data = {
                    'pk': self.object.pk,
            }
            return JsonResponse(data)

class AuthorCreate(JsonableResponseMixin, CreateView):
    model = Author
    fields = ['name']
###
# Using SingleObjectMixin with View
# views.py
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from books.models import Author

class RecordInterest(SingleObjectMixin, View):
    """Records the current user's interest in an author."""
    model = Author

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        # Look up the author we're interested in.
        self.object = self.get_object()
        # Actually record interest somehow here!

        return HttpResponseRedirect(reverse('author-detail', kwargs={'pk': self.object.pk}))

###
# urls.py
from django.urls import path
from books.views import RecordInterest

urlpatterns = [
        # ...
        path('author/<int:pk>/interest/', RecordInterest.as_view(), name='author-interest'),
]
############
# Using SingleObjectMixin with ListView
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from books.models import Publisher

class PublisherDetail(SingleObjectMixin, ListView):
    paginate_by = 2
    template_name = "books/publisher_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Publisher.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publisher'] = self.object
        return context

    def get_queryset(self):
        return self.objecty.book_set.all()

###
{% extends "base.html" %}

{% block content %}
  <h2>Publisher {{ publisher.name }}</h2>
  <ol>
    {% for book in page_obj %}
      <li>{{ book.title }}</li>
    {% endfor %}
  </ol>
  
  <div class="pagination">
    <span class="step-links">
      {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">previous</a>
      {% endif %}

      <span class="current">
        Page {{ page_obj.number }} of {{ paginator.num_pages }}.
      </span>

      {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">next</a>
      {% endif %}
    </span>
  </div>
{% endblock %}
########
# Using FormMixin with DetailView
# CAUTION: you almost certainly do not want to do this.
# It is provided as part of a discussion of problems you can
# run into when combining different generic class-based view
# functionality that is not designed to be used together.

from django import forms
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from books.models import Author

class AuthorInterestForm(forms.Form):
    message = forms.CharField()

class AuthorDetail(FormMixin, DetailView):
    model = Author
    form_class = AuthorInterestForm

    def get_success_url(self):
        return reverse('author_detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super().form_valid(form)
###########
# An alternative using DetailView
from django import forms
from django.views.generic import DetailView
from books.models import Author

class AuthorInterestForm(form.Form):
    message = forms.CharField()

class AuthorDisplay(DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthorInterestForm()
        return context
###
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin

class AuthorInterest(SingleObjectMixin, FormView):
    template_name = 'books/author_detail.html'
    form_class = AuthorInterestForm
    model = Author

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('author-detail', kwargs={'pk': self.object.pk})

###
from django.views import View

class AuthorDetail(View):

    def get(self, request, *args, **kwargs):
        view = AuthorDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = AuthorInterest.as_view()
        return view(request, *args, **kwargs)
##############
# JSON mixin example
from django.http import JsonResponse

class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
                self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Return an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context
###
from django.views.generic import TemplateView

class JSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)
###
from django.views.generic.detail import BaseDetailView

class JSONDetailView(JSONResponseMixin, BaseDetailView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)
###
from django.views.generic.detail import SingleObjectTemplateResponseMixin

class HybridDetailView(JSONResponseMixin, SingleObjectTemplateResponseMixin,
        BaseDetailView):
    def render_to_response(self, context):
        # Look for a 'format=json' GET argument
        if self.request.GET.get('format') == 'json':
            return self.render_to_json_response(context)
        else:
            return super().render_to_response(context)
##########
# conditional view processing
# the condition decorator
condition(etag_func=None, last_modified_func=None)

###
import datetime
from django.db import models

class Blog(models.Model):
    ...

class Entry(model.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    published = models.DateTimeField(default=datetime.datetime.now)
    ...
###
def latest_entry(request, blog_id):
    return Entry.objects.filter(blog=blog_id).latest("published").published

###
from django.views.decorators.http import condition

@condition(last_modified_func=latest_entry)
def front_page(request, blog_id):
    ...
#############
# shortcuts for only computing one value
etag(etag_func)
last_modified(last_modified_func)

### 
@last_modified(latest_entry)
def front_page(request, blog_id):
    ...
### or
def front_page(request, blog_id):
    ...
front_page = last_modified(latest_entry)(front_page)
############
# both conditions
# bad code. Don't do this!
@etag(etag_func)
@last_modified(last_modified_func)
def my_view(request):
    ...
##############
# sending email
from django.core.mail import send_mail

send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
)

### preventing header injection
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

###########
# Send a text and HTML combination
from django.core.mail import EmailMultiAlternatives

subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
text_content = 'This is an important message.'
html_content = '<p>This is an <strong>important</strong> message.</p>'
msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
msg.attach_alternative(html_content, "text/html")
msg.send()

###
msg = EmailMessage(subject, html_content, from_email, [to])
msg.content_subtype = "html" # Main content is now text/html
msg.send()

#############
# email backends
from django.core import mail

with mail.get_connection()as connection:
    mail.EmailMessage(
            subject1, body1, from1, [to1],
            connection=connection,
    ).send()
    mail.EmailMessage(
            subject2, body2, from2, [to2],
            connection=connection,
    ).send()

##############
# sending multiple emails
from django.core import mail

connection = mail.get_connection()  # Use default email connection
messages = get_notification_email()
connection.send_messages(messages)

###
from django.core import mail

connection = mail.get_connection()

# Manually open the connection
connection.open()

# Construct an email message that uses the connection
email1 = mail.EmailMessage(
        'Hello',
        'Body goes here',
        'from@example.com',
        ['to1@example.com'],
        connection=connection,
)
email1.send()  # Send th email

# Construct two more messages
email2 = mail.EmailMessage(
        'Hello',
        'Body goes here',
        'from@example.com',
        ['to2@example.com'],
)
email3 = mail.EmailMessage(
        'Hello',
        'Body goes here',
        'from@example.com',
        ['to3@example.com'],
)

# Send the two emails in a single call -
connection.send_messages([email2, email3])
# The connection was already open so send_messages() doesn't close it.
# We need to manually close the connection.
connection.close()

#############
# internationalization in python code
from django.http import HttpResponse
from django.utils.translation import gettext as _

def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)

###
from django.http import HttpResponse
from django.utils.translation import gettext

def my_view(request):
    output = gettext("Welcome to my site.")
    return HttpResponse(output)

###
def my_view(request):
    words = ['Welcome', 'to', 'my', 'site.']
    output = _(' '.join(words))
    return HttpResponse(output)

###
def my_view(request):
    sentence = 'Welcome to my site.'
    output = _(sentence)
    return HttpResponse(output)

###
def my_view(request, m, d):
    output = _('Today is %(month)s %(day)s.') % {'month': m, 'day': d}
    return HttpResponse(output)

##############
# Pluralization
from django.http import HttpResponse
from django.utils.translation import ngettext

def hello_world(request, count):
    page = ngettext(
            'there is %(count)d object',
            'there are %(count)d object',
            count,
    ) % {
            'count': count,
    }
    return HttpResponse(page)

###
from django.utils.translation import ngettext
from myapp.models import Report

count = Report.objects.count()
if count == 1:
    name = Report._meta.verbose_name
else:
    name = Report._meta.verbose_name_plural

text = ngettext(
        'There is %(count)d %(name)s available.',
        'There are %(count)d %(name)s available.',
        count,
) % {
        'count': count,
        'name': name
}

###
text = ngettext(
        'There is %(count)d %(name)s object available.',
        'There are %(count)d %(name)s object available.',
        count,
) % {
        'count': count,
        'name': Report._meta.verbose_name,
}
##############
# contextual markers
from django.utils.translation import pgettext

month = pgttext("month name", "May")

###
from django.db import models
from django.utils.translation import pgettext_lazy

class MyThing(models.Model):
    name = models.CharField(help_text=pgttext_lazy(
        'help text for MyThing model', 'This is the help text'))

#######
# lazy translation
from django.db import models
from django.utils.translation import gettext_lazy as _

class MyThing(models.Model):
    name = models.CharField(help_text=_('This is the help text'))

###
class MyThing(models.Model):
    kind = models.ForeignKey(
            ThingKind,
            on_delete=models.CASCADE,
            related_name='kinds',
            verbose_name=_('kind'),
    )

############

