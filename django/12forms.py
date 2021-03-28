"""Second file about forms."""

###### Now forms step by step

### templates/base.html
{% load staticfiles %}
<html>
  <head>
    <title>Django blog</title>
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400"
    rel="stylesheet">
    <link href="{% static 'css/base.css' %}" rel="stylesheet">
  </head>
  <body>
    <div>
      <header>
        <div class="nav-left">
          <h1><a href="{% url 'home' %}">Django blog</a></h1>
        </div>
        <div class='nav-right'>
          <a href="{% url 'post_new' %}">+ New Blog Post</a>
        </div>
      </header>
      {% block content %}
      {% endblock content %}
    </div>
  </body>
</html>

### Alternative sintax base.html
{% load staticfiles %}
<html>
  <head>
    <title>Django blog</title>
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400" rel/="stylesheet">
    <link rel="stylesheet" href="{% static 'css/base.css' %}">
  </head>
  <body>
    <div class="container">
      <header>
        <div class="nav-left">
          <h1><a href="/">Django blog</a></h1>
        </div>
        <div class="nav-right">
          <a href="{% url 'post_new' %}">+ New Blog Post</a>
        </div>
      </header>
      {% block content %}
      {% endblock content %}
    </div>
  </body>
</html>

### Create view
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
#   fields = '__all__'   # alternative

### further $ touch templates/post_new.html
{% extends 'base.html' %}

{% block content %}
  <h1>New post</h1>
  <form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save" />
  </form>
{% endblock content %}

### add an import on the second line for reverse get_absolute_url() and __str__()
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
            'auth.User',
            on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

### $ touch templates/post_detail.html
{% extends 'base.html' %}

{% block content %}
  <div class="post-entry">
    <h2>{{ post.title }}</h2>
    <p>{{ post.body }}</p>
  </div>

  <a href="{% url 'post_edit' post.pk %}">+ Edit Blog Post</a>
{% endblock content %}

### Alternative
{% extends 'base.html' %}

{% block content %}
  <h1>Edit post</h1>
  <form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
  <input type="submit" value="Update" />
</form>
{% endblock %}

### blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']  # or '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

### blog/urls.py
from django.urls import path
from .views import(    # or from . import views
        BlogListView,
        BlogDetailView,
        BlogCreateView,
        BlogUpdateView,
)

urlpatterns = [
        path('post/<int:pk>/edit/',
            BlogUpdateView.as_view(), name='post_edit'),
        path('post/new/', BlogCreateView.as_view(), name='post_now'),
        path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
        path('', BlogListView.as_view(), name='home'),
]

### templates/post_detail.html
{% extends 'base.html' %}

{% block content %}

    <div class="post-entry">
      <h2>{{ post.title }}</h2>  # or object.title
      <p>{{ post.body }}</p>     # or object.body
    </div>

    <p><a href="{% url 'post_edit' post.pk %}">+ Edit Blog Post</a></p>
    <p><a href="{% url 'post_delete' post.pk %}">+ Delete Blog Post</a></p>
{% endblock content %}

### $ touch templates/post_delete.html
# templates/post_delete.html
{% extends 'base.html' %}

{% block content %}
  <h1>Delete post</h1>
  <form action="" method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ post.title }}"?</p>
    <input type="submit" value="Confirm" />
  </form>
{% endblock %}

###### blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy

from .models import  Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']   # or '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

### blog/urls.py
from django.urls import path

from .views import (    # or from . import views
        BlogListView,
        BlogUpdateView,
        BlogDeleteView,
        BlogCreateView,
        BlogDeleteView, # new
)

urlpatterns = [
        path('post/<int:pk>/delete/', # new
            BlogDeleteView.as_view(), name='post_new'),
        path('post/new/', BlogCreateView.as_view(), name='post_new'),
        path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
        path('post/<int:pk>/edit/',
            BlogUpdateView.as_view(), name='post_edit'),
        path('', BlogListView.as_view(), name='home'),
]

###### Declaring and Identifying Fields

from django import forms

class ContactForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        if not user.is_authenticated():
            # Add a name field since the user doesn't have a name
            self.fields['name'] = forms.CharField(label='Full name')

###### Binding to User Input

from my_app.forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
    else:
        form = MyForm()
    ...

### for FILES
from my_app.forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
    else:
        form = MyForm()
    ...

###### Validating Input

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            # Do mare work here, since the data is known to be good
        else:
            form = MyForm()
        ...

###### Using Class-Based Views

from django.shortcuts import render, redirect

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/success/')
        return render(request, 'form.html', {'form': form})

### better
from django.shortcuts import render, redirect
from django.views.generic.base import View

class MyView(View):
    def get(self, request):
        form = MyForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/success/')
        return render(request, 'form.html', {'form': form})

### better more
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

class MyView(FormView):
    form_class = MyForm
    template_name = 'form.html'
    success_url = '/success/'

    def form_valid(self, form):
        form.save()
        return super(MyView, self).form_valid(form)

### 
from django.views.generic import edit
from my_app.models import MyModel

class CreateObject(edit.CreateView):
    model = MyModel

    class EditObject(edit.UpdateView):
        model = MyModel

    class DeleteObject(edit.DeleteView):
        model = MyModel
        success_url = '/'

###### forms validation

from django.forms import fields, uril

class LatitudeField(fields.DecimalField):
    default_error_messages = {
            'out_of_range': u'Value must be within -90 and 90.',
    }

    def clean(self, value):
        value = super(LatitudeField, self).clean(value)
        if not -90 <= value <= 90:
            raise util.ValidationError(self.error_messages['out_of_range'])
        return value


class LongitudeField(fields.DecimalField):
    default_error_messages = {
            'out_of_range': u'Value must be within -180 and 180.',
    }

    def clean(self, value):
        value = super(LatitudeField, self).clean(value)
        if not -180 <= value <= 180:
            raise util.ValidationError(self.error_messages['out_of_range'])
        return value

###### Rendering HTML

from django import forms

class PriceInput(forms.TextInput):
    def render(self, name, value, attrs=None):
        return '$ %s' % super(PriceInput, self).render(name, value, attrs)

class PercentInput(forms.TextInput):
    def render(self, name, value, attrs=None):
        return '%s %%' % super(PercentInput, self).render(name, value, attrs)

class ProductEntry(forms.Form):
    sku = forms.IntegerField(label='SKU')
    description = forms.CharField(widget=forms.Textarea())
    price = form.DecimalField(decimal_places=2, widget=PriceInput())
    tax = forms.IntegerField(widget=PercentInput())

print ProductEntry()

"""
<tr><th><label for="id sku">SKU:</label></th><td<>input type="text" name="sku" id="id_sku" /></td></tr>
<tr><th><label for="id_description">Description:</label></th><td><textarea id="id_description" rows="10" cols="40" name="description"></textarea></td></tr>
<tr><th><label for="id_price">Price:</label></th><td>$ <input type="text" name="price" id="id_price" /></td></tr>
<tr><th><label for="id_tax">Tax:</label></th><td><input type="text" name="tax" id="id_tax" /> %</td></tr>
"""
###### Spliting Data Across Multiple Widgets

from django.forms import fields

class LatLonField(fields.MultiValueField):

    def __init__(self, *args, **kwargs):
        filds = (LatitudeField(), LongitudeField())
        super(LatLonField, self).__init__(flds, *args, *kwargs)

    def compress(self, data_list):
        if data_list:
            if data_list[0] in fields.EMPTY_VALUES:
                raise fields.ValidationError(u'Enter a valid latitude.')
            if data_list[1] in fields.EMPTY_VALUES:
                raise fields.ValidationError(u'Enter a valid longitude.')
            return tuple(data_list)
        return None

###
from django.form import fields, widgets

class LatLonWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        wdgts = (widgets.TextInput(attrs), widgets.TextInput(attrs))
        super(LatLonWidget, self).__init__(wdgts, attrs)

    def decompress(self, value):
        return value or (None, None)

class LatLonField(fields.MultiValueField):
    widget = LatLonWidget

    # The rest of the code previously described

###### Pending and Resuming Forms

from django import forms
from django_localflavor_us import forms as us_forms

from pend_form.forms import PendForm

class Offer(PendForm):
    name = forms.CharField(max_length=255)
    phone = us_forms.USPhoneNumberField()
    price = forms.IntegerField()

###### Storing Values for Later

class PendedForm(models.Model):
    form_class = models.CharField(max_length=255)
    hash = models.CharField(max_length=32)


class PendedValue(models.Model):
    form = models.ForeignKey(PendedForm, related_name='data')
    name = mdoels.CharField(max_length=255)
    value = models.TextField()

###
try:
    from hashlib import md5
except:
    from md5 import new as md5

from django import forms

from pend_form.models import PendedForm

class PendForm(forms.Form):
    @classmethod
    def get_import_path(cls):
        return '%s.%s' % (cls.__module__, cls.__name__)

    def hash_data(self):
        content = ','.join('%s:%s' % (n, self.data[n]) for n in self.fields.keys())
        return md5(content).hexdigest()

    def pend(self):
        import_path = self.get_import_path()
        form_hash = self.hash_data()
        pended_form = PendedForm.objects.get_or_create(form_class=import_path,
                                                       hash=form_hash)
        for name in self.fields:
            pended_form.data.get_or_create(name=name, value=self.data[name])
        return form_hash

###### Reconstituting a Form

@ classmethod
def resume(cls, form_hash):
    import_path = cls.get_import_path()
    form = models.PendForm.objects.get(form_class=import_path, hash=form_hash)
    data = dict((d.name, d.value) for d in form.data.all())
    return cls(data)

###### A Full Workflow
1. Display an empty form.
2. User fills in some data.
3. User clicks Submit
4. Validate data submitted by the user.
5. Display th form with errors.
6. User clicks Pend.
7. Save form values in the database.
8. Validate data retrieved from the database.
9. Display the form with errors.
10. Process the completed form.

- User requests a form without any data.
- User posts data using th Pend button.
- User requests a form using a form hash.
- User posts data using the Submit button.

from django import http
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from properties import models, forms

def make_offer(request, id, template_name='', form_hash=None):
    if request.method == 'POST':
        form = forms.Offer(request.POST)
        if 'pend' in request.POST:
            form_hash = form.pend()
            return http.HttpRedirect(form_hash)
        else:
            if form.is_valid():
                # This is where actual processing would take place
        else:
            if form_hash:
                form = form.Offer.resume(form_hash)
            else:
                form = form.Offer()
        return render_to_response(template_name, {'form': form},
                                  context_instance=RequestContext(request))

### better
from pend_form.decorators import pend_form

@pend_form
def make_offer(request, id, form):
    # This is where actual processing would take place

from django import http
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from django.utils.functional import wraps

def pend_form(view):
    @wraps(view)
    def wrapper(request, form_class, template_name,
                form_hash=None, *args, **kwargs):
        if request.method == 'POST':
            form = form_class(request.POST)
            if 'pend' in request.POST:
                form_hash = form.pend()
                return http.HttpRedirect(form_hash)
            else:
                if form.is_valid():
                    return view(request, form=form, *args, **kwargs)
        else:
            if form_hash:
                form = form_class.resume(form_hash)
            else:
                form = form_class()
                return render_to_response(template_name, {'form': form},
                                          context_instance=RequestContext(request))
        return wrapper

###### A Class-Based Approach

from django.views.generic.edit import FormView
from pend_form.models import PendedValue

class PendFormView(FormView):
    form_hash_name = 'form_hash'

    def get_form_kwargs(self):
        """
        Returns a dictionary of arguments to pass into the form instantiation.
        If resuming a pended form, this will retrieve data from the database.
        """
        form_hash = self.kwargs.get(self.form_hash_name)
        if form_hash:
            import_path = self.get_import_path(self.get_form_class())
            return {'data': self.get_pended_data(import_path, form_hash)}
        else:
            return super(PendFormView, self).get_form_kwargs()

    # Utility methods

    def get_import_path(self, form_class):
        return '%s.%s' % (form_class.__module__, form_class.__name__)

    def get_pended_data(self, import_path, form_hash):
        data = PendedValue.objects.filter(import_path=import_path, form_hash=form_hash)
        return dict((d.name, d.value) for d in data)

###
from django.views.generic.edit import FormView
from pend_form.models import PendedForm, PendedValue

class PendFormView(FormView):
    pend_button_name = 'pend'

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests with form data. If the form was pended, it doesn't folloe
        the normal flow, but saves the values for later instead.
        """
        if self.pend_button_name in self.request.POST:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            self.form_pended(form)
        else:
            super(PendFormView, self).post(request, *args, **kwargs)

    # Custom methods follow

    def get_import_path(self, form_class):
        return '%s.%s' % (form_class.__module__, form_class.__nam__)

    def get_form_hash(self,form):
        content = ','.join('%s:%s' % (n, form.data[n]) for n in form.fields.keys())
        return md5(content).hexdigest()

    def form_pended(self, form):
        import_path = self.get_import_path(self.get_form_class())
        form_hash = self.get_form_hash(form)
        pended_form = PendedForm.objects.get_or_create(form_class=import_path,
                                                       hash=form_hash)
        for name in form.fields.keys():
            pended_form.data.get_or_create(name=name, value=form.data[name])
        return form_hash

### form_pended()
from django.views.generic.edit import FormView
from pend_form.models import PendedForm, PendedValue

class PendFormView(FormView):
    form_hash_name = 'form_hash'
    pend_button_name = 'pend'

    def get_form_kwargs(self):
        """
        Returns a dictionary of arguments to pass into the form instantiation.
        If resuming a pended form, this will retrieve data from the database.
        """
        form_hash = self.kwargs.get(self.form_hash_name)
        if form_hash:
            import_path = self.get_import_path(self.get_form_class())
            return {'data': self.get_pended_data(import_pat, form_hash)}
        else:
            return super(PendFormView, self).get_form_kwargs()

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests with form data. If the form was pended, it doesn't follow
        the normal flow, but saves the values for later instead.
        """
        if self.pend_button_name in self.request.POST:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            self.form_pended(form)
        else:
            super(PendFormView, self).post(request, *args, **kwargs)

        # Custom methods follow

        def get_import_path(self, form_class):
            return '{0}.{1}'.format(form_classs.__module__, form_class.__name__)

        def get_form_hash(self, form):
            content = ','.join('{0}:{1}'.format(n, form.data[n] for n in form.fields.keys())
            return md5(content).hexdigest()

        def form_pended(self, form):
        import_path = self.get_import_path(self.get_form_class())
        form_hash = self.get_form_hash(form)
        pended_form = PendedForm.objects.get_or_create(form_class=import_path,
                                                       hash=form_hash)
        for name in form.fields.keys():
            pended_form.data.get_or_create(name=name, value=form.data[nam])
        return form_hash

        def get_pended_data(self, import_path, form_hash):
            data = PendedValue.objects.filter(import_path=import_path, form_hash=form_hash)
            return dict((d.nam, d.value) for d in data)

######
