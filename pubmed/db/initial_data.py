#!/usr/bin/env python
# coding=utf-8
from collections import namedtuple

LookupChoice = namedtuple('LookupChoice', ('cls', 'pk', 'choice'))


class InitialData(object):
    @classmethod
    def export(cls):
        return (

            LookupChoice(subclass.__name__, pk, choice)

            for subclass in cls.__subclasses__()

            for pk, choice in enumerate(subclass.choices)

        )

def populate_lookup_tables(apps, schema_editor):
    for entry in InitialData.export():
        Model = apps.get_model('pubmed', entry.cls)
        Model.objects.create(pk=entry.pk, choice=entry.choice)


class StructureLookup(InitialData):
    choices = ['Sequence', 'Structural', ]


class MutationTypeLookup(InitialData):
    choices = ['Variant', 'Rule', ]


class SyntaxLookup(InitialData):
    choices = ['Genomic', 'cDNA', 'Protein', ]


class RuleLevelLookup(InitialData):
    choices = ['Genomic', 'cDNA', 'Protein', ]


class OperatorLookup(InitialData):
    choices = ['Contains', 'Not Contains', ]


class BreakendStrandLookup(InitialData):
    choices = ['Forward', 'Reverse', ]


class BreakendDirectionLookup(InitialData):
    choices = ['Left', 'Right', ]


class MateBreakendStrandLookup(InitialData):
    choices = ['Forward', 'Reverse', ]


class SexLookup(InitialData):
    choices = ['Male', 'Female', 'Mixed', 'Other', ]


class AssessedPatientOutcomeLookup(InitialData):
    choices = ['Disease Progression', 'Disease-Control Rate',
               'Disease-Free Survival', 'Event-Free Survival',
               'Median Survival', 'Objective Response', 'Overall Response Rate',
               'Overall Survival', 'Post-Recurrence Survival', 'Prognosis',
               'Progression-Free Survival', 'Remission', 'Response Rate',
               'Time To Progression', 'Time To Relapse', 'Toxicity',
               'Treatment-Related Mortality', ]


class SignificantPatientOutcomeLookup(InitialData):
    choices = ['Disease Progression', 'Disease-Control Rate',
               'Disease-Free Survival', 'Event-Free Survival',
               'Median Survival', 'Objective Response', 'Overall Response Rate',
               'Overall Survival', 'Post-Recurrence Survival', 'Prognosis',
               'Progression-Free Survival', 'Remission', 'Response Rate',
               'Time To Progression', 'Time To Relapse', 'Toxicity', ]


class VariantConsequenceLookup(InitialData):
    choices = ['Non Synonymous Missense', 'Non Synonymous Nonsense', ]


class VariantTypeLookup(InitialData):
    choices = ['Deletion', 'Duplication', 'Indel', 'Insertion',
               'Substitution', ]


if __name__ == '__main__':
    print(list(InitialData.export()))
