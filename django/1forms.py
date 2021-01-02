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


