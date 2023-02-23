"""Seret key about."""

#1

import os
SECRET_KEY = os.environ['SECRET_KEY']


#2 from file

with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
