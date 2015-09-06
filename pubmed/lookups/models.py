# coding=utf-8

# Django Packages
from django.db import models

# Third Party Packages
from model_utils import models as utils_models
from model_utils import FieldTracker


class LookupTable(utils_models.TimeStampedModel):
    choice = models.CharField(max_length=100, unique=True)

    tracker = FieldTracker()

    class Meta:
        abstract = True

    def __str__(self):
        return self.choice


class StructureLookup(LookupTable):
    pass


class MutationTypeLookup(LookupTable):
    pass


class SyntaxLookup(LookupTable):
    pass


class OperatorLookup(LookupTable):
    pass


class RuleLevelLookup(LookupTable):
    pass


class BreakendStrandLookup(LookupTable):
    pass


class BreakendDirectionLookup(LookupTable):
    pass


class VariantTypeLookup(LookupTable):
    pass


class VariantConsequenceLookup(LookupTable):
    pass


class SexLookup(LookupTable):
    pass


class DiseaseLookup(LookupTable):
    pass


class PatientOutcomesLookup(LookupTable):
    pass
