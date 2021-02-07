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

###########

