#!/usr/bin/env python
# coding=utf-8
from factory import DjangoModelFactory
from faker import Faker

from .models import User
from ..core.utils.factories import make

faker = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)

    username = make(faker.user_name)
    email = make(faker.email)
    name = make(faker.name)
    password = 'secret'
