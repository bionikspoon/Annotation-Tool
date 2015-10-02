"""
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
"""

from annotation_tool.core.utils.env import Env

try:
    Env().read_env('.env.local')
finally:
    from .common import *  # noqa


# CACHE CONFIGURATION
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
    }
}
CACHEOPS = {}
# CACHEOPS = {
#     'lookups.*': {
#         'ops': 'all',
#         'timeout': 300
#     },
#     'pubmed': {
#         'ops': 'all',
#         'timeout': 300
#
#     },
#     'users': {
#         'ops': 'all',
#         'timeout': 300
#     }
# }

# DEV TOOLS: django-debug-toolbar
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
DEBUG_TOOLBAR_PANELS = ['debug_toolbar.panels.sql.SQLPanel',
                        'debug_toolbar.panels.cache.CachePanel',
                        'debug_toolbar.panels.timer.TimerPanel',
                        'debug_toolbar.panels.headers.HeadersPanel',
                        'debug_toolbar.panels.request.RequestPanel',
                        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
                        'debug_toolbar.panels.templates.TemplatesPanel',
                        'debug_toolbar.panels.signals.SignalsPanel',
                        'debug_toolbar.panels.logging.LoggingPanel',
                        'debug_toolbar.panels.settings.SettingsPanel',
                        'debug_toolbar.panels.versions.VersionsPanel',
                        'debug_toolbar.panels.redirects.RedirectsPanel', ]

# DEV TOOLS: django-extensions
# ------------------------------------------------------------------------------
THIRD_PARTY_APPS += ('django_extensions',)

# MAIL SETTINGS
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = ROOT_DIR('logs', 'emails')

# SERVER
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = ['localhost:8000', '127.0.0.1:8000']
SECURE_SSL_REDIRECT = False


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# STATICFILES_DIRS = [APPS_DIR('static'), ROOT_DIR('dist')]
# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
TEMPLATES[0]['OPTIONS']['context_processors'].insert(0, 'django.template.context_processors.debug')
# COMBINE INSTALLED APPS
# ------------------------------------------------------------------------------
INSTALLED_APPS = (DJANGO_APPS + ADMIN_APPS + LOCAL_APPS + THIRD_PARTY_APPS)

# COMBINE MIDDLEWARE_CLASSES
# ------------------------------------------------------------------------------
# MIDDLEWARE_CLASSES = (DEV_MIDDLEWARE + UPDATE_CACHE_MIDDLEWARE + MIDDLEWARE_CLASSES +
#     FETCH_CACHE_MIDDLEWARE)
MIDDLEWARE_CLASSES = (DEV_MIDDLEWARE + MIDDLEWARE_CLASSES)
