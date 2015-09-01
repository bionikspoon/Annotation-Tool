#!/usr/bin/env python
# coding=utf-8

from rest_framework.serializers import HyperlinkedModelSerializer, \
    HyperlinkedIdentityField

from annotation_tool.users.serlializers import UserSerializer
import pubmed_lookup
from .models import EntryMeta


class EntryUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = tuple(field for field in UserSerializer.Meta.fields if
                       field != 'pubmed_entries')


class EntrySerializer(HyperlinkedModelSerializer):
    user = EntryUserSerializer()

    class Meta:
        model = EntryMeta.model
        fields = ('url', 'pubmed_id') + EntryMeta.all_fields
        depth = 1
