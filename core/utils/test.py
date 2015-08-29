#!/usr/bin/env python
# coding=utf-8
from django.conf import settings
from django.core.urlresolvers import reverse, NoReverseMatch
from test_plus.test import CBVTestCase, TestCase

from annotation_tool.users.factories import UserFactory


# noinspection PyUnresolvedReferences
class BaseTestMixin(object):
    """Override user factory"""
    user_factory = UserFactory

    def assertLoginRequired(self, url_name, *args, **kwargs):
        """ Ensure login is required to GET this URL """
        response = self.get(url_name, *args, **kwargs)
        reversed_url = reverse(url_name, args=args, kwargs=kwargs)
        try:
            login_url = reverse(settings.LOGIN_URL)
        except NoReverseMatch:
            login_url = settings.LOGIN_URL
        expected_url = "{0}?next={1}".format(login_url, reversed_url)
        self.assertRedirects(response, expected_url)


class BaseTestCase(BaseTestMixin, TestCase):
    pass


class BaseCBVTestCase(BaseTestMixin, CBVTestCase):
    pass
