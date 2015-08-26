#!/usr/bin/env python
# coding=utf-8

from factory.django import DjangoModelFactory
from . import models


class EntryFactory(DjangoModelFactory):
    class Meta:
        model = models.Entry
