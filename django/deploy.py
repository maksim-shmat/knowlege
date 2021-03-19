""" About deploying."""

###### sign up Heroku account

$ brew install heroku (for Mac)

$ heroku login

- update Pipfile.lock
- make a new Procfile file
- install gunicorn as our web server
- make a one-line change to settings.py file

# Pipfile
[requires]
python_version = "3.6"
======
$ pipenv lock

======
$ touch Procfile
# add in
web: gunicorn pages_project.wsgi --log-file -

======
$ pipenv install gunicorn==19.9.0

======
# change to settings.py
ALLOWED_HOST = ['*']
# '*' - all domain are acceptable. In prod change it.

####### Deploy

- create a new app on Heroku and push our code to it
- add a git remote "hook" for Heroku
- configure the app to igonre static files, which we`ll cover in later
- start the Heroku server so the app is live
- visit the app on Heroku`s provided URL

###### creating a new Heroku app
$ heroku create

====== # make ignore static files
$ heroku config:set DISABLE_COLLECTSTATIC=1

====== # push our code to Heroku
$ git push heroku master

====== # make app live to be free
$ heroku ps:scale web=1

====== # We're done!
$ heroku open

###### third time deploying an app
- update Pipfile.lock
- new Procfile
- install gunicorn
- update settings.py

### Pipfile
[requires]
python_version = "3.6"

$ pipenv lock

$ touch Procfile

web: gunicorn blog_project.wsgi --log-file -  # into a file Procfile

### install gunicorn
$ pipenv install gunicorn==19.9.0

### blog_project/settings.py
ALLOWED_HOSTS = ['*']

### logged in to Heroku account
$ heroku login
$ heroku create dfb-blog  # it's name
$ heroku git:remote -a dfb-blog
$ pipenv install whitenoise  # for support static files

### settings.py
INSTALLED_APPS = [
        'blog.apps.BlogConfig',
        'accounts.apps.AccountsConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'whitenoise.runserver_nostatic', # new
        'django.contrib.staticfiles',
    ]

MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware', # new
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

...

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # new!
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

### commit your new changes
$ git add -A
$ git commit -m 'Heroku config'
$ git push origin master

$ git push heroku master
$ heroku ps:scale web=1

https://dfd-blog.herokuapp.com/

######
