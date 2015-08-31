#!/usr/bin/env python
# coding=utf-8

from rest_framework.serializers import (ModelSerializer,
    HyperlinkedIdentityField)
from rest_framework import serializers

from annotation_tool.users.serlializers import UserSerializer
from . import models


class LookupTableSerializer(serializers.HyperlinkedModelSerializer):
    url = NotImplemented

    class Meta:
        model = models.LookupTable
        fields = ('id', 'choice', 'url')


class StructureLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:structurelookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.StructureLookup


class MutationTypeLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:mutationtypelookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.MutationTypeLookup


class SyntaxLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:syntaxlookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.SyntaxLookup


class OperatorLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:operatorlookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.OperatorLookup


class RuleLevelLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:rulelevellookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.RuleLevelLookup


class BreakendStrandLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:breakendstrandlookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.BreakendStrandLookup


class BreakendDirectionLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(
        view_name='api:breakenddirectionlookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.BreakendDirectionLookup


class VariantTypeLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:varianttypelookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.VariantTypeLookup


class VariantConsequenceLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(
        view_name='api:variantconsequencelookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.VariantConsequenceLookup


class SexLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:sexlookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.SexLookup


class DiseaseLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:diseaselookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.DiseaseLookup


class PatientOutcomesLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:patientoutcomelookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.PatientOutcomesLookup


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
    # assessed_patient_outcomes = PatientOutcomesLookupSerializer(many=True )
    # significant_patient_outcomes = PatientOutcomesLookupSerializer(many=True)

    class Meta:
        model = models.Entry
        fields = ('url',) + models.EntryMeta.all_fields
        depth = 1
