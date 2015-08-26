#!/usr/bin/env python
# coding=utf-8

from django.test import SimpleTestCase
from ..migrations.initial_data.build import SummaryManager, generate_data


class InitialDataSummaryTest(SimpleTestCase):
    def test_summary(self):
        generate_data()

        self.assertTrue('')
