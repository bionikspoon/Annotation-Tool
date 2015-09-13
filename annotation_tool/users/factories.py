# Python Libraries
import logging

# Third Party Packages
from factory import LazyAttribute
from factory.django import DjangoModelFactory
from faker import Faker

logger = logging.getLogger(__name__)
faker = Faker()

_ = lambda declaration: LazyAttribute(lambda __: declaration())
"""...translate this!"""


class UserFactory(DjangoModelFactory):
    class Meta:
        model = 'users.User'

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)

    username = _(faker.user_name)
    email = _(faker.email)
    name = _(faker.name)


class SuperUserFactory(UserFactory):
    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_superuser(*args, **kwargs)
