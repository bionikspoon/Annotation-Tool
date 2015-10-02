#!/usr/bin/env python
# coding=utf-8
from rest_framework import serializers

from annotation_tool.pubmed.models import Pubmed


class PubmedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pubmed
        fields = ('url', 'pubmed_id', 'gene', 'chromosome')
