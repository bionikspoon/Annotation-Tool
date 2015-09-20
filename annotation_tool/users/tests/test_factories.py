# Python Libraries
import logging

# Django Packages
from django.test import TestCase

# Local Application
from ..factories import SuperUserFactory, UserFactory

logger = logging.getLogger(__name__)


class UserFactoryTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.superuser = SuperUserFactory()

    def test_factory_creates_entry(self):
        self.assertTrue(self.user)
        self.assertTrue(self.superuser)

    def test_superuser_is_admin(self):
        self.assertTrue(self.superuser.is_superuser)
        self.assertFalse(self.user.is_superuser)
