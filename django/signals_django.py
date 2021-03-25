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

######
