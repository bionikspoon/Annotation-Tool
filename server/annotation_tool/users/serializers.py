#!/usr/bin/env python
# coding=utf-8
from rest_framework import serializers

from .models import User
from ..pubmed.models import PUBMED_ENTRIES


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = 'url', 'username', 'name', PUBMED_ENTRIES
