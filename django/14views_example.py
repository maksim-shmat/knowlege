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

######
