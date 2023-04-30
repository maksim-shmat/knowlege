"""Work with whitenoise about."""

#1 Add to the MIDDLEWARE settings

...
MIDDLEWARE = [
        ...,
        'whitenoise.middleware.WhiteNoiseMiddleware',
]

#2 add variable called STATICFILES_STORAGE to the settings.py, just above
# STATIC_URL and STATIC_ROOT

...
STATICFILES_STORAGE = 'whitenoise.storage.
CompressedManifestStaticFilesStorage'
STATIC_URL = '/staticfiles/'
STATIC_ROOT = posixpath.join(
        *(BASE_DIR.split(os.path.set) + ['staticfiles'])
)

#3 Change the value of your STATIC_URL and STATIC_ROOT variables to equal
# what is shown in the preceding code, if your value has not alredy changed.
