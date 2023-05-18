"""Email sending about."""

#1 into .env

EMAIL_HOST = 'smtp.mailtrap.io'  # e.g.
EMAIL_HOST_USER = 'chupacabra'
EMAIL_HOST_PASSWORD = 'chupacabra'
EMAIL_PORT = '2525'

#2 settings.py
...
if DEBUG:
    EMAIL_HOST = os.getevn('EMAIL_HOST')
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = os.getenv('EMAIL_PORT')
else:
    # Production Email Connecting Settings
    Pass

#3 settings.py

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

#4 settings.py
...
from django.conrib.messages import constants as messages
...
if DEBUG:
    MESSAGE_LEVEL = messages.DEBUG
else:
    pass

#5 settings.py

from django.contrib.messages import constant as messages
...
MESSAGE_TAGS = {
        messages.INFO: 'information',
}

#6 custom message levels

MINOR = 50
MAJOR = 60
CRITICAL = 70

MESSAGE_TAGS = {
        messages.INFO: 'information',
        MINOR: 'minor',
        MAJOR: 'major',
        CRITICAL: 'critical',
}

#7 Creating a message
# views.py
...
from django.contrib import messages
from django.template.response import TemplateResponse
from django.views.generic.edit import FormView


class FormClassView(FormView):
    ...
    def post(self, request, *args, **kwargs):
        ...
        if form.is_valid():
            messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Your contact form submitted successfully'
            )
            context = {
                    'title': 'FormClassView Page',
                    'page_id': 'form-class-id',
                    'page_class': 'form-class-page',
                    'h1_tag': 'This is the FormClassView Page Using ContactForm',
                    'form': form,
            }
        else:
            messages.add_message(
                    request,
                    messages.ERROR,
                    'There was a problem submitting your contact form.<br />Please review the highlighted fields below.'
            )
            context = {
                    'title': 'FormClassView Page - Please
                    Correct The Errors Below',
                    'page_id': 'form-class-id',
                    'page_class': 'form-class-page errors-found',
                    'h1_tag': 'This is the FormClassView Page Using ContactForm<br /><small class="error-msg">Errors Found</small>',
                    'form': form,
            }
            return TemplateResponse(
                    request,
                    self.template_name,
                    context
            )
            ...

#7.1 analog
...
class FormClassView(FormView):
    ...
    def post(self, request, *args, **kwargs):
        ...
        if form.is_valid():
            messages.success(
                    request,
                    'Your contact form submitted successfuly'
            )
            ...
        else:
            messages.error(
                    request,
                    'There was a problem submitting your contact form.<br />Please review the highlighted fields below.'
            )
    ...

#8
