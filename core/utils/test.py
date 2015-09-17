"""
Utilities for testing.
"""

# Django Packages
from functools import wraps
from urllib.parse import urljoin
from django.conf import settings
from django.core.urlresolvers import NoReverseMatch, reverse

# Annotation Tool Project
from django.test.client import MULTIPART_CONTENT
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


def implode_request(func):
    """
    Decorator.  Convenience to automate `client` request calls.

    * Sanitize input. Use class variable `path` and `pk` if available.
    * Save `response` and `data` to `self`.
    * Detailed error response for common issue: trailing slashes.

    :param func:
    :return: Client Response object.
    """

    @wraps(func)
    def wrapper(self, path=None, pk=0, *, data=None, **kwargs):
        """
        Call and return client response object.

        :param path: API endpoint or class `self.PATH`
        :param data: Payload.
        :param pk: PK for item urls.
        :param args:
        :param kwargs:
        :return: Client response object.
        """
        path = path if path else self.PATH
        if '%s' in path:
            path %= pk
        try:
            self.response = func(self, path, data, **kwargs)
            self.data = self.response.data
            return self.response
        except AttributeError:
            line = '\n... Path: %s' % path
            if not all((path.startswith('/'), path.endswith('/'))):
                raise ValueError('`path` should start and end with a `/`.%s' % line)
            else:
                raise ValueError('Data not found.  Check `path` is accurate.%s' % line)

    return wrapper


class BaseAPITestCase(APITestCase):
    TEST_SERVER = 'http://testserver/'
    PATH = NotImplemented
    response = NotImplemented
    data = NotImplemented

    @implode_request
    def get(self, *args, **kwargs):
        return self.client.get(*args, **kwargs)

    @implode_request
    def post(self, *args, **kwargs):
        return self.client.post(*args, **kwargs)

    @implode_request
    def put(self, *args, **kwargs):
        return self.client.put(*args, **kwargs)

    @implode_request
    def patch(self, *args, **kwargs):
        return self.client.patch(*args, **kwargs)

    @implode_request
    def delete(self, *args, **kwargs):
        return self.client.delete(*args, **kwargs)

    @implode_request
    def options(self, *args, **kwargs):
        return self.client.options(*args, **kwargs)

    @implode_request
    def request(self, *args, **kwargs):
        return self.client.request(*args, **kwargs)

    def assert_404(self):
        self.assertEqual(self.response.status_code, 404)
        self.assertEqual(self.data['detail'], 'Not found.')

    def assert_405(self):
        self.assertEqual(self.response.status_code, 405)

    def url(self, suffix=None):
        return urljoin(self.TEST_SERVER, suffix) if suffix else self.TEST_SERVER
