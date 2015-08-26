#!/usr/bin/env python
# coding=utf-8

# noinspection PyPackageRequirements
import environ

environ.Env().read_env('.env.test')
from .common import *  # NOQA

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default='secret')

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
TEMPLATE_DEBUG = DEBUG

# See: https://docs.djangoproject.com/en/dev/ref/settings/
# #template-context-processors
TEMPLATES[0]['OPTIONS']['context_processors'] = [

    # 'django.template.context_processors.debug',
    'django.template.context_processors.request',
    # 'django.contrib.auth.context_processors.auth',
    # 'django.template.context_processors.i18n',
    # 'django.template.context_processors.media',
    # 'django.template.context_processors.static',
    # 'django.template.context_processors.tz',
    # 'django.contrib.messages.context_processors.messages',

]

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}
# DATABASES['default']['ATOMIC_REQUESTS'] = True
# DATABASES['pg'] = DATABASES['default']
# DATABASES['pg']['TEST_DEPENDENCIES'] = []
# DATABASES['default'] = {
#
#     'ENGINE': 'django.db.backends.sqlite3',
#     'ATOMIC_REQUESTS': True,
#     'TEST_DEPENDENCIES': []
#
# }

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)


# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions',)

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Your local stuff: Below this line define 3rd party library settings

ACCOUNT_EMAIL_VERIFICATION = 'optional'

CRISPY_FAIL_SILENTLY = env.bool('CRISPY_FAIL_SILENTLY', not DEBUG)

MIDDLEWARE_CLASSES = (

    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',

)

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (

    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',

)


# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING['disable_existing_loggers'] = True

# OTHER CONFIGURATION
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)
