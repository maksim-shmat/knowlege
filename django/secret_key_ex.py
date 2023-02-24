"""Seret key about."""

#1

import os
SECRET_KEY = os.environ['SECRET_KEY']

#1.1

import os
SECTET_KEY = os.environ.get('DJANGO_SECRET_KEY',
        'cg#p$g+j9tax!#a3cup@1$8abt2__^k3q_pmi)5%asj6yupkag')

#2 from file

with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

#3 Warn!

DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))
DJANGO_DEBUG = ''  # it False

#4 pythohn manage.py check -deploy

check deploy settings
