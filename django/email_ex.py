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

#8 Using a custom message level

from django.views.generic.edit import FormView
...
from django.conf import settings


class FormClassView(FormView):
    ...
    def post(self, request, *args, **kwargs):
        ...
        if form.is_valid():
            messages.add_message(
                    request,
                    settings.CRITICAL,
                    'This is critical!'
            )
            ...

#9 With extra tags

from django.contrib import messages
from django.views.generic.edit import FormView
from django.conf import settings

...

class FormClassView(FormView):
    ...
    def post(self, request, *args, **kwargs):
        ...
        if form.is_valid():
            messages.success(
                    request,
                    'Your contact form submitted successfully',
                    extra_tags = 'bold'
            )
            ...

#10 silently fails

from django.contrib import messages
from django.views.generic.edit import FormView
from django.conf import settings

...

class FormClassView(FormView):
    ...
    def post(self, request, *args, **kwargs):
        ...
        if form.is_valid():
            messages.success(
                    request,
                    'Your contact form submitted successfully',
                    fail_silently=True
            )
            ...

#11 Displaying messages form-class.html
...
{% block body_content %}
  ...
  <form method="post">
    {% csrf_token %}
    
    {% if messages %}
      <ul class="messages">
        {% for message in messages %}
          <li{% if message.tage %} class="{{message.tags }}"{% endif %}>
          {{ message|safe }}
          </li>
        {% endfor %}
      </ul>
    {% endif %}
    ...

#12 As plain text emails
# forms.py
...
from django.core.mail import EmailMessage
...

class ContactForm(Form):
    ...
    def send_email(self, request):
        data = self.cleaned_data
        msg_body = 'Hello World'
        email = EmailMessage(
                subject = 'New Contact Form Entry',
                body = msg_body,
                from_email = 'no-reply@example.com',
                reply_to = ['no-reply@example.com'],
                cc = []
                bcc = []
                to = [data['email_1']],
                attachments = [],
                headers = {},
        )

        email.content_subtype = 'plain'
        email.send()

# views.py

from django.template.response import TemplateResponse
...

class FormClassView(FormView):
    ...
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        ...
        form.send_email(request)
        return TemplateResponse(
                request,
                self.template_name,
                context
        )

#13 As HTML emails with a plain text alt
...
from django.core.mail import (EmailMessage, EmailMultiAlternatives)
...

class ContactForm(Form):
    ...
    def send_email(self, request):
        data = self.cleaned_data
        msg_body = '<b>Hello World</b>'

        email = EmailMultiAlternatives(
                subject = 'New Contact Form Entry',
                body = msg_body,
                from_email = 'no-reply@example.com',
                reply_to = ['no-reply@example.com'],
                cc = []
                bcc = []
                to = [data['email_1']]
                attachments = [],
                headers = {},
        )
        email.content_subtype = 'html'
        email.attach_alternative(
                'Hello World',
                'text/plain'
        )
        email.send()

#14 With attachment .pdf
# forms.py
...
from django.conf import settings
...

class ContactForm(Form):
    ...
    def send_email(self, request):
        ...
        email.attach_file(settings.STATIC_ROOT + '/chapter_7/pdf/example.pdf')
        email.send()

#15 fail silently
# forms.py
...
class ContactForm(Form):
    ...
    def send_email(self, request):
        ...
        email.send(fail_silently=True)
        

#16 custom email templates
# forms.py
...
from django.template.loader import get_template
...
class ContactForm(Form):
    ...
    def send_email(self, request):
        data = self.cleaned_data
        template = get_template(
                'chapter_7/emails/plain_text_format.html'
        )
        msg_body = template.render()

        email = EmailMessage(
                subject = 'New Contact Form Entry',
                body = msg_body,
                from_email = 'no_reply@example.com',
                reply_to = ['no_reply@example.com'],
                cc = [],
                bcc = [],
                to = [data['email_1']],
                attachments = [],
                headers = {},
        )
        
        email.content_subtype = 'plain'
        email.send(fail_silently = True)

# results: plain text into email

#17 for HTML email
# forms.py
...
from django.template.loader import get_template
...

class ContactForm(Form):
    ...
    def send_email(self, request):
        data = self.cleaned_data
        template = get_template(
                'chapter_7/emails/html_format.html'
        )
        msg_body = template.rener()
        email = EmailMessage(
                subject = 'New Contact Form Entry',
                body = msg_body,
                from_email = 'no_reply@example.com',
                reply_to = ['no_reply@example.com'],
                cc = [],
                bcc = [],
                to = [data['email_1']]
                attachments = [],
                headers = {}
        )

        email.content_subtype = 'html'
        email.send(fail_silently = True)

# html_format.html
<!DOCTYPE html>
<html lang="en" xmlns="http://www.www.w3.org/1000/xhtml">
  <head>
    <meta charset="utf-8" />
    <title>Hello World</title>
    </head>
    <body>
      <b>Hello World</b>
    </body>
  </html>

# results: HTML into email

#18 Provided template context
# forms.py
...
from django.template.loader import get_template
...
class ContactForm(Form):
    ...
    def send_email(self, request):
        data = self.cleaned_data
        template = get_template('chapter_7/emails/new_contact_form_entry.html')
        context = {'data': data}
        msg_body = template.render(context)
        
        email = EmailMessage(
                subject = 'New Contact Form Entry',
                body = msg_body,
                from_email = 'no_reply@example.com',
                reply_to = ['no_reply@example.com'],
                cc = [],
                bcc = [],
                to = [data['email_1']]
                attachments = [],
                headers = {}
        )

        email.content_subtype = 'html'
        email.send(fail_silently = True)

# new_contact_form_entry.html
{% load static %}
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1000/xhtml">
  <head>
    <meta charset="utf-8">
    <title>Contact Form Submitted</title>
  </head>
  <body>
    <center>
      <h1>New Contact Form Entry</h1>
      <h2>The field contents are listed below</h2>
      <ul>
        <li>Full Name: {{ data.full_name }}</li>
        <li>Email Field Example 1: {{ data.email_1 }}</li>
        <li>Email Field Example 2: {{ data.email_2 }}</li>
        <li>Email Field Example 3: {{ data.email_3 }}</li>
        <li>Conditionally Required Field: {{ data.conditional_required }}</li>
        <li>Multiple Emails Field: {{ data.multiple_emails }}</li>
        <li>Message: {{ data.message }}</li>
      </ul>
    </center>
  </body>
</html>

#19 Generating PDF reports

(virtual_env) pip install xhtml2pdf

# forms.py
...
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
...

class ContactForm(Form):
    ...
    def generate_pdf(self, request):
        dest = open(settings.STATIC_ROOT + '/chapter_7/pdf/test.pdf', 'w+b')
        template = get_template('chapter_7/pdfs/pdf_template.html')
        html = templste.render()
        result = pisa.CreatePDF(
                html,
                dest = dest,
        )
        return HttpResponse(result.err)

# views.py
from django.template.response import TemplateResponse
from django.views.generic.edit import FormView
...

class FormClass_View(FormView):
    ...
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        ...
        form.send_email(request)
        form.generate_pdf(request)
        return TemplateResponse(
                request,
                self.template_name,
                context
        )

# pdf_template.html

<!DOCTYPE html>
<html>
  <head></head>
  <body>
    <div id="header_obj"><h1>Header</h1></div>
    <div id="footer_obj">&copy;Footer - Page <pdf:pagenumber> of <pdf:pagecount>
    </div>
    <div class="body-content">
      <h2>Hello World</h2>
      {% lorem 50 p %}<pdf:pdf-next-page />{% lorem 50 p %}
    </div>
  </body>
</html>

# pdf_template.html with CSS formating for pdf
...
  <head>
    <style>
      @page {
              size: a4 portrait;
              @frame header_frame {
                  -pdf-frame-content: header_obj;
                  top: 50pt; left: 50pt;
                  width: 512pt; height: 40pt;
              }
              @frame content_frame {
                  top: 90pt; left: 50pt;
                  width: 512pt; height: 40pt;
              }
              @frame footer_frame {
                  -pdf-frame-content: footer_obj;
                  top: 772pt; left: 50pt;
                  width: 512pt; height: 20pt;
              }
      }
      #header_obj { color: darkblue; text-align: center;}
      .body-content {color:black; text-align: left;}
      #footer_obj {color: green; text-align: right;}
    </style>
  </head>
...

#20 Adding context
# forms.py

from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
...

class ContactForm(Form):
    ...
    def generate_pdf(self, request):
        data = self.cleaned_data
        context = {'data': data}
        dest = open(settings.STATIC_ROOT + '/chapter_7/pdf/test_2.pdf', 'w+b')
        template = get_template('chapter_7/pdfs/pdf_template.html')
        html = template.render(context)
        result = pisa.CreatePDF(
                html,
                dest = dest,
        )
        
        return HttpResponse(result.err)

# pdf_template.html
...
      <div class="body-content">
        <h2>Hello World</h2>
        <h3>The field contents are listed below</h3>
        <ul>
          <li>Full Name: {{ data.full_name }}</li>
          <li>Email Field Example 1: {{ data.email_1 }}</li>
          <li>Email Field Example 2: {{ data.email_2 }}</li>
          <li>Email field Example 3: {{ data.email_3 }}</li>
          <li>Conditionally Required Field: {{ data.conditional_required }}</li>
          <li>Multiple Emails Field: {{ data.multiple_emails }}</li>
          <li>Message: {{ data.message }}</li>
        </ul>
        {% lorem 50 p %}<pdf:pdf-next-page />{% lorem 50 p %}
      </div>
...

