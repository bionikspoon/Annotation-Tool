#!/usr/bin/env python
# coding=utf-8
from test_plus.test import TestCase, CBVTestCase
from annotation_tool.users.factories import UserFactory


class BaseTestMixin(object):
    """Override user factory"""
    user_factory = UserFactory


class BaseTestCase(BaseTestMixin, TestCase):
    pass


class BaseCBVTestCase(BaseTestMixin, CBVTestCase):
    pass
