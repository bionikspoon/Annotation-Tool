#!/usr/bin/env python
# coding=utf-8

from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel

__all__ = ['choices', 'LookupTable']


def _upper_or_int(arg):
    try:
        return arg.upper()
    except AttributeError:
        return arg


def choices(*args):
    return Choices(*((_upper_or_int(arg), arg) for arg in args))


class LookupTable(TimeStampedModel):
    choice = models.CharField(max_length=128, unique=True, db_index=True)

    class Meta:
        abstract = True

    def __repr__(self):
        return ' <%s:%r:%r>' % (self.__class__.__name__, self.id, self.choice)

    def __str__(self):
        return self.choice
