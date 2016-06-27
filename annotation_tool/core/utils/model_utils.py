#!/usr/bin/env python
# coding=utf-8

from django.db import models
from model_utils import Choices

__all__ = ['field_choices', 'LookupMixin', 'LookupTable']


def _upper_or_int(arg):
    try:
        return arg.upper()
    except AttributeError:
        return arg


def field_choices(*args):
    return Choices(*((_upper_or_int(arg), arg) for arg in args))


class LookupMixin(object):
    id = NotImplemented
    choice = NotImplemented

    def __repr__(self):
        return ' <%s:%r:%r>' % (self.__class__.__name__, self.id, self.choice)

    def __str__(self):
        return self.choice


class LookupTable(LookupMixin, models.Model):
    choice = models.CharField(max_length=128, unique=True, db_index=True)

    class Meta:
        abstract = True
