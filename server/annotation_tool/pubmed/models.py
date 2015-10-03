from django.conf import settings
from django.contrib.postgres import fields as postgres
from django.db import models
from model_utils.models import TimeStampedModel

from ..utils import choices


class Choices:
    OPERATOR = choices('Contains', 'Not Contains')
    STRAND = choices('Forward', 'Reverse')
    DIRECTION = choices('Left', 'Right')
    SEX = choices('Male', 'Female', 'Mixed', 'Unknown')
    RANGE_FIVE = choices(*range(1, 6))


PUBMED_ENTRIES = 'pubmed_entries'


class LookupTable(TimeStampedModel):
    choice = models.CharField(max_length=128, unique=True, db_index=True)

    class Meta:
        abstract = True

    def __repr__(self):
        return ' <%s:%r:%r>' % (self.__class__.__name__, self.id, self.choice)

    def __str__(self):
        return self.choice


class StructureLookup(LookupTable):
    pass


class MutationTypeLookup(LookupTable):
    pass


class SyntaxLookup(LookupTable):
    pass


class RuleLevelLookup(LookupTable):
    pass


class VariantTypeLookup(LookupTable):
    pass


class VariantConsequenceLookup(LookupTable):
    pass


class DiseaseLookup(LookupTable):
    pass


class PatientOutcomesLookup(LookupTable):
    pass


class Pubmed(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=PUBMED_ENTRIES, db_index=True)
    pubmed_id = models.PositiveIntegerField(db_index=True)
    gene = models.CharField(max_length=128, blank=True)
    structure = models.ForeignKey(StructureLookup, related_name=PUBMED_ENTRIES, null=True)
    mutation_type = models.ForeignKey(MutationTypeLookup, related_name=PUBMED_ENTRIES, null=True)
    syntax = models.ForeignKey(SyntaxLookup, related_name=PUBMED_ENTRIES, null=True)
    syntax_text = models.CharField(max_length=128, blank=True)
    operator = models.CharField(max_length=32, choices=Choices.OPERATOR, blank=True)
    rule_level = models.ForeignKey(RuleLevelLookup, related_name=PUBMED_ENTRIES, null=True)
    chromosome = models.CharField(max_length=128, blank=True)
    chromosome_range = postgres.IntegerRangeField(null=True, blank=True)
    breakend_strand = models.CharField(max_length=32, choices=Choices.STRAND, blank=True)
    breakend_direction = models.CharField(max_length=32, choices=Choices.DIRECTION, blank=True)
    mate_chromosome = models.CharField(max_length=128, blank=True)
    mate_chromosome_range = postgres.IntegerRangeField(null=True, blank=True)
    mate_breakend_strand = models.CharField(max_length=32, choices=Choices.STRAND, blank=True)
    mate_breakend_direction = models.CharField(max_length=32, choices=Choices.DIRECTION, blank=True)
    number_of_copies = postgres.IntegerRangeField(null=True, blank=True)
    coordinate_predicate = models.CharField(max_length=32, blank=True)
    partner_coordinate_predicate = models.CharField(max_length=32, blank=True)
    variant_type = models.ForeignKey(VariantTypeLookup, related_name=PUBMED_ENTRIES, null=True)
    variant_consequence = models.ForeignKey(VariantConsequenceLookup, related_name=PUBMED_ENTRIES, null=True)
    variant_clinical_grade = models.PositiveSmallIntegerField(choices=Choices.RANGE_FIVE, null=True, blank=True)
    disease = models.ManyToManyField(DiseaseLookup, related_name=PUBMED_ENTRIES, blank=True)
    treatment_number_of_arms = models.PositiveSmallIntegerField(choices=Choices.RANGE_FIVE, null=True, blank=True)
    population_size = models.PositiveIntegerField(null=True, blank=True)
    sex = models.CharField(max_length=32, choices=Choices.SEX, blank=True)
    ethnicity = models.CharField(max_length=128, blank=True)
    assessed_patient_outcomes = models.ManyToManyField(PatientOutcomesLookup,
                                                       related_name='assessed_patient_outcomes_pubmed_entries',
                                                       blank=True)
    significant_patient_outcomes = models.ManyToManyField(PatientOutcomesLookup,
                                                          related_name='significant_patient_outcomes_pubmed_entries',
                                                          blank=True)
    study_design = models.TextField(blank=True)
    reference_claims = models.TextField(blank=True)
    comments = models.TextField(blank=True)

    def __repr__(self):
        return ' <Pubmed:%r(pubmed_id:%r)>' % (self.id, self.pubmed_id)
