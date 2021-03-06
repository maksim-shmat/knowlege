""" Forms examples."""

# Set the fields attribute to the special value '__all__' to indicate that
# all fields in the model should be used.

from django.forms import ModelForm

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

# Set exlude attribute of the ModeForm's inner Meta class to a list of fields
# to be excluded from the form.

class PartialAuthorForm(ModelForm):
    class Meta:
        model = Author
        exlude = ['title']

###########

# Overriding the default fields

from django.form import ModelForm, Textarea
from myapp.models import Author

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields  = ('name', 'title', 'birth_date')
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

###

from django.utils.translation import gettext_lazy as _

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title', 'birth_date')
        label = {
            'name': _('Writer'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }
###

from django.forms import ModelForm
from myapp.models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter', 'slug']
        field_classes = {
                'slug': MySlugFormField,
        }
###

from django.forms import CharField, ModelForm
from myapp.models import Article

class ArticleForm(ModelForm):
    slug = CharField(validators=[validate_slug])

    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter', 'slug']

########
# Using a custom queryset

from django.forms import modelformset_factory
from django.shortcuts import render
from myapp.models import Author

def manage_authors(request):
    AuthorFormSet = modelFormset_factory(Author, fields=('name', 'title'))
    if request.method == "POST":
        formset = AuthorFormSet(
                request.POST, request.FILES,
                queryset=Author.objects.filter(name__startswith='O'),
        )
        if formset.is_valid():
            formset.save()
            # Do something.
    else:
        formset =
AuthorFormSet(queryset=Author.objects.filter(name__startswith='O'))
return render(request, 'manage_authors.html', {'formset': formset})

############
# Basic forms
# forms.py

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
# The view can be constructed using a FormView
# views.py

from myapp.forms import ContactForm
from django.views.generic.edit import FormView

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

########## configuring the rendering of a form's widgets

from django import forms

class MyForm(forms.Form):
    default_renderer = MyRenderer()

### customizing BoundField

class GPSCoordinatesBoundField(BoundField):
    @property
    def country(self):
        """
        Return the country the coordinates lie in or None if it can't be
        determined.
        """
        value = self.value()
        if value:
            return get_country_from_coordinates(value)
        else:
            return None


class GPSCoordinatesField(Field):
    def get_bound_field(self, form, field_name):
        return GPSCoordinatesBoundField(form, self, field_name)

### MultiValueField

from django.core.validators import RegexValidator

class PhoneField(MultiValueField):
    def __init__(self, **kwargs):
        # Define one message for all fields.
        error_messages = {
                'incomplete': 'Enter a country calling code and a phone number.',}
        # Or define a different message for each field.
        fields = (
                CharField(
                    error_messages={'incomplete': 'Enter a country calling
                    code.'},
                    validators=[
                        RegexValidator(r'^[0-9]+$', 'Enter a valid country
                        calling code.'),
                        ],
                    ),
                CharField(
                    error_messages={'incomplete': 'Enter a phone number.'},
                    validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')],
                    ),
                CharField(
                    validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid extension.')],
                    required=False,
                ),
            )
        super().__init__(
                error_messages=error_messages, fields=fields,
                require_all_fields=False, **kwargs
        )

############## SplitDateTimeField

class FooMultipleChoiceForm(forms.Form):
    foo_select = forms.ModelMultipleChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foo_select'].queryset = ...

### ModelChoiceField

from django.forms import ModelChoiceField

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "My Object #%i" % obj.id

### ModelMultipelChoiceField

from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)

###

from django import forms

class ToppingSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['date-price'] = value.instance.price
        return option

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['topping']
        widgets = {'topping': ToppingSelect}

############# specifying widgets

from django import forms

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)

########### setting arguments for widgets

from django import forms

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLOR_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
]

class SimpleForm(forms.Form):
    birth_year = 
    forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=FAVORITE_COLORS_CHOICES,
    )

############ styling widget instances

from django import forms

class CommentForm(forms.Form):
    name = form.CharField()
    url = forms.URLField()
    comment = forms.CharField()

###
class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    url = forms.URLField()
    comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))

###
class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField()

    name.widget.attrs.update({'class': 'special'})
    comment.widget.attrs.update(size='40')

###
class CommentForm(forms.ModelForm):
    def __input__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'special'})
        self.fields['comment'].widget.attrs.update(size='40')

########### MultiWidget
# decompress(value)

from django.forms import MultiWidget

class SplitDateTimeWidget(MultiWidget):
    # ...
    def decompress(self, value):
        if value:
            return [value.date(), value.time()]
        return [None, None]

### the widget template
{% for subwidget in widget.subwidgets %}
  {% include subwidget.template_name with widget=subwidget %}
{% endfor %}

###
from datetime import date
from django import forms

class DateSelectorWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        days = [(day, day) for day in range(1, 32)]
        months = [(month, month) for month in range(1, 13)]
        years = [(year, year) for year in [2018, 2019, 2020]]
        widgets = [
                forms.Select(attrs=attrs, choices=days),
                forms.Select(attrs=attrs, choices=months),
                forms.Select(attrs=attrs, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.day, value.month, value.year]
        elif isinstance(value, str):
            year, month, day = value.split('-')
            return [day, month, year]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        day, month, year = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.
        return '{}-{}-{}'.format(year, month, day)

########### form field default cleaning

from django import forms
from django.core.validators import validate_email

class MultiEmailField(forms.Field):
    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(',')

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        for email in value:
            validate_email(email)

###
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    recipients = MultiEmailField()
    cc_myself = forms.BooleanField(required=False)

############## cleaning a specific field attribute

from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    # Everything as before.
    ...

    def clean_recipients(self):
        data = self.cleaned_data['recipients']
        if "fred@example.com" not in data:
            raise ValidationError("You have forgotten about Fred!")
        # Always return a value to use as the new cleaned data, even if
        # this method did't change it.
        return data

############ cleaning and validating fields that depend on each other

from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    # Everything as before.
    ...

    def clean(self):
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")

        if cc_myself and subject:
            # Only do something if both fields are valid so far.
            if "help" not in subject:
                raise ValidationError(
                        "Did not send for 'help' in the subject despite "
                        "CC`ing yourself."
                        )

###
def clean(self):
    super().clean()
    cc_myself = self.cleaned_data.get("cc_myself")
    ...

###
from django import forms

class ContactForm(forms.Form):
    # Everything as before.
    ...

    def clean(self):
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")

        if cc_myself and subject and "help" not in subject:
            msg = "Must put 'help' in subject when cc'ing yourself."
            self.add_error('cc_myself', msg)
            slef.add_error('subject', msg)

############## django form class definition
# forms.py in app named 'contact'

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(label='Your email')
    comment = forms.CharField(widget=forms.Textarea)

########### django view method that uses a django form
# views.py in app named 'contact'

from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    form = ContactForm()
    return render(request, 'about/contact.html',{'form':form})

### django form instance rendered in template as HTML
<tr><th><label for="id_name">Name:</label></th><td><input id="id_name" name="name" type="text" /></td></tr>
<tr><th><label for="id_email"><Your email:</label></th><td><input id="id_email" required name="email" type="email" /></td></tr>
<tr><th><label for="id_comment">Comment:</label></th><td><textarea cols="40" id="id_comment" required name="comment" row="10">
</textarea></td></tr>

########## django form template declaration for functional web form

<form method="POST">
  {% csrf_token %}

<table>
{{form.as_table}}
</table>
<input type="submit" value="Submit form">
</form>

######### django view method that sends and processes Django form

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            # process data, insert into DB, generate email, etc
            # redirect to a new URL:
            return HttpResponseRedirect('/about/contact/thankyou')
        else:
            # GET, generate blank form
            form = ContactForm()
        return render(request, 'about/contact.html',{'form':form})

########### django form with automatic ids(default auto_id=True option) and no automatic ids auto_id=False option

<!-- Option 1, default auto_id=True -->
<tr><th><label for="id_name">Name:</label></th><td><input id="id_name" name="name" type="text" /></td></tr>
<tr><th><label for="id_email">Your email:</label></th><td><input id="id_email" name="email" type="email" /></td></tr>
<tr><th><label for="id_comment">Comment:</label></th><td><textarea cols="40" id="id_comment" name="comment" rows="10">
</textarea></td></tr>

<!-- Option 2 auto_id=False -->
<tr><th>Name:</th><td><input name="email" type="email" /></td></tr>
<tr><th>Comment:</th><td><textarea cols="40" name="comment" rows="10">\r\n</textarea>
</td></tr>

###########

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(label='Your email')
    comment = forms.CharField(widget=forms.Textarea)
    field_order = ['email','comment','name'] # Set order email,comment,name

########### django form is_valid() method for form processing

from django.http import HttpResponseRedirect

def contact(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # Reference is now a bound instance with user data sent in POST
        # Call is_valid() to validate data and create cleaned_data and errors dict
        if form.is_valid():
            # Form data is valid, you can now access validated values in the cleaned_data dict
            # e.g form.cleaned_data['email']
            # process data, insert into DB, generate email
            # Redirect to a new URL
            return HttpResponseRedirect('/about/contact/thankyou')
        else:
            pass # Not needed
            # is_valid() method created errors dict, so form reference now contains errors
            # this form reference drops to the last return statement where errors
            # can then be presented accessing form.errors in a template
    else:
        # GET, generate blank form
        form = ContactForm()
        # Reference is now an unbound (empty) form
    # Reference form instance (bound/unboun) is sent to template for rendering
    return render(request,'about/contact.html',{'form':form})

########## django form field validators option with custom validator method for form processing

from django import forms
import re

def validate_commit_word_count(value):
    count = len(value.split())
    if count < 30:
        raise forms.ValidationError(('Please provide at least a 30 word message, %(count)s words is not descriptive enough'), params={'count': count},)

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(label='Your email')
    comment = forms.CharField(widget=forms.Textarea,validators=[validate_comment_word_count])

########### django form field validation with clean_<filed>() methods

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(label='Your email')
    comment = forms.CharField(widget=forms.Textarea)
    
    def clean_name(self):
        # Get the field value from cleaned_data dict
        value = self.cleaned_data['name']
        # Check if the value is all upper case
        if value.isupper():
            # Value is all upper case, raise an error
            raise forms.ValidationError("Please don't use all upper case for your name, use lower case",code='uppercase')
        # Always return value
        return value

    def clean_email(self):
        # Get the field value from cleaned_data dict
        value = self.cleaned_data['email']
        # Check if the value end in @hotmail.com
        if value.endswith('@hotmail.com'):
            # Value ends in @hotmail.com, raise an error
            raise forms.ValidationError("Please don't use a hotmail email, we simply don't like it",code='hotmail')
        # Always return value
        return value

###### django form field validation with clean() method
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(label='Your email')
    comment = forms.CharField(widget=forms.Textarea)

    def clean(self):
        # Call clean() method to ensure base class validation
        super(ContactForm, self).clean()

        # Get the field values from cleaned_data dict
        name = self.cleaned_data.get('name','')
        email = self.cleaned_data.get('email','')

        # Check if the name is part of the email
        if name.lower() not in email:
            # Name is not in email, raise an error
            raise forms.ValidationError("Please provide an email that contains your name, or viceversa")

########## django form field error assignment with add_error() in clean() method

def clean(self):
    # Call clean() method to ensure base class validation
    super(ContactForm, self).clean()

    # Get the field values from cleaned_data dict
    name = self.cleaned_data.get('name','')
    
    # Check if the name is part of the email
    if name.lower() not in email:
        # Name is not in email, raise an error
        message = "Please provide an email that contains your name, or viceversa"
        self.add_error('name', message)
        self.add_error('email', forms.ValidationError(message))
        self.add_error(None, message)

########### django form ValidationError instance creation

from django import forms

# Placed inside def clean_email(self):
raise forms.ValidationError("Please don't use a hotmail email, we simply don't like it",code='hotmail')

# Placed inside def clean(self):
raise forms.ValidationError([
    forms.ValidationError("Please provide an email that matches your name, or viceversa",code='custom'),
    forms.ValidationError("Please provide your professional email, %(value)s doesn't look professional ",code='required',params={'value':self.cleaned_data.get('email') })

######## django form  output with form.as_table

<tr>
  <th><label for="id_name">Name:</label></th>
  <td><input id="id_name" name="name" type="text" /></td>
</tr>\n
<tr>
  <th><label for="id_email">Your email:</label></th>
  <td><input id="id_email" name="email" type="email" required/></td>
</tr>\n
<tr>
  <th><label for="id_comment">Comment:</label></th>
  <td><textarea cols="40" id="id_comment" name="comment" rows="10" required>\r\n</textarea></td>
</tr>

####### djanago form output with form.as_p

<p>
  <label for="id_name">Name:</label> <input id="id_name" name="name" type="text" /></p>\n
</p>
<p>
  <label for="id_email">Your email:</label> <input id="id_email" name="email" type="email" required/>
</p>\n
<p>
  <label for="id_comment">Comment:</label> <textarea cols="40" id="id_comment" name="comment" rows="10" required>\r\n</textarea>
</p>

####### django form output with form.as_ul

<li>
  <label for="id_name">Name:</label> <input id="id_name" name="name" type="text" />
</li>\n
<li>
  <label for="id_email">Your email:</label> <input id="id_email" name="email" type="email" required/>
</li>\n
  <li><label for="id_comment">Comment:</label> <textarea cols="40" id="id_comment" name="comment" rows="10" required>\r\n</textarea>
</li>

######## django form {% for %} loop over all fields

{% for field in form %}
  <div class="row">
    <div class="col-md-2">
    {{ field.label_tag }}
    {% if field.help_text %}
      <sup>{{ field.help_text }}</sup>
    {% endif %}
    {{ field.errors }}
    </div><div class="col-md-10 pull-left">
      {{ field }}
    </div>
  </div>
{% endfor %}

####### django form field_order option to enforce field order
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(label='Your email')
    comment = forms.CharField(widget=forms.Textarea)
    field_order = ['email','comment','name']

###### django form error_css_class and required_css_class fields to apply CSS formating from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(label='Your email')
    comment = forms.CharField(widget=forms.Textarea)
    error_css_class = 'error'
    required_css_class = 'bold'

###### django form with inline widget definition to add custom CSS class

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(label='Your email', widget=forms.TextInput(attrs={'clss': 'myemailclass'}))
    comment = forms.CharField(widget=forms.Textarea)

###### django loop over form.<field_name>.errors
{% for field in form %}
  <div class="row">
    <div class="col-md-2">
      {{ field.label_tag }}
        <sup>{{ field.help_text }}</sup>
        {% endif %}
        {% for error in field.errors %}
        <div class="row">
          <div class="alert alert-danger">{{error}}</div>
        </div>
        {% endfor %}
    </div><div class="col-md-10 pull-left">
      {{ field }}
    </div>
  </div>
{% endfor %}

###### django form.errors and form.non_field_errors with custom HTML output

<!-- Field errors -->
  {% if form.errors %}
    <div class="row">
      {% for field_with_error,error_message in form.errors.items %}
        <div class="alert alert-danger">{{field_with_error}} {{error_messages}}</div>
      {% endfor %}
    </div>
    {% endif %}

<!-- Non-field errors -->
  {% if form.non_field_errors %}
    <div class="row">
      {% for error in form.non_field_errors %}
      <div class="alert alert-danger">{{error}}</div>
      {% endfor %}
    </div>
    {% endif %}

###### django custom form field inherits behavior from forms.ChoiceField

class GenderField(forms.ChoiceField):
    def __init__(self, *args, **kwargs):
        super(GenderField, self).__init__(*args, **kwargs)
        self.error_messages = {"required": "Please select a gender, it's required"}
        self.choices = ((None, 'Select gender'),('M', 'Male'), ('F', 'Female'))

###### django custom form widget inherits behavior from forms.widgets.Input

class PlaceholderInput(forms.widgets.Input):
    template_name = 'about/placeholder.html'
    input_type = 'text'
    def get_context(self, name, value, attrs):
        context = super(PlaceholderInput, self).get_context(name, value, attrs)
        context['widget']['attrs']['maxlength'] = 50
        context['widget']['attrs']['placeholder'] = name.title()
        return context

###### django custom form widget inherits behavior from forms.widgets.Input

# about/placeholder.html
<input type="{{ widget.type }}" name="{{ widget.name }}"{% if widget.value != None %}
value="{{ widget.value }}"{% endif %}{% include "django/forms/widgets/attrs.html" %} ?>

# django/forms/widgets/attrs.html
{% for name, value in widget.attrs.items %}{% if value is not False %} {{ name }}{% if value is not True %}="{{ value }}"{% endif %}{% endif %}{% endfor %}

###### Django form with field marked as hidden

<form method="POST">
  {% csrf_token %}
    <div class="row">
      <div class="col-md-2">
        {{ form.comment.label_tag }}
          {% if form.comment.help_text %}
          <sup>{{ form.comment.help_text }}</sup>
          {% endif %}
          {% for error in form.comment.errors %}
          <div class="row">
          <div class="alert alert-danger">{{error}}</div>
          </div>
          {% endfor %}
      </div><div class="col-md-10 pull-left">
        {{ form.comment }}
      </div>
    </div>
  {{form.name.as_hidden}}
  {{form.email.as_hidden}}
<input type="submit" value="Submit form" class="btn btn-primary">
</form>

###### Django form subclass with removed parent fields

from coffeehouse.about.forms import ContactForm

class ContactCommentOnlyForm(ContactForm):
    def __init__(self, *args, **kwargs):
        super(ContactCommentOnlyForm, self).__init__(*args, **kwargs)
        del self.fields['name']
        del self.fields['email']

###### JavaScript logic to submit Django form via Ajax
# NOTE: The following is only the Django (HTML) template with AJAX logic
# See Listing 6-35 for AJAX processing views.py and urls.py
<h4>Feedback</h4>
<div class="row">
  <div id="feedbackmessage"</div>
</div>
<form method="POST" id="feedbackform" action="{% url 'stores:feedback' %}">
  {% csrf_token %}
    <div class="row">
      <div class="col-md-12 pull-left">
        {{ form.comment }}
      </div>
    </div>
    {{form.name.as_hidden}}
    {{form.email.as_hidden}}
<input type="submit" value="Submit feedback" class="btn btn-primary">
</form>

<script>
$(document).ready(function() {
    $("#feedbackform").submit(function(event) {
        event.preventDefault();
        $.ajax({ data: $(this).serialize(),
                 type: $(this).attr('method'),
                 url: $(this).attr('action'),
                 success: function(response) {
                     console.log(response);
                     if(response['success']) {
                         $("#feedbackmessage").html("<div class='alert alert-success'>
                         Successfully sent feedback, thank you!</div>");
                         $("#feedbackform").addClass("hidden");
                     }
                     if (response['error']) {
                         $("#feedbackmessage").html("<div class='alert alert-danger'>" + response['error']['comment'] +"</div>");
                     }
                 },
                 error: function (request, status, error) {
                     console.log(request.responseText);
                 }
            });
        });
    });
</script>

###### Django view method to process Django form via AJAX
# urls.py (Main)

urlpatterns = [
        url(r'^stores/',include('coffeehouse.stores.urls',namespace="stores"))
]

# urls.py (App stores)

urlpatterns = [
        url(r'^$',views.index,name="index"),
        url(r'^feedback/$',views.feedback,name="feedback"),
]

# views.py (App stores)

from django.http import HttpResponse, JsonResponse
from coffeehouse.about.forms import ContactForm

def feedback(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'error':form.errors})
    return HttpResponse("Hello from feedback!")

###### Django form with file fields, corresponding view method, and template layout

# forms.py
from django import forms

class SharingForm(forms.Form):
    # NOTE: forms.PhotoField requieres Python PIL & other operating system libraries,
    #       so generic FileField is used instead
    video = forms.FileField()
    photo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

# views.py

def index(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = SharingForm(request.POST,request.FILES)
        # check if it's valid:
        if form.is_valid():
            # Process file data in request.FILES
            # Process data, insert into DB, generate email,etc
            # redirect to a new URL:
            return HttpResponseRedirect('/about/contact/thankyou')
    else:
        # GET, generate blank form
        form = SharingForm()
    return render(request,'social/index.html',{'form':form})

# social/index.html
<form method="post" enctype="myltipart/form-data">
  {% csrf_token %}
  <ul>
    {{form.as_ul}}
  </ul>
    <input type="submit" value="Submit photo" class="btn btn-primary">
</form>

###### Django form file processing with save procedure to MEDIA_ROOT
# views.py

from django.conf import settings

def save_uploaded_file_to_media_root(f):
    with open('%s%s' % (settings.MEDIA_ROOT,f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    if request.methon == 'POST':
        # POST, generate form with data from the request
        form = SharingForm(request.POST,request.FILES)
        # check if it's valid:
        if form.is_valid():
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    save_uploaded_file_to_media_root(formfile)
            return HttpResponseRedirect('/about/contact/thankyou')
    else:
        # GET, generate blank form
        form = SharingForm()
    return render(request,'social/index.html',{'form':form})

###### django formset factory initialization and template layout
# forms.py

from django import forms

DRINKS = ((None,'Please select a drink type'),(1,'Mocha'),(2,'Espresso'),(3,'Latte'))
SIZES = ((None,'Please select a drink size'),('s','Small'),('m','Medium'),('l','Large'))

class DrinkForm(forms.Form):
    name = forms.ChoiceField(choices=DRINKS,initial=0)
    size = forms.ChoiceField(choices=SIZES,initial=0)
    amount = forms.ChoiceField(choices=[(None,'Amount of drinks')]+[(i,i) for i in range(1,10)])

# views.py

from django.forms import formset_factory

def index(request):
    DrinkFormSet = formset_factory(DrinkForm, extra=2, max_num=20)
    if request.method == 'POST':
        # TODO
    else:
        formset = DrinkFormSet(initial=[{'name':1,'size':'m','amount':1}])
    return render(request,'online/index.html',{'formset':formset})

# online/index.html

<form method="post">
    {% csrf_token %}
  {{ formset.management_form }}
  <table>
    {% for form in formset %}
    <tr><td><ul class="list-inline">{{ form.as_ul }}</ul></td></tr>
    {% endfor %}
  </table>
  <input type="submit" value="Submit order" class="btn btn=primary">
</form>

######## django formset designed to add extra forms by user
# view.py

def index(request):
    extra_forms = 2
    DrinkFormSet = formset_factory(DrinkForm, extra=extra_forms, max_num=20)
    if request.method == 'POST':
        if 'additems' in request.POST and request.POST['additems'] == 'true':
            formset_dictionary_copy = request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(formset_dictionary_copy
            ['form-TOTAL_FORMS']) + extra_forms
            formset = DrinkFormSet(formset_dictionary_copy)
        else:
            formset = DrinkFormSet(request.POST)
            if formset.is_valid():
                return HttpResponseRedirect('/about/contact/thankyou')
    else:
        formset = DrinkFormSet(initial=[{'name': 1, 'size': 'm', 'amount': 1}])
    return render(request, 'online/index.html', {'formset': formset})

# online/index.html

<form method="post">
    {% csrf_token %}
  {{ formset.management_form }}
  <table>
    {% for form in formset %}
    <tr><td>{{ form }}</td></tr>
    {% endfor %}
  </table>
  <input type="hidden" value="false" name="additems" id="additems">
  <button class="btn btn-primary" id="additemsbutton">Add items to order</button>
  <input type="submit" value="Submit order" class="btn btn-primary">
</form>

<script>
$(document).ready(function() {
    $("#additemsbutton").on('click',function(event) {
        $("#additems").val("true");
    });
});
</script>

###### Django custom formset with custom validation

from django.forms import BaseFormSet

class BaseDrinkFormSet(BaseFormSet):
    def clean(self):
        # Check errors dictionary first, if there are any error, no point in validating further
        if any(self.errors):
            return
        name_size_tuples = []
        for form in self.forms:
            name_size = (form.cleaned_data['name'],form.cleaned_data['size'])
            if name_size in name_size_tuples:
                raise forms.ValidationError("Ups! You have multiple %s %s items in your order, keep one and increase the amount" % (dict(SIZES)
                [name_size[1]],dict(DRINKS)[int(name_size[0])]))
            name_size_tuples.append(name_size)

###### django custom formset to display non_form_errors

<form method="post">
    {% csrf_token %}
  {{ formset.management_form }}
  {% if formset.non_form_errors %}
    <div class="alert alertdanger">{{formset.non_form_errors}}</div>
  {% endif %}
    {{ formset.management_form }}
  <table>
    {% for form in formset %}
    <tr><td<>ul class="list-inline">{{ form.as_ul }}</ul></td></tr>
    {% endfor %}
  </table>
</form>

######
