#!/usr/bin/env python
# coding=utf-8
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Gene


class GeneSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Gene
        fields = 'url', 'uuid'
