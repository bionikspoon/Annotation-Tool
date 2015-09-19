"""
Django settings for annotation_tool project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Compatibility
from __future__ import absolute_import, unicode_literals

# Third Party Packages
import environ

ROOT_DIR = environ.Path(__file__) - 3  # /annotation_tool/
APPS_DIR = ROOT_DIR.path('annotation_tool')

env = environ.Env()


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG')
# ==============================================================================


# ACCOUNT CONFIGURATION
# ------------------------------------------------------------------------------
# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'


# ADMIN CONFIGURATION
# ------------------------------------------------------------------------------
GRAPPELLI_ADMIN_TITLE = 'Annotation Tool'

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (  # :off

    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

    # 'django.contrib.postgres',
    # Useful template tags:
    # 'django.contrib.humanize',

)  # :on

ADMIN_APPS = (  # :off

    'django.contrib.admindocs',
    'grappelli',
    'django.contrib.admin',

)  # :on

THIRD_PARTY_APPS = (  # :off

    'crispy_forms',  # Form layouts
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
    'rest_framework',
    'compressor'

)  # :on

# Apps specific for this project go here.
LOCAL_APPS = (

    'core',  # templates and static
    'annotation_tool.users',  # custom users app
    'pubmed',

    'pubmed.lookups',

)

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', 'allauth.account.auth_backends.AuthenticationBackend'

)

# CACHE CONFIGURATION
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "{0}/{1}".format(env.str('REDIS_URL'), 0),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True
        },
        'TIMEOUT': 300
    }
}

UPDATE_CACHE_MIDDLEWARE = ('django.middleware.cache.UpdateCacheMiddleware',)
FETCH_CACHE_MIDDLEWARE = ('django.middleware.cache.FetchFromCacheMiddleware',)

DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True

# THIRD_PARTY_APPS += ('cacheops',)
CACHEOPS_REDIS = {key.lower(): value for key, value in env.db('REDIS_URL').items() if value}
CACHEOPS_REDIS['db'] = 1

# CACHEOPS = {
#     'lookups.*': ('all', 300)
# }

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db("DATABASE_URL")
}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------

PROJECT_NAME = 'Annotation Tool'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'


# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(name)s %(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
        'human': {
            'format': '%(levelname)s %(name)s Line %(lineno)d '
                      '%(asctime)s\n'
                      '%(message)s\n'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
        'not_django': {
            '()': 'core.utils.log.NotDjangoFilter'
        },
        'not_production': {
            '()': 'core.utils.log.NotProductionFilter'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'django': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': str(ROOT_DIR.path('logs', 'django.log')),
            'filters': ['require_debug_true'],
            'backupCount': 10,
            'when': 'MIDNIGHT',
            'formatter': 'verbose'
        },
        'pubmed': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': str(ROOT_DIR.path('logs', 'pubmed.log')),
            'backupCount': 10,
            'when': 'm',
            'interval': 10,
            'formatter': 'human'
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': str(ROOT_DIR.path('logs', 'debug.log')),
            'filters': ['require_debug_true'],
            'backupCount': 10,
            'when': 'm',
            'interval': 10,
            'formatter': 'human'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'django': {
            'handlers': ['django'],
            'level': 'DEBUG',
            'propagate': True
        },
        'pubmed': {
            'handlers': ['pubmed'],
            'level': 'DEBUG',
            'propagate': True,
            'filter': ['not_production']
        },
        '': {
            'handlers': ['debug'],
            'level': 'DEBUG',
            'propagate': True,
            'filter': ['not_django']
        }
    }
}


# Form Configuration
# ------------------------------------------------------------------------------

CRISPY_FAIL_SILENTLY = env.bool('CRISPY_FAIL_SILENTLY', not DEBUG)
# See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'flat_form'
CRISPY_ALLOWED_TEMPLATE_PACKS = ('flat_form',)
CRISPY_CLASS_CONVERTERS = {
    'textinput': 'form-control',
    'numberinput': 'form-control',
    'textarea': 'form-control'
}
# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (("""Manu Phatak""", 'bionikspoon@gmail.com'),)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
# Make sure djangosecure.middleware.SecurityMiddleware is listed first
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'

)

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': 'annotation_tool.contrib.sites.migrations',
    'flatpages': 'annotation_tool.contrib.flatpages.migrations'
}

# SECRET KEY
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANGO_SECRET_KEY not in os.environ
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY
# ------------------------------------------------------------------------------
# This ensures that Django will be able to detect a secure connectionproperly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_FRAME_DENY = env.bool("DJANGO_SECURE_FRAME_DENY", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
SECURE_BROWSER_XSS_FILTER = True

# SESSION
# ------------------------------------------------------------------------------
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_CACHE_ALIAS = "default"

SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
COMPRESS_ROOT = STATIC_ROOT = str(ROOT_DIR('staticfiles'))
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
COMPRESS_URL = STATIC_URL = '/static/'
# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = []
# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.FileSystemFinder',
                       'django.contrib.staticfiles.finders.AppDirectoriesFinder',
                       'compressor.finders.CompressorFinder')
COMPRESS_ENABLED = env.bool('DJANGO_COMPRESS_ENABLED', not DEBUG)
COMPRESS_OFFLINE = True
# COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
#                         'compressor.filters.yuglify.YUglifyCSSFilter']
# COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter', 'compressor.filters.yuglify.YUglifyJSFilter']
COMPRESS_YUGLIFY_BINARY = ROOT_DIR.path('node_modules', '.bin', 'yuglify')

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [{
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    'DIRS': [str(APPS_DIR.path('templates'))],
    'OPTIONS': {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
        'debug': DEBUG,

        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
        # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
        'loaders': [

            'django.template.loaders.filesystem.Loader',

            'django.template.loaders.app_directories.Loader'],

        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
        'context_processors': [

            'django.template.context_processors.request',

            'django.contrib.auth.context_processors.auth',

            'django.template.context_processors.i18n',

            'django.template.context_processors.tz',

            'django.contrib.messages.context_processors.messages'

        ]
    }
}]


# REST FRAMEWORK
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}


# Combine Apps
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + ADMIN_APPS + LOCAL_APPS + THIRD_PARTY_APPS
