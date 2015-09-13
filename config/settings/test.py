"""
Test Settings

- Debug off
- Disable template processors
- Use faster password hash algorithm.

"""

try:
    import environ

    environ.Env().read_env('.env')
    environ.Env().read_env('.env.test')
finally:
    from .local import *  # NOQA



# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', 'allauth.account.auth_backends.AuthenticationBackend',)

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache', }
}


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES['default']['ATOMIC_REQUESTS'] = False

# MAIL SETTINGS
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = str(ROOT_DIR.path('logs', 'test_emails'))

# MIDDLEWARE
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

)

# SITE SETTINGS
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
SECURE_SSL_REDIRECT = False

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATES[0]['OPTIONS']['context_processors'] = [

    'django.template.context_processors.request', 'django.contrib.auth.context_processors.auth',
    # 'django.template.context_processors.i18n',
    # 'django.template.context_processors.media',
    # 'django.template.context_processors.static',
    # 'django.template.context_processors.tz',
    'django.contrib.messages.context_processors.messages', ]

# TEST RUNNER
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# TESTING PERFORMANCE
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)
