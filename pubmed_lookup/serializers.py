#!/usr/bin/env python
# coding=utf-8
from rest_framework.serializers import (HyperlinkedIdentityField,
    HyperlinkedModelSerializer)
from pubmed import EntrySerializer
from . import models


class LookupTableSerializer(HyperlinkedModelSerializer):
    url = NotImplemented
    entry = pubmed.serializers.EntrySerializer(many=True, read_only=True,
                                               view_name='api:entry-detail')

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
    url = HyperlinkedIdentityField(view_name='api:patientoutcomeslookup-detail')

    class Meta(LookupTableSerializer.Meta):
        model = models.PatientOutcomesLookup
