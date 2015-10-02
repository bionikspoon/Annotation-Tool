#!/usr/bin/env python
# coding=utf-8
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Pubmed, PUBMED_ENTRIES, StructureLookup, MutationTypeLookup, SyntaxLookup, RuleLevelLookup, \
    VariantTypeLookup, VariantConsequenceLookup, DiseaseLookup, PatientOutcomesLookup

LOOKUP_FIELDS = 'url', 'choice', 'created', 'modified', PUBMED_ENTRIES


class StructureSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = StructureLookup
        fields = LOOKUP_FIELDS


class MutationTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MutationTypeLookup
        fields = LOOKUP_FIELDS


class SyntaxSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = SyntaxLookup
        fields = LOOKUP_FIELDS


class RuleLevelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = RuleLevelLookup
        fields = LOOKUP_FIELDS


class VariantTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = VariantTypeLookup
        fields = LOOKUP_FIELDS


class VariantConsequenceSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = VariantConsequenceLookup
        fields = LOOKUP_FIELDS


class DiseaseSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = DiseaseLookup
        fields = LOOKUP_FIELDS


class PatientOutcomesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PatientOutcomesLookup
        fields = LOOKUP_FIELDS


class PubmedSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Pubmed
        fields = (

            'url', 'user', 'created', 'modified', 'pubmed_id', 'gene', 'syntax_text', 'operator', 'chromosome',
            'chromosome_range', 'breakend_strand', 'breakend_direction', 'mate_chromosome', 'mate_chromosome_range',
            'number_of_copies', 'coordinate_predicate', 'variant_clinical_grade', 'treatment_number_of_arms',
            'population_size', 'sex', 'ethnicity', 'study_design', 'reference_claims', 'comments'

        )
