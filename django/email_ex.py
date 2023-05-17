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

#7
