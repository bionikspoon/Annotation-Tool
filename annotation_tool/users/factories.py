#!/usr/bin/env python
# coding=utf-8

from factory.django import DjangoModelFactory
from . import models


class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)
