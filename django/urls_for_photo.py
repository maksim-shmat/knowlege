"""In need photo app."""

from django.conf.urls.defaults import *
from gallery.items.models import Item, Photo

urlpatterns = patterns('django.views.generic',
        url(r'^$', 'simple.direct_to_template',
            kwargs={
                'template': 'index.html',
                'extra_context': {'item_list': lambda: Item.objects.all()}
            },
            name='index'
        ),
        url(r'^items/$', 'list_detail.object_list',
            kwargs={
                'queryset': Item.objects.all(),
                'template_name': 'items_list.html',
                'allow_empty': True
            },
            name='item_list'
        ),
        url(r'^items/(?P<object_id>\d+)/$', 'list_detail.object_detail',
            kwargs={
                'queryset': Item.objects.all(),
                'template_name': 'items_detail.html'
            },
            name='item_detail'
        ),
        url(r'^photos/(?P<object_id>\d+)/$', 'list_detail.object_detail',
            kwargs={
                'queryset': Photo.objects.all(),
                'template_name': 'photo_detail.html'
            },
            name='photo_detail'
        ),
)

#2 examples with +=

from dnango.conf.urls.static import static
from django.conf import settings


urlpatterns = [
        ...
]

urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
