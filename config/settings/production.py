"""
Production Configurations

- Use djangosecure
- Use Amazon's S3 for storing static files and uploaded media
- Use mailgun to send emails
- Use Redis on Heroku

"""

# Compatibility
from __future__ import absolute_import, unicode_literals

# Django Packages
from django.utils import six

# Third Party Packages
# noinspection PyUnresolvedReferences
import boto.s3.connection

# Local Application
from .common import *  # noqa

# AWS CONFIGURATION
# ------------------------------------------------------------------------------
# See: http://django-storages.readthedocs.org/en/latest/index.html
# noinspection PyUnresolvedReferences
THIRD_PARTY_APPS += ('storages',)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET_NAME')
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False

AWS_S3_CALLING_FORMAT = boto.s3.connection.OrdinaryCallingFormat()

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIRY = 60 * 60 * 24 * 7

# See: https://github.com/jschneier/django-storages/issues/47
# Revert the following and use str after the above-mentioned bug is fixed in either django-storage-redux or
#  boto
AWS_HEADERS = {
    'Cache-Control': six.b('max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIRY, AWS_EXPIRY))
}

# CACHING
# ------------------------------------------------------------------------------

CACHEOPS = {
    'lookups.*': {
        'ops':     'get',
        'timeout': 300
    }
}
# Add UPDATE_CACHE_MIDDLEWARE and FETCH_CACHE_MIDDLEWARE to middleware!
# TODO, don't forget this.

# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default='annotation_tool <noreply@annotation-tool.herkokapp.com>')
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = env('DJANGO_MAILGUN_API_KEY')
MAILGUN_SERVER_NAME = env('DJANGO_MAILGUN_SERVER_NAME')
EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default='[annotation_tool] ')
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

# MEDIA
# ------------------------------------------------------------------------------
# URL that handles the media served from MEDIA_ROOT, used for managing stored files.
MEDIA_URL = 'https://s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME

# SECURITY
# ------------------------------------------------------------------------------
INSTALLED_APPS += ("djangosecure",)

SECURITY_MIDDLEWARE = ('djangosecure.middleware.SecurityMiddleware',)
# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)


# SERVER SETTINGS
# ------------------------------------------------------------------------------
# noinspection PyUnresolvedReferences
THIRD_PARTY_APPS += ("gunicorn",)

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [env.str('DJANGO_ALLOW_HOSTS', default='annotation-tool.herokuapp.com')]


# STATIC
# ------------------------
LOCAL_APPS += ('core.production',)

COMPRESS_STORAGE = STATICFILES_STORAGE = 'core.utils.compressor.CachedS3BotoStorage'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
COMPRESS_URL = STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [(

    'django.template.loaders.cached.Loader',
    ['django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader']

)]

# COMBINE INSTALLED APPS
# ------------------------------------------------------------------------------
INSTALLED_APPS = (DJANGO_APPS + ADMIN_APPS + LOCAL_APPS + THIRD_PARTY_APPS)

# COMBINE MIDDLEWARE
# ------------------------------------------------------------------------------
# Make sure djangosecure.middleware.SecurityMiddleware is listed first
MIDDLEWARE_CLASSES = (
SECURITY_MIDDLEWARE + UPDATE_CACHE_MIDDLEWARE + MIDDLEWARE_CLASSES + FETCH_CACHE_MIDDLEWARE)
