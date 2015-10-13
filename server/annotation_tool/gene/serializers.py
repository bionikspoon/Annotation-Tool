#!/usr/bin/env python
# coding=utf-8
from rest_framework.serializers import ModelSerializer

from .models import Gene


class GeneSerializer(ModelSerializer):
    class Meta:
        model = Gene
        fields = 'url', 'uuid'
