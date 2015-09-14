"""
Utilities for testing.
"""

# Django Packages
from urllib.parse import urljoin
from django.conf import settings
from django.core.urlresolvers import NoReverseMatch, reverse

# Annotation Tool Project
from rest_framework.test import APITestCase
from annotation_tool.users.factories import UserFactory

import logging

logger = logging.getLogger(__name__)


# noinspection PyUnresolvedReferences
class UserTestMixin(object):
    """Override user factory for `test_plus` class."""
    user_factory = UserFactory

    # noinspection PyPep8Naming
    def assertLoginRequired(self, url_name, *args, **kwargs):
        """
        Ensure login is required to GET this URL.

        :param url_name: Named URL to test.
        :param args:
        :param kwargs:
        """
        response = self.get(url_name, *args, **kwargs)
        reversed_url = reverse(url_name, args=args, kwargs=kwargs)
        try:
            login_url = reverse(settings.LOGIN_URL)
        except NoReverseMatch:
            login_url = settings.LOGIN_URL
        expected_url = "{0}?next={1}".format(login_url, reversed_url)
        self.assertRedirects(response, expected_url, status_code=302)

    def response_401(self, response=None):
        """ Given response has status_code 401 """
        response = self._which_response(response)
        self.assertEqual(response.status_code, 302)


class BaseAPITestCase(APITestCase):
    TEST_SERVER = 'http://testserver/'

    def get(self, path, data=None, secure=False, **extra):
        try:
            self.response = self.client.get(path, data=data, secure=secure, **extra)
            self.data = self.response.data
            return self.response
        except AttributeError:
            line = '\n... Path: %s' % path
            if not all((path.startswith('/'), path.endswith('/'))):
                raise ValueError('`path` should start and end with a `/`.%s' % line)
            else:
                raise ValueError('Data not found.  Check `path` is accurate.%s' % line)

    def url(self, suffix=None):
        return urljoin(self.TEST_SERVER, suffix) if suffix else self.TEST_SERVER
