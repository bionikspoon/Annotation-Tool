#!/usr/bin/env python
# coding=utf-8

from rest_framework.relations import (HyperlinkedRelatedField,
    HyperlinkedIdentityField)
from rest_framework.serializers import ModelSerializer

from .models import EntryMeta


class EntrySerializer(ModelSerializer):
    user = HyperlinkedRelatedField(view_name='api:user-detail', read_only=True)
    url = HyperlinkedIdentityField(view_name='api:entry-detail')

    class Meta:
        model = EntryMeta.model
        fields = ('url',) + EntryMeta.all_fields
