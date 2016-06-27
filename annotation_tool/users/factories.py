from factory import DjangoModelFactory
from faker import Faker

from .models import User
from ..core.utils.factory_utils import lazy_callback

faker = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)

    username = lazy_callback(faker.user_name)
    email = lazy_callback(faker.email)
    name = lazy_callback(faker.name)
    password = 'secret'
