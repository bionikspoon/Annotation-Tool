#!/usr/bin/env python
# coding=utf-8
from rest_framework import serializers
from .models import User
from ..pubmed.models import PUBMED_ENTRIES


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = 'url', 'username', 'name', PUBMED_ENTRIES


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'email', 'name', 'groups', 'get_all_permissions', 'is_superuser'
