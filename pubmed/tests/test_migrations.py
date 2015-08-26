#!/usr/bin/env python
# coding=utf-8
from django.db import migrations
from django.test import override_settings, SimpleTestCase

from ..migrations.initial_data.build import generate_data
from ..migrations.initial_data import (populate_lookup_tables,
                                       unpopulate_lookup_tables)


@override_settings(DATABASES={'default': {}})
class InitialDataSummaryTest(SimpleTestCase):
    def test_summary(self):
        pass
