"""
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
"""

# Third Party Packages
from environ import Env

Env().read_env('.env')


# Local Application
from .common import *  # noqa


# DEV TOOLS: django-debug-toolbar
# ------------------------------------------------------------------------------
DEV_MIDDLEWARE = ('debug_toolbar.middleware.DebugToolbarMiddleware',)
THIRD_PARTY_APPS += ('debug_toolbar',)

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS':        [

        'debug_toolbar.panels.redirects.RedirectsPanel'

    ],
    'SHOW_TEMPLATE_CONTEXT': True
}

# DEV TOOLS: django-extensions
# ------------------------------------------------------------------------------
THIRD_PARTY_APPS += ('django_extensions',)

# MAIL SETTINGS
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = str(ROOT_DIR.path('logs', 'emails'))


# SERVER
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
SECURE_SSL_REDIRECT = False

CACHEOPS = {
    'lookups.*': ('all', 300)
}


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
LOCAL_APPS += ('core.local', 'core.production')

if not DEBUG:
    STATIC_URL = '/staticfiles/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (str(ROOT_DIR.path('.tmp')),)


# COMBINE INSTALLED APPS
# ------------------------------------------------------------------------------
INSTALLED_APPS = (DJANGO_APPS + ADMIN_APPS + LOCAL_APPS + THIRD_PARTY_APPS)

# COMBINE MIDDLEWARE_CLASSES
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (MIDDLEWARE_CLASSES + DEV_MIDDLEWARE)
