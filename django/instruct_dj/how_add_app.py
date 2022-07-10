""" Insturction how add package with one app django to another django site."""

1. First, create a parent directory for polls, outside of your Django project.
Call this dierctory django-polls.

2. Move the polls directory into the django-polls directory.

3.Create a file django-polls/README.rst with the following contents:
# django-polls/README.rst
====
Polls
====

Polls is a Django app to conduct Web-based polls. For each question, 
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1) Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
            ...
            'polls',
    ]

2) Include the polls URLconf in your project urls.py like this::
    path('polls/', include('polls.urls')),

3) Run ``python manage.py migrate`` to create the polls models.

4) Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you`ll need the Admin app enabled).

5) Visit http://127.0.0.1:8000/polls/ to participate in the poll.

4. Create a django-polls/LICENSE file. Choosing a license is beyond the scope of this tutorial, but suffice it to say that code released publicly without a 
license is useless. Django and many Django-compatible apps are distributed
under the BSD license; however, you`re free to pick your own license. Just be 
aware that your licensing choice will affect who is able use your code.

5. Next we`ll create setup.sfg and setup.py files which detail how to build
and install the app. A full explanation of these files is beyond the scope of
this tutorial, but the setuptools documentation has a good explanation.
Create the files django-polls/setup.cfg and django-polls/setup.py with the 
following contents:
    django-polls/setup.cfg
[metadata]
name = django-polls
version = 0.1
description = A Django app to conduct Web-based polls.
long_description = file: README.rst
url = https://www.example.com/
author = Your Name
author_email = yourname@example.com
license = BSD-3-Clause  # Example license
classifiers = 
    Environment :: Web Environment
    Framework :: Django
    Framework :: Django :: X.Y # Replace "X.Y" as appropriate
    Intended Audience :: Developers
    License :: OSI Approved :: BSD License
    Operating System :: OS Independent
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Topic :: Internet :: WWW/HTTP
    Topic :: Internet :: WWW/HTTP :: Dynamic Content

[option]
include_package_data = true
packages = find:

# django-polls/setup.py
from setuptools import setup
setup()

6. Only Python modules and packages are included in the package by default. To
include additional files, we`ll need to create a MANIFEST.in file. The
setuptools docs referred in the previous step discuss this file in more details.
To include the templates, the README.rst and our LICENSE file, create a file
django-polls/MANIFEST.in with the following contents:
# django-polls/MANIFEST.in
include LICENSE
include README.rst
recursive-include polls/static *
recursive-include polls/templates *

7. It`s optional, but recommended, to include detailed documentation with your
app. Create an empty directory django-polls/docs for future documentation.
Add an additional line to django-polls/MANIFEST.in:
    recursive-include docs *
Note that the docs directory won`t be included in your package unless you add
some files to it. Many Django apps also provide their documentation online 
through sites like readthedocs.org

8. Try building your package with python setup.py sdist(run from inside
django-polls). This creates a directory called dist and builds your new package, django-polls-0.1.tar.gz.

For more information on packaging, see Python`s Tutorial on Packaging and 
Distributing Projects.
