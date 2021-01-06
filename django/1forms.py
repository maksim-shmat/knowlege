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
##########

