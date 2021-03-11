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

######
