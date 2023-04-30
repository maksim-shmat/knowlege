"""Static about."""

#1 Activate static files in your local env in your main urls.py

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [...] + static(
        settings.STATIC_URL,
        document_root = settings.STATIC_ROOT
        ) + static(settings.MEDIA_URL,
                document_root = settings.MEDIA_ROOT
        )

#2 alternating

urlpatterns = [...]

if settings.DEBUG:
    urlpatterns += static(
            settings.STATIC_URL,
            document_root = settings.STATIC_ROOT
        )

#3 
