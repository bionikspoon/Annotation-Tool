from django.conf import settings
from django.contrib.postgres import fields as postgres
from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel

breakend_choices = Choices('Forward', 'Reverse')
breakend_direction = Choices('Left', 'Right')
sex_choices = Choices('Male', 'Female', 'Mixed', 'Unknown')


class Pubmed(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='pubmed_entries', db_index=True)
    pubmed_id = models.PositiveIntegerField(db_index=True)
    gene = models.CharField(max_length=128, blank=True)
    # structure = models.ForeignKey()
    # mutation_type = models.ForeignKey()
    # syntax = models.ForeignKey()
    syntax_text = models.CharField(max_length=128, blank=True)
    operator = models.CharField(max_length=32, choices=Choices('Contains', 'Not Contains'), blank=True)
    # rule_level = models.ForeignKey()
    chromosome = models.CharField(max_length=128, blank=True)
    chromosome_range = postgres.IntegerRangeField(null=True, blank=True)
    breakend_strand = models.CharField(max_length=32, choices=breakend_choices, blank=True)
    breakend_direction = models.CharField(max_length=32, choices=breakend_direction, blank=True)
    mate_chromosome = models.CharField(max_length=128, blank=True)
    mate_chromosome_range = postgres.IntegerRangeField(null=True, blank=True)
    number_of_copies = postgres.IntegerRangeField(null=True, blank=True)
    coordinate_predicate = models.CharField(max_length=32, blank=True)
    # variant_type = models.ForeignKey()
    # variant_consequence = models.ForeignKey()
    variant_clinical_grade = models.PositiveSmallIntegerField(choices=Choices(*range(1, 6)), null=True, blank=True)
    # disease = models.ManyToManyField()
    treatment_number_of_arms = models.PositiveSmallIntegerField(choices=Choices(*range(1, 6)), null=True, blank=True)
    population_size = models.PositiveIntegerField(null=True, blank=True)
    sex = models.CharField(max_length=32, choices=sex_choices, blank=True)
    ethnicity = models.CharField(max_length=128, blank=True)
    # assessed_patient_outcomes = models.ManyToManyField()
    # significant_patient_outcomes = models.ManyToManyField()
    study_design = models.TextField(blank=True)
    reference_claims = models.TextField(blank=True)
    comments = models.TextField(blank=True)

    def __repr__(self):
        return ' <Pubmed:%r(pubmed_id:%r)>' % (self.id, self.pubmed_id)
