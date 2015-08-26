#!/usr/bin/env python
# coding=utf-8

from factory.django import DjangoModelFactory
from faker import Faker
from . import models

faker = Faker()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)

    username = faker.user_name()
    email = faker.email()
    name = faker.name()


class SuperUserFactory(UserFactory):
    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_superuser(*args, **kwargs)
