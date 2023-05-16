"""Custom admin form class about."""

#1 forms.py
...
from django.forms import ..., ModelForm
from ..chapter_3.models import Engine


class EngineForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        print('EngineForm Initialized')
        super(EngineForm, self).__init__(*args, **kwargs)


    class Meta:
        model = Engine
        fields = '__all__'
