#!/usr/bin/env python
# coding=utf-8
import test_plus.test
from annotation_tool.users.factories import UserFactory


class BaseTestMixin(object):
    """Override user factory"""
    user_factory = UserFactory


class BaseTestCase(BaseTestMixin, test_plus.test.TestCase):
    pass


class BaseCBVTestCase(BaseTestMixin, test_plus.test.CBVTestCase):
    pass
