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

########
