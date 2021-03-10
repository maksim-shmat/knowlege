"""Beginning django web app development."""

# configure and install the Django admin site docs App
pip install docutils

url(r'^admin/doc/', include('django.contrib.admindocs.urls'))
# add before the url(r'^admin/'...)
http://127.0.0.1.8000/admin/doc/

######### send basic email with EmailMessage class
from django.core.mail.message import EmailMessage

# Build message
email = EmailMessage(subject='Coffeehouse specials', body='We would like to let you know about this week/`s specials...', from _email='stores@coffeehouse.com',
        to=['ilovecoffee@hotmail.com', 'officemgr@startups.com'], bcc=['marketing@coffeehouse.com'], cc=['ceo@coffeehouse.com']
        headers = {'Reply-To': 'support@coffeehouse.com'})

# Send message with built-in send() method
email.send()

######## send multiple emails in a single connection with EmailMessage class
from django.core import mail
connection = mail.get_connection()

# Manually open the connection
connection.open()

# Build message
email = EmailMessage(subject='Coffeehouse specials', body='We would like to let you know about this week/`s specials...', from_email='stores@coffeehouse.com',
        to=['ilovecoffee@hotmail.com', 'offecemgr@startups.com'],
        bcc=['marketing@coffeehouse.com'], cc=['ceo@coffeehouse.com']
        headers = {'Reply-To': 'support@coffeehouse.com'})

# Build message
email2 = EmailMessage(subject='Coffeehouse coupons', body='New coupons for our best customers...', from_email='stores@coffeehouse.com',
        to=['officemgr@startups.com', 'food@momandpopshop.com'],
        bcc=['marketing@coffeehouse.com'], cc=['ceo@coffeehouse.com']
        headers = {'Reply-To': 'support@coffeehouse.com'})

# Send the two emails in a single call
connection.send_messages([email, email2])
# The connection was already open so send_messages() doesn't close it.
# We need to manually close the connection.
connection.close()

############ send HTML(w/text) emsil with EmailMiltiAlternatives, a subclass of the EmailMessage class
from django.core.mail import EmailMultiAlternatives

subject, from_email, to = 'Important support message', 'support@coffeehouse.com', 'ceo@coffeehouse.com'
text_content = 'This is an important message.'
html_content ='
This is an important message.
'
msg = EmailMultiAlternatives(subject=subject, body=text_content, from_email=from_email, to=[to])
msg.attach_alternative(html_content, "text/html")
msg.send()

############## send HTML emails with EmailMessage class
subject, from_email, to = 'Important support message', 'support@coffeehouse.com', 'ceo@coffeehouse.com'
html_content = '
This is an important message.
'
msg = EmailMessage(subject=subject, body=html_content, from_email=from_email, to=[to])
msg.content_subtype = "html" # Main content is now text/html
msg.send()

############ send email with PDF attachment with EmailMessage class
from django.core.mail.message import EmailMessage

# Built message
email = EmailMessage(subject='Coffeehouse sales report', body='Attached is sales report...', from_email='stores@coffeehouse.com',
        to=['ceo@coffeehouse.com', 'marketing@coffeehouse.com']
        headers = {'Replay-To': 'sales@coffeehouse.com'})

# Open PDF file
attachment = open('SalesReport.pdf', 'rb')

# Attach PDf file
email.attach('SalesReport.pdf',attachment.read(),'application/pdf')

# Send message with built-in send() method
email.send()

########## Create Django superuser

[user@coffeehouse ~]$ python manage.py createsuperuser
Username (leave blank to use 'admin'):
Email address: admin@coffeehouse.com
Password:
Password (again):
Superuser crated successfully

[user@coffeehouse ~]$ python manage.py createsuperuser --usename=bigboss
                     --email=bigboss@coffeehouse.com
Password:
Password (again):
Superuser created successfully.

[user@coffeehouse ~]$ python manage.py shell
Python 2.7.3 (default, Apr 10 2013, 06:20:15)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_superuser(username='angelinvestor',
        email='angelinvestor@coffeehouse.com',
        password='seedfunding')
>>>

######
