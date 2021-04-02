""" About 404 page and difference."""

######
from django.views.generic import TemplateView

class EditContact(TemplateView):
    def get(self, request, username=None):
        pass

###
from django.chortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from contacts.models import Contact

class EditContact(TemplateView):
    def get_objects(self, username):
        # Set up some default objects if none were defined.
        if username:
            user = get_object_or_404(User, username=username)
            try:
                # Return the contact directly if it already exists
                contact = user.contact
            except Contact.DoesNotExist:
                # Create a contact for the user
                contact = Contact(user=user)
            else:
                # Create both the user and an associated contact
                user = User()
                contact = Contact(user=user)
            return user, contact

        def  get(self, request, username=None):
            pass

###
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from contacts.models import Contact
from contacts import forms

class EditContact(TemplateView):
    def get_objects(self, username):
        # Set up some default objects if none were defined.
        if username:
            user = get_object_or_404(User, username=username)
            try:
                # Return the contact directly if it already exists
                contact = user.contact
            except Contact.DoesNotExist:
                # Create a contact for the user
                contact = Contact(user=user)
            else:
                # Create both the user and an associated contact
                user = User()
                contact = Contact(user=user)
            return user, contact

        def get(self, request, username=None):
            user, contact = self.get_objects()
            return self.render_to_response({
                'username': username,
                'user_form': forms.UserEditorForm(instance=user),
                'contact_form': forms.ContactEditorForm(instance=contact),
            })

###
from django.core.urlresolvers import reverse
from django.http import HttpReponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from contacts.models import User
from contacts import forms

class EditContact(TemplateView):
    def get_objects(self, username):
        # Set up some default objects if none were defined.
        if username:
            user = get_object_or_404(User, username=username)
            try:
                # Return the contact directly if it already exists
                contact = user.contact
            except Contact.DoesNotExist:
                # Create a contact for the user
                contact = Contact(user=user)
        else:
            # Create both the user and an associated contact
            user = User()
            contact = Contact(user=user)

        return user, contact

    def get(self, request):
        user, contact = self.get_objects()
        return self.render_to_response({
            'username': user.username,
            'user_form': forms.UserEditorForm(instance=user),
            'contact_form': forms.ContactEditorForm(instance=contact),
        })

    def post(self, request):
        user, contact = self.get_object()
        user_form = forms.UserEditorForm(request.POST, instance=user)
        contact_form = forms.ContactEditorForm(request.POST, instance=contact)
        if user_form.is_valid() and contact_form.is_valid():
            user = user_form.save()
            # Attach the user to the form before saving
            contact = contact_form.save(commit=False)
            contact.user = user
            contact.save()
            return HttpResponseRedirect(reverse('contact_detail',
                                        kwargs={'slug': user.username}))

        return self.render_to_response(self.template_name, {
            'username': user.username,
            'user_form': user_form,
            'contact_form': contact_form,
        })

######

