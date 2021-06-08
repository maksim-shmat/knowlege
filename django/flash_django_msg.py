"""Techniques to add Django flash messages."""

from django.contrib import messages

# Generic add_message method
messages.add_message(request, messages.DEBUG, 'The following SQL statements were executed:
        %s' % sqlqueries) # Debug messages ignored by default
messages.add_message(request, messages.INFO, 'All items on this page have freeshipping.')
messages.add_message(request, messages.SUCCESS, 'Email sent successfully.')
messages.add_message(request, messages.WARNING, 'You will need to change your password in one week.')
messages.add_message(request, messages.ERROR, 'We could not process your request at this time.')

# Shortcut level methods
messages.debug(request, 'The following SQL statements were executed: %s' % sqlqueries) # Debug messages ignored by default
messages.info(request, 'All items on this page have free shipping.')
messages.success(request, 'Email sent successfully.')
messages.warning(request, 'You will need to change your password in one week.')
messages.error(request, 'We could not process your request at this time.')

###### Set default Django message level globally in settings.py
# Reduce threshold to DEBUG level in settings.py
from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG

# Increase threshold to WARNING level in settings.py
from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.WARNING

### Set default Django message level on a per request basis
# Reduce threshold to DEBUG level rer request
from django.contrib import messages
messages.set_level(request, messages.DEBUG)

# Increase threshold to WARNING level per request
from djano.contrib import messages
messages.set_level(request, messages.WARNING)

###### Use of the fail_silently=True attribute to ignore errors in case Djangomessags framework not installed.
from django.contrib import messages

# Generic add_message method, with fail_silently=True
messages.add_message(request, messages.INFO, 'All items on this page have freeshipping.', fail_lilently=True)

# Shortcut level method, with fail_silently=True
messages.info(request, 'All items on this page have free shipping.', fail_silently=True)

###### Boilerplate code to use in Django template to display Django flash messages
{% if messages %}
<ul class="messages">
  {% for msg in messages %}
  <li>
    <div class="alert alert-{{msg.level_tag}}" role="alert">
    {{msg.message}}
    </div>
  </li>
  {% endfor %}
</ul>
{% endif %}

######

