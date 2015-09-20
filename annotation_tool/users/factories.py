# Python Libraries
import logging

# Third Party Packages
from factory.django import DjangoModelFactory
from faker import Faker
from ..core.utils.factories import make

logger = logging.getLogger(__name__)
faker = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = 'users.User'

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)

    username = make(faker.user_name)
    email = make(faker.email)
    name = make(faker.name)
    password = 'secret'


class SuperUserFactory(UserFactory):
    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_superuser(*args, **kwargs)
