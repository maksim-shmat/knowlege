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

