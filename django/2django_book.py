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

############
