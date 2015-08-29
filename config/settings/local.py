# -*- coding: utf-8 -*-
"""
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
"""
from environ import Env

Env().read_env('.env')

from .common import *  # noqa


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = TEMPLATES[0]['OPTIONS']['debug'] = env.bool('DJANGO_DEBUG',
                                                    default=True)

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY")

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')

ACCOUNT_EMAIL_VERIFICATION = 'optional'

# SERVER
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar',)

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [

        'debug_toolbar.panels.redirects.RedirectsPanel'

    ],
    'SHOW_TEMPLATE_CONTEXT': True
}

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions',)

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------

if not DEBUG:
    STATIC_URL = '/staticfiles/'

STATICFILES_STORAGE = ('whitenoise.django.GzipManifestStaticFilesStorage')


# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/
# #std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (

    str(ROOT_DIR.path('.tmp')),

)

# FORMS CONFIGURATION
# ------------------------------------------------------------------------------
CRISPY_FAIL_SILENTLY = env.bool('CRISPY_FAIL_SILENTLY', False)
