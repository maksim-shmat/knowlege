"""Vidges django's about."""

#1
from django import newforms as forms  # need it? it's ancient no?

class LargeTextareaWidget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'rows': 40, 'cols': 100})
        super(LargeTextareaWidget, self).__init__(*args, **kwargs)
