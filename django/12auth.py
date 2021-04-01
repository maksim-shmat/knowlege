""" Second fele contains example about authentication and etc."""

###### PermissionDenied

from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class PermissionRedirectMiddleware(object):
    def __init__(self, view='request_permission', args=None, kwargs=None):
        self.view = view
        self.args = args or ()
        self.kwargs = kwargs or {}

    def process_view(self, request, view, args, kwargs):
        try:
            response = view(request, *args, **kwargs)
        except PermissionDenied:
            url = reverse(self.view, args=self.args, kwargs=self.kwargs)
            return HttpResponseRedirect(url)

######
