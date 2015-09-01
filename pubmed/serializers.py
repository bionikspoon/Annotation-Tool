#!/usr/bin/env python
# coding=utf-8

from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedIdentityField

from annotation_tool.users.serlializers import UserSerializer
import pubmed_lookup
from .models import EntryMeta


class EntryUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = tuple(field for field in UserSerializer.Meta.fields if
                       field != 'pubmed_entries')


class EntrySerializer(HyperlinkedModelSerializer):
    user = EntryUserSerializer()
    # url = HyperlinkedIdentityField(view_name='api:entry-detail')
    # structure = pubmed_lookup.StructureLookupSerializer()
    # mutation_type = pubmed_lookup.MutationTypeLookupSerializer()
    # syntax = pubmed_lookup.SyntaxLookupSerializer()
    # operator = pubmed_lookup.OperatorLookupSerializer()
    # rule_level = pubmed_lookup.RuleLevelLookupSerializer()
    # breakend_strand = pubmed_lookup.BreakendStrandLookupSerializer()
    # breakend_direction = pubmed_lookup.BreakendDirectionLookupSerializer()
    # mate_breakend_strand = pubmed_lookup.BreakendStrandLookupSerializer()
    # mate_breakend_direction = (
    #     pubmed_lookup.BreakendDirectionLookupSerializer())
    #
    # variant_type = pubmed_lookup.VariantTypeLookupSerializer()
    # variant_consequence = (pubmed_lookup.VariantConsequenceLookupSerializer())
    #
    # sex = pubmed_lookup.SexLookupSerializer()
    # disease = pubmed_lookup.DiseaseLookupSerializer(many=True)
    # assessed_patient_outcomes = (
    #     pubmed_lookup.PatientOutcomesLookupSerializer(many=True))
    #
    # significant_patient_outcomes = (
    #     pubmed_lookup.PatientOutcomesLookupSerializer(many=True))

    class Meta:
        model = EntryMeta.model
        fields = ('url',) + EntryMeta.all_fields
        depth =1
