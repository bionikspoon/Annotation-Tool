"""
Utilities for testing.
"""

from django.conf import settings
from django.core.urlresolvers import reverse, NoReverseMatch

from annotation_tool.users.factories import UserFactory


# noinspection PyUnresolvedReferences
class BaseTestMixin(object):
    """Override user factory"""
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

    # def response_304(self, response=None):
    #     """ Given response has status_code 304 """
    #     response = self._which_response(response)
    #     self.assertEqual(response.status_code, 304)

    def response_401(self, response=None):
        """ Given response has status_code 403 """
        response = self._which_response(response)
        self.assertEqual(response.status_code, 302)
