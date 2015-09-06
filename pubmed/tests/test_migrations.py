# Django Packages
from django.test import SimpleTestCase, override_settings


@override_settings(DATABASES={
    'default': {}
    })
class InitialDataSummaryTest(SimpleTestCase):
    def test_summary(self):
        pass
