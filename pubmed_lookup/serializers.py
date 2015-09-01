#!/usr/bin/env python
# coding=utf-8
from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import (HyperlinkedIdentityField,
    HyperlinkedModelSerializer)

from . import models


class LookupTableSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.LookupTable
        fields = ('id', 'choice', 'url')


class EntrySetLookupTableSerializer(LookupTableSerializer):
    entry_set = HyperlinkedRelatedField(view_name='api:entry-detail',
                                        read_only=True, many=True)

    class Meta:
        model = models.LookupTable
        fields = ('id', 'choice', 'url')


class StructureLookupSerializer(EntrySetLookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:structurelookup-detail')

    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.StructureLookup


class MutationTypeLookupSerializer(EntrySetLookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:mutationtypelookup-detail')

    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.MutationTypeLookup


class SyntaxLookupSerializer(EntrySetLookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:syntaxlookup-detail')

    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.SyntaxLookup


class OperatorLookupSerializer(EntrySetLookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:operatorlookup-detail')

    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.OperatorLookup


class RuleLevelLookupSerializer(EntrySetLookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:rulelevellookup-detail')

    class Meta(EntrySetLookupTableSerializer.Meta):
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


class VariantTypeLookupSerializer(EntrySetLookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:varianttypelookup-detail')

    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.VariantTypeLookup


class VariantConsequenceLookupSerializer(EntrySetLookupTableSerializer):
    url = HyperlinkedIdentityField(
        view_name='api:variantconsequencelookup-detail')

    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.VariantConsequenceLookup


class SexLookupSerializer(EntrySetLookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:sexlookup-detail')

    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.SexLookup


class DiseaseLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:diseaselookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.DiseaseLookup


class PatientOutcomesLookupSerializer(LookupTableSerializer):
    url = HyperlinkedIdentityField(view_name='api:patientoutcomeslookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.PatientOutcomesLookup
