"""Notes Heroku about."""

# Deployment to Heroku

Enter project root and run the following commands:

```
$ heroku create superbook-demo
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku config:set DJANGO_SETTINGS_MODULE=superbook.settings.production
$ git push heroku master

