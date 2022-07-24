"""Paste chunk of code."""

# models.py

import datetime
from django.db import models
from django.db.models import permalink
from django.contrib import admin

class Paste(models.Model):
    """Structure one paste on app Pastebin."""

    SYNTAX_CHOICES = (
            (0, "Plan"),
            (1, "Python"),
            (2, "HTML"),
            (3, "SQL"),
            (4, "Javascript"),
            (5, "CSS"),
    )

    content = models.TextField()
    title = models.CharField(blank=True, max_length=30)
    syntax = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ('-timestamp',)

    def __unicode__(self):
        return "%s (%s)" % (self.title or "#%s" % self.id,
                self.get_syntax_display())
    @permalink
    def get_absolute_url(self):
        return ('django.views.generic.list_detail.object_detail',
                None, {'object_id': self.id})


class PasteAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title', 'poster', 'syntax', 'timestamp')
    list_filter = ('timestamp', 'syntax')

admin.site.register(Paste, PasteAdmin)

# URL's
from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object
from pastebin.models import Paste

display_info = {'queryset': Paste.objects.all()}
create_info = {'model': Paste}

urlpatterns = patterns('',
        url(r'^$', object_list, dict(display_info, allow_empty=True)),
        url(r'^(?P<object_id>\d+)/$', object_detail, display_info),
        url(r'^add/$', create_object, create_info),
)

#
