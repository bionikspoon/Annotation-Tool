#!/usr/bin/env python
# coding=utf-8
from rest_framework import serializers

from .models import Pubmed


class PubmedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pubmed
        fields = (

            'url',
            'user',
            'created',
            'modified',
            'pubmed_id',
            'gene',
            'syntax_text',
            'operator',
            'chromosome',
            'chromosome_range',
            'breakend_strand',
            'breakend_direction',
            'mate_chromosome',
            'mate_chromosome_range',
            'number_of_copies',
            'coordinate_predicate',
            'variant_clinical_grade',
            'treatment_number_of_arms',
            'population_size',
            'sex',
            'ethnicity',
            'study_design',
            'reference_claims',
            'comments'

        )
