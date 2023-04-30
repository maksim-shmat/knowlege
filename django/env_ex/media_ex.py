"""How work with your media."""

#1 change media in settings.py just below STATIC_ROOT

...
MEDIA_URL = '/media/'
MEDIA_ROOT = posixpath.join(
        *(BASE_DIR.split(os.path.sep) ['media'])
)
