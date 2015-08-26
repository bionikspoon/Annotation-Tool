#!/usr/bin/env python
# coding=utf-8
from factory import SubFactory

from factory.django import DjangoModelFactory
from . import models
from annotation_tool.users.factories import UserFactory


class EntryFactory(DjangoModelFactory):
    class Meta:
        model = models.Entry

    pubmed_id = 1234
    user = SubFactory(UserFactory)
