""" API about."""

from django.core import serializers

class QuerySetSerializer(serializers.get_serializer('json')):
    pass

###
class QuerySetSerializer(serializers.get_serializer('json')):
    def get_dump_object(self, obj):
        return self._current

### outputing a Single Object
class SingleObjectSerializer(QuerySetSerializer):
    def serialize(self, obj, **options):
        # Wrap the object in a list in oreder to use the standard serializer
        return super(SingleObjectSerializer, self).serialize([obj], **options)
    
    def getvalue(self):
        # Strip off the outer list for just a single item
        value = super(SingleObjectSerializer, self).getvalue()
        return value.strip('[]\n')

###### Handling Relationships

class DataSerializer(serializers.get_serializer('python')):
    def get_dump_object(self, obj):
        return self._current

class QuerySetSerializer(DataSerializer, serializers.get_serializer('json')):
    pass # Behavior is now inherited from DataSerializer

###
class DataSerializer(serializers.get_serializer('python')):
    def get_dump_object(self, obj):
        return self._current

    def handle_fk_field(self, obj, field):
        # Include content from the related object
        related_obj = getattr(obj, field.name)
        value = DataSerializer().serialize([related_obj])
        self._current[field.name] = value[0]

######
class DataSerializer(serializers.get_serializer('python')):
    def serialize(self, queryset, **options):
        if hasattr(queryset, 'model'):
            model = queryset.model
        else:
            model = queryset[0].__class__
        if options.get('fields') is None and model in field_registry:
            options['fields'] = field_registry[model]
        return super(DataSerializer, self).serialize(queryset, **options)
    
    # Other methods previously described

######
from api import serialize_fields
from contacts.models import Contact
from django.contrib.auth.models import User

serialize_fields(Contact, [
    'phone_number',
    'address',
    'city',
    'state',
    'zip_code',
    'use',
])
serialize_fields(User, [
    'username',
    'first_name',
    'last_name',
    'email',
])

######
from api import serialize_fields
from contacts.models import Contact
from django.contrib.auth.models import User
from contacts.form import ContactEditorForm, UserEditorForm

serialize_fields(Contact, ContactEditorForm.base_fields.keys() + ['user'])
serialize_fields(User, UserEditorForm.base_fields.keys())

###
class DataSerializer(serializers.get_serializer('python')):
    # Other methods previously described

    def handle_m2m_field(self, obj, field):
        # Include content from all related objects
        related_objs = getattr(obj, field.name).all()
        values = DataSerializer().serialize(related_objs)
        self._current[field.name] = values

######
from django.db.models import AutoField, ForeignKey

class DataSerializer(serializers.get_serializer('python')):
    # Other methods previously described

    def get_through_fields(self, obj, field):
        extra = set()

        fro f in field.rel.through._meta.fields:
            if isinstance(f, AutoField):
                # Nothing to do with AutoFields, so just ignore it
                continue
            
            if isinstance(f, ForeignKey):
                # The source will refer to the model of our primary object
                if f.rel.to == obj.__class__:
                    source = f.name
                    continue

                # The target will be the same as on the ManyToManyField
                if f.rel.to == field.rel.to:
                    target = f.name
                    continue

            # Otherwise this is a standard field
            extra.add(f.name)
        return source, target, extra

###
api.serialize_fields(Feature, ['title', 'description'])

###
class DataSerializer(serializers.get_serializer('python')):
    # other methods previously described
    
    def handle_m2m_field(self, obj, field):
        source, target, extra_fields = self.get_through_fields(obj, field)
        fields = field_registry.get(field.rel.to, extra_fields)

        # Find all the relationships for the object passed into this method
        relationships = field.rel.through._default_manager.filter(**{source: obj})
        objects = []
        for relationships in relationships.select_related():
            # Serialize the related object first
            related_obj = getattr(relation, target)
            data = DataSerializer().serialize([related_obj])[0]

            # Then add in the relationship data, but only
            # those that were specified in the field list
            for f in fields & extra_fields:
                data[f] = getattr(relation, f)

            objects.append(data)
        self._current[field.name] = objects

###### Resource View

from django.views.generic import View

class ResourceView(View):
    serializer = None
    fields = None

    def get_fields(self):
        return self.fields

    def serialize(self, value):
        return self.serializer.serialize(value, fields=self.get_fields())

###### Resource List View

from django.http import HttpResponse
from django.views.generic import View, ListView

from api import serializers

# ResourceView is defined here

class ResourceListView(ResourceView, ListView):
    serializer = serializers.QuerySetSerializer()

    def render_to_response(self, context):
        return HttpResponse(self.serialize(context['object_list']),
                content_type='application/json')

### url
from django.conf.urls import *
from django.contrib.auth.models import User, Group

from api.serializers import serialize_fields
from api.views import ResourceListView
from contacts.models import Contact
from contacts import forms

serialize_fields(Contact, forms.ContactEditorForm.base_fields.keys() + ['user'])
serialize_fields(User, forms.UserEditorForm.base_fields.keys())
serialize_fields(Group, ['name'])

urlpatterns = patterns('',
        url(r'^$',
            ResourceListView.as_view(
                queryset=Contact.objects.all(),
            ), name='contact_list_api'),
)

###### Resource Detail View

from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView

from api import serializers

# ResourceView is define here

class ResourceListView(ResourceView, ListView):
    serializer = serializers.QuerySetSerializer()

    def render_to_response(self, context):
        return HttpResponse(self.serialize(context['object_list']),
                content_type='application/json')


class ResourceDetailView(ResourceView, DetailView):
    serializer = serializers.SingleObjectSerializer()

    def render_to_response(self, context):
        return HttpResponse(self.serialize(context['object']),
                content_type='application/json')

### url configuration

from django.conf.urls import *
from django.contrib.auth.models import User, Group

from api.serializers import serialize_fields
from api.views import ResourceListView, ResourceDetailView
from contacts.models import Contact
from contacts import forms

serialize_fields(Contact, forms.ContactEditorForm.base_fields.keys() + ['user'])
serialize_fields(User, forms.UserEditorForm.base_fields.keys())
serialize_fields(Group, ['name'])

urlpatterns = patterns('',
        url(r'^$',
            ResourceListView.as_view(
                queryset=Contact.objects.all(),
            ), name='contact_list_api'),
        url(r'^(?P<slug>[\w-]+)/$',
            ResourceDetailView.as_view(
                queryset=Contact.objects.all(),
                slug_field='user__username',
            ), name='contact_detail_api'),
)

######
