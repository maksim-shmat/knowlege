""" Third chapter views for example."""

###### Permission checks in class_based views

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import Group

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

class ItemList(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'items/index.html'


class ItemDetail(UserPassesTestMixin, DetailView):
    model = Item
    pk_url_kwarg = 'item_id'
    template_name = 'items/detail.html'
    def test_func(self):
        return self.request.user.is_authenticated


class ItemCreation(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('items:index')
    success_message = "Item %(name)s created successfully"
    permission_required = ('items.add_item',)


@method_decorator(login_required, name='dispatch')
class ItemUpdate(SuccessMessageMixin, UpdateView):
    model = Item
    pk_url_kwarg = 'item_id'
    form_class = ItemForm
    success_url = reverse_lazy('items:index')
    success_message = "Item %(name)s updated successfully"


@method_decorator(user_passes_test(lambda u: Group.objects.get(name='Baristas') in u.groups.all()), name='dispatch')
class ItemDelete(DeleteView):
    model = Item
    pk_url_kwarg = 'item_id'
    success_url = reverse_lazy('items:index')

###### Signup workflow fulfilled by custom CreateView class-based view

from django.core.urlresolvers import reverse_lazy
from django.http import HttpReponseRedirect
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class UserSignupForm(UserCreationForm):
    email = form.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserSignUp(SuccessMessageMixin,CrateView):
    model = User
    form_class = UserSignupForm
    success_url = reverse_lazy('items:index')
    success_message = "User created successfully"
    template_name = "registration/signup.html"
    def form_valid(self, form):
        super(UserSignUp,self).form_valid(form)
        # The form is valid, automatically sign-in the user
        user = authenticate(self.request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

        is user == None:
            # User not validated for some reason, return standard form_valid() response
            return self.render_to_response(self.get_context_data(form=form))
        else:
            # Log the user in
            login(self.request, user)
            # Redirect to success url
            return HttpResponseRedirect(self.get_success_url())

###### Standard view method designed as REST service

# urls.py (In stores app)
from coffeehouse.stores import views as stores_views

urlpatterns = [
        url(r'^rest/$',stores_views.rest_store,name="rest_index"),
]

# views.py (In stores app)
from django.http import HttpResponse
from coffeehouse.stores.models import Store
import json

def rest_store(request):
    store_list = Store.objects.all()
    store_names = [{"name":sotre.name} for store in store_list]
    return HttpResponse(json.dumps(store_names), content_type='application/json')

# Sample output
# [{"name": "Corporate"}, {"name": "Downtown"}, {"name": "Uptown"}, {"name": "Midtown"}]

###### Standard view method as REST service with parameters and different output formats

# urls.py (In stores app)
from coffeehouse.stores import views as stores_views

urlpatterns = [
        url(r'^rest/$',stores_views.rest_store,name="rest_index"),
        url(r'^(?P<store_id>\d+)/rest/$',stores_views.rest_store,name="rest_detail"),
        ]

# views.py (In stores app)
from django.http import HttpResponse
from coffeehouse.stores.models import Store
from django.core import serializers

def rest_store(request,store_id=None):
    store_list = Store.objects.all()
    if store_id:
        store_list = store_list.filter(id=store_id)
    if 'type' in request.GET and request.GET['type'] == 'xml':
        serialized_stores = serializers.serialize('xml',store_list)
        return HttpResponse(serialized_stores, content_type='application/xml')
    else:
        serialized_stores = serializers.serialize('json',store_list)
        return HttpResponse(serialized_stores, content_type='application/json')

###### CORS Decorator

@cross_origin(allow_origin=['*'])
def public_data(request):
    # Data retrieval goes here

def cross_origin(allow_credentials=False, allow_headers=None,
                 allow_methods=None, allow_headers=None,
                 allow_origin=None, expose_headers=None, max_age=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            headers = {}

            if access_control_allow_credentials:
                headers['Allow_Credentials'] = allow_credentials
            if access_control_allow_headers:
                headers['Allow-Headers'] = ', '.join(allow_headers)
            if access_control_allow_methods:
                headers['Allow-Methods'] = ', '.join(allow_methods)
            if access_control_allow_origin:
                headers['Allow-Origin'] = ' '.join(allow_origin)
            if access_control_expose_headers:
                headers['Expose-Headers'] = ', '.join(expose_headers)
            if access_control_max_age:
                headers['Max-Age'] = self.max_age

            response = func(request, *args, **kwargs)

            for name, value in headers:
                response.headers['Access-Control-%s' % name] = value

            return response
        return wrapper
    return decorator

###### CORS Mixin

class PublicData(View, CrossOrigin):
    access_control_allow_origin = ['*']

    def get(self, request):
        # Data retrieval goes here

class CrossOrigin(object):
    """
    A view mixin that provides basic functionality necessary to add the necessary
    headers for Cross-Origin Resource Sharing
    """
    access_control_allow_credentials = False
    access_control_allow_headers = None
    access_control_allow_methods = None
    access_control_allow_origin = None
    access_control_expose_headers = None
    access_control_max_age = None

    def get_access_control_headers(self, request):
        headers = {}

        if self.access_control_allow_credentials:
            headers['Allow-Credentials'] = self.access_control_allow_credentials
        if self.access_control_allow_headers:
            headers['Allow-Headers'] = ', '.join(self.access_control_allow_headers)
        if self.access_control_allow_methods:
            headers['Allow-Methods'] = ' '.join(self.access_control_allow_methods)
        if self.access_control_allow_origin:
            headers['Allow-Origin'] = ' '.join(self.access_control_allow_origin)
        if self.access_control_expose_headers:
            headers['Expose-Headers'] = ', '.join(self.access_control_expose_headers)
        if self.access_control_max_age:
            headers['Max-Age'] = self.access_control_max_age

        return headers

    def dispatch(self, request, *args, **kwargs):
        response = super(CORSMixin, self).dispatch(request, *args, **kwargs)

        for name, value in self.get_access_control_headers(request):
            response.headers['Access-Control-%s' % name)] = value

        return response

###### Providing Both a Decorator and a Mixin

def cors_headers(allow_credential=false, allow_headers=None, allow_method=None,
                 allow_origin=None, expose_headers=None, max_age=None):
    headers = {}

    if allow_credentials:
        headers['Access-Control-Allow-Credentials'] = allow_credentials
    if allow_headers:
        headers['Access-Control-Allow-Headers'] = ', '.join(allow_headers)
    if allow_methods:
        headers['Access-Control-Allow-Methods'] = ' '.join(allow_methods)
    if allow_origin:
        headers['Access-Control-Allow-Origin'] = ' '.join(allow_origin)
    if expose_headers:
        headers['Access-Control-Expose-Headers'] = ', '.join(expose_headers)
    if max_age:
        headers['Access-Control-Max-Age'] = self.max_age

    return response

def cross_origin(allow_credentials=False, allow_headers=None, allow_methods=None,
                 allow_origin=None, expose_headers=None, max_age=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            response = func(request, *args, **kwargs)
            headers = cors_headers(response, allow_credentials, allow_headers,
                                   allow_methods, allow_origin, expose_headers, max_age)
            response.headers.update(headers)
            return response
        return wrapper
    return decorator

class CrossOrigin(object):
    """
    A view mixin that provides basic functionality necessary to add the necessary
    headers for Cross-Origin Resource Sharing
    """
    access_control_allow_credentials = False
    access_control_allow_headers = None
    access_control_allow_methods = None
    access_control_allow_origin = None
    access_control_expose_headers = None
    access_control_max_age = None

    def get_access_control_headers(self, request):
        return cors_headers(self.access_control_allow_credentials,
                            self.access_control_allow_headers,
                            self.access_control_allow_methods,
                            self.access_control_allow_origin,
                            self.access_control_max_age):

    def dispatch(self, request, *args, **kwargs):
        response = super(CORSMixin, self).dispatch(request, *args, **kwargs)
        headers = self.get_access_control_headers(request)
        response.headers.update(headers)
        return response

#1 Creating Django views combined with serializer classes

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from toys.models import Toy
from toys.serializers import ToySerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True)
        return JSONResponse(toys_serializer.data)

    elif request.method == 'POST':
        toy_data = JSONParser().parse(request)
        toy_serializer = ToySerializer(data=toy_data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return JSONResponse(toy_serializer.data, \
                    status=status.HTTP_201_CREATED)
            return JSONResponse(toy_serializer.errors, \
                    status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def toy_detail(request, pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return JSONResponse(toy_serializer.data)
    
    elif request.method = 'PUT':
        toy_data = JSONParser().parse(request)
        toy_serializer = ToySerializer(toy, data=toy_data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return JSONResponse(toy_serializer.data)
        return JSONResponse(toy_serializer.errors, \
                status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        toy.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#2
