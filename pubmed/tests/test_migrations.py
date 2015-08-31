#!/usr/bin/env python
# coding=utf-8
from django.test import override_settings, SimpleTestCase


@override_settings(DATABASES={'default': {}})
class InitialDataSummaryTest(SimpleTestCase):
    def test_summary(self):
        pass
