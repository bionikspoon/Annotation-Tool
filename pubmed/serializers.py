#!/usr/bin/env python
# coding=utf-8

from rest_framework.serializers import (ModelSerializer)

from annotation_tool.users.serlializers import UserSerializer
from pubmed_lookup.serializers import *
from pubmed import models


class EntryUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = tuple(field for field in UserSerializer.Meta.fields if
                       field != 'pubmed_entries')


class EntrySerializer(ModelSerializer):
    user = EntryUserSerializer()
    url = HyperlinkedIdentityField(view_name='api:entry-detail')
    structure = StructureLookupSerializer()
    mutation_type = MutationTypeLookupSerializer()
    syntax = SyntaxLookupSerializer()
    operator = OperatorLookupSerializer()
    rule_level = RuleLevelLookupSerializer()
    breakend_strand = BreakendStrandLookupSerializer()
    breakend_direction = BreakendDirectionLookupSerializer()
    mate_breakend_strand = BreakendStrandLookupSerializer()
    mate_breakend_direction = BreakendDirectionLookupSerializer()
    variant_type = VariantTypeLookupSerializer()
    variant_consequence = VariantConsequenceLookupSerializer()
    sex = SexLookupSerializer()
    disease = DiseaseLookupSerializer(many=True)
    assessed_patient_outcomes = PatientOutcomesLookupSerializer(many=True)
    significant_patient_outcomes = PatientOutcomesLookupSerializer(many=True)

    class Meta:
        model = models.Entry
        fields = ('url',) + models.EntryMeta.all_fields
        depth = 1
