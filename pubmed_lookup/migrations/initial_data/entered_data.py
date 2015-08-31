#!/usr/bin/env python
# coding=utf-8
from . import InitialData


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
