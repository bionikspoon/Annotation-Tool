#!/usr/bin/env python
# coding=utf-8

from rest_framework import serializers

from .models import EntryMeta


class EntrySerializer(serializers.ModelSerializer):
    class Meta(EntryMeta):
        pass
