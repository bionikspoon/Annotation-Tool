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




# DEBUG
# ------------------------------------------------------------------------------
DEBUG = TEMPLATES[0]['OPTIONS']['debug'] = env.bool('DJANGO_DEBUG', default=True)

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY")

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')

ACCOUNT_EMAIL_VERIFICATION = 'optional'

# SERVER
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# SESSION
# ------------------------------------------------------------------------------
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# CACHING
# ------------------------------------------------------------------------------

UPDATE_CACHE_MIDDLEWARE = ('django.middleware.cache.UpdateCacheMiddleware',)

FETCH_CACHE_MIDDLEWARE = ('django.middleware.cache.FetchFromCacheMiddleware',)

# django-debug-toolbar
# ------------------------------------------------------------------------------
DEV_MIDDLEWARE = ('debug_toolbar.middleware.DebugToolbarMiddleware',)
THIRD_PARTY_APPS += ('debug_toolbar',)

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [

        'debug_toolbar.panels.redirects.RedirectsPanel'

    ],
    'SHOW_TEMPLATE_CONTEXT': True
}

# django-extensions
# ------------------------------------------------------------------------------
THIRD_PARTY_APPS += ('django_extensions',)

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
LOCAL_APPS += ('core.local', 'core.production')

if not DEBUG:
    STATIC_URL = '/staticfiles/'

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (

    str(ROOT_DIR.path('.tmp')),

)

# FORMS CONFIGURATION
# ------------------------------------------------------------------------------
CRISPY_FAIL_SILENTLY = env.bool('CRISPY_FAIL_SILENTLY', False)


# SILK CONFIGURATION
# ------------------------------------------------------------------------------
# THIRD_PARTY_APPS += ('silk',)
# DEV_MIDDLEWARE += ('silk.middleware.SilkyMiddleware',)


# COMBINE INSTALLED APPS
# ------------------------------------------------------------------------------
INSTALLED_APPS = DJANGO_APPS + ADMIN_APPS + LOCAL_APPS + THIRD_PARTY_APPS

# COMBINE MIDDLEWARE_CLASSES
# ------------------------------------------------------------------------------
# Make sure djangosecure.middleware.SecurityMiddleware is listed first
MIDDLEWARE_CLASSES = (

    # UPDATE_CACHE_MIDDLEWARE +

    MIDDLEWARE_CLASSES + DEV_MIDDLEWARE


    # + FETCH_CACHE_MIDDLEWARE

)
