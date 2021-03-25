""" Signals about."""

###### class_prepared

from django.db import models

def listener(sender, **kwargs):
    print('%s.%s' % (sender._meta.app_label, sender._meta.object_name))

models.signals.class_prepared.connect(listener)
class Article(models.Model):
    title = models.CharField(max_length=255)
    class Meta:
        app_label = 'news'

#news.Article

###### pre_init and  post_init

from django.db.models.signals import pre_init
from news.models import Article

def print_args(sender, args, kwargs, **signal_kwargs):
    print('%s(*%s, **%s)' % (sender._meta.object_name, args, kwargs))

pre_init.connect(print_args, sender=Article)
article = Article(title=u'Testing')
# Article(*(), **{'title': u'Testing'})

###
from django.db.models.signals import post_init
from news.models import Article

def print_args(sender, args, kwargs, **signal_kwargs):
    print('Instantiated %r' % instance)

post_init.connect(sender=Article)
article = Article(title=u'Testing')
# Instanitated <Article: Testing>

###### pre_save and post_save

from django.db.models import signals
from news.models import Article

def before(instance, **kwargs):
    print('About to save %s' % instance)

signals.post_save.connect(after, sender=Article)
Article.objects.create(title='New article!')
# About to save New article!
# New Article! was just created<Article: New article!>

###### post_syncdb

from django.db.models import signals

def app_report(app, created_models, verbosity, **kwargs):
    app_label = app.__name__.split('.')[-2]

    if verbosity == 0:
        # Don't do anything, because the user doesn't want to see this.
        return

    # Get a list of models created fo just the current application
    app_models = [m for m in created_models if m._meta.app_label == app_label]

    if app_models:
        # Print a simple status message
        print('Created %s model%s fo %s.' % (len(app_models),
                                             len(app_models) > 1 and 's' or '', app_label))

        if verbosity == 2:
            # Print more detail about the models that were installed
            for model in app models:
                print(' %s.%s -> %s' % (app_label,
                                        model._meta.object_name,
                                        model._meta.db_table))
    elif verbosity == 2:
        print('%s had no models created.' % app_label)

signals.post_syncdb.connect(app_report)

###### Storing Raw Data

from django.db import models

class PickleField(midels.TextField):

    def get_attname(self):
        return '%s_pickled' % self.name

### pickling and unpickling data
try:
    import cPickle as pickle
except ImportError:
    import pickle

###
class PickleField(models.TextField):
    def pickle(self, obj):
        return pickle.dumps(obj)

    def unpickle(self, data):
        return pickle.loads(str(data))

    def get_attname(self):
        return '%s_pickled' % self.name

    def get_db_prep_lookup(self, lookup_type, value):
        raise ValueError("Can't make comparisons against pickled data.")

######
