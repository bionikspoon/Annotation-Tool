#!/usr/bin/env python
# coding=utf-8
from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import (HyperlinkedModelSerializer, Serializer)

from . import models


class LookupTableSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.LookupTable
        fields = ('id', 'choice', 'url')


class EntrySetLookupTableSerializer(LookupTableSerializer):
    entry_set = HyperlinkedRelatedField(view_name='entry-detail',
        read_only=True, many=True)

    class Meta:
        model = models.LookupTable
        fields = ('id', 'choice', 'url', 'entry_set')


class StructureLookupSerializer(EntrySetLookupTableSerializer):
    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.StructureLookup


class MutationTypeLookupSerializer(EntrySetLookupTableSerializer):
    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.MutationTypeLookup


class SyntaxLookupSerializer(EntrySetLookupTableSerializer):
    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.SyntaxLookup


class OperatorLookupSerializer(EntrySetLookupTableSerializer):
    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.OperatorLookup


class RuleLevelLookupSerializer(EntrySetLookupTableSerializer):
    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.RuleLevelLookup


class BreakendStrandLookupSerializer(LookupTableSerializer):
    breakend_strand_entry_set = HyperlinkedRelatedField(
        view_name='entry-detail', read_only=True, many=True)
    mate_breakend_strand_entry_set = HyperlinkedRelatedField(
        view_name='entry-detail', read_only=True, many=True)

    class Meta:
        model = models.BreakendStrandLookup
        fields = LookupTableSerializer.Meta.fields + (
            'breakend_strand_entry_set', 'mate_breakend_strand_entry_set')


class BreakendDirectionLookupSerializer(LookupTableSerializer):
    breakend_direction_entry_set = HyperlinkedRelatedField(
        view_name='entry-detail', read_only=True, many=True)
    mate_breakend_direction_entry_set = HyperlinkedRelatedField(
        view_name='entry-detail', read_only=True, many=True)

    class Meta:
        model = models.BreakendDirectionLookup
        fields = LookupTableSerializer.Meta.fields + (
            'breakend_direction_entry_set', 'mate_breakend_direction_entry_set')


class VariantTypeLookupSerializer(EntrySetLookupTableSerializer):
    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.VariantTypeLookup


class VariantConsequenceLookupSerializer(EntrySetLookupTableSerializer):
    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.VariantConsequenceLookup


class SexLookupSerializer(EntrySetLookupTableSerializer):
    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.SexLookup


class DiseaseLookupSerializer(EntrySetLookupTableSerializer):
    class Meta(EntrySetLookupTableSerializer.Meta):
        model = models.DiseaseLookup


class PatientOutcomesLookupSerializer(LookupTableSerializer):
    assessed_patient_outcomes_entry_set = HyperlinkedRelatedField(
        view_name='entry-detail', read_only=True, many=True)
    significant_patient_outcomes_entry_set = HyperlinkedRelatedField(
        view_name='entry-detail', read_only=True, many=True)

    class Meta:
        model = models.PatientOutcomesLookup
        fields = LookupTableSerializer.Meta.fields + (
            'assessed_patient_outcomes_entry_set',
            'significant_patient_outcomes_entry_set')


class LookupBaseSerializer(Serializer):
    LookupTable = LookupTableSerializer()
