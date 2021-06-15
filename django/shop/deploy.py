"""Deploy Django about."""

# first make settings.py two variables for DEBUG True/False
if DEBUG is True:
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
            Path(BASE_DIR, "/static/")
    ]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = Path(BASE_DIR, 'media')
else:
    STATIC_ROOT = '/var/www/static/'
    STATICFILES_DIRS = [
            Path(BASE_DIR, '/var/www/static/')
    ]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = Path(BASE_DIR, '/var/www/ /media/')

######
