#!/usr/bin/env python
# coding=utf-8

from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from annotation_tool.users.serlializers import UserSerializer
from pubmed_lookup import serializers as lookup_serializers
from pubmed import models as pubmed_models


class EntryUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = tuple(field for field in UserSerializer.Meta.fields if
                       field != 'pubmed_entries')


class EntrySerializer(ModelSerializer):
    user = EntryUserSerializer()
    url = HyperlinkedIdentityField(view_name='api:entry-detail')
    structure = lookup_serializers.StructureLookupSerializer()
    mutation_type = lookup_serializers.MutationTypeLookupSerializer()
    syntax = lookup_serializers.SyntaxLookupSerializer()
    operator = lookup_serializers.OperatorLookupSerializer()
    rule_level = lookup_serializers.RuleLevelLookupSerializer()
    breakend_strand = lookup_serializers.BreakendStrandLookupSerializer()
    breakend_direction = lookup_serializers.BreakendDirectionLookupSerializer()
    mate_breakend_strand = lookup_serializers.BreakendStrandLookupSerializer()
    mate_breakend_direction = (
        lookup_serializers.BreakendDirectionLookupSerializer())

    variant_type = lookup_serializers.VariantTypeLookupSerializer()
    variant_consequence = (
        lookup_serializers.VariantConsequenceLookupSerializer())

    sex = lookup_serializers.SexLookupSerializer()
    disease = lookup_serializers.DiseaseLookupSerializer(many=True)
    assessed_patient_outcomes = (
        lookup_serializers.PatientOutcomesLookupSerializer(many=True))

    significant_patient_outcomes = (
        lookup_serializers.PatientOutcomesLookupSerializer(many=True))

    class Meta:
        model = pubmed_models.Entry
        fields = ('url',) + pubmed_models.EntryMeta.all_fields
        depth = 1
