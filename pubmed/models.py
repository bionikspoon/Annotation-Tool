from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from model_utils import FieldTracker, Choices
from model_utils.models import TimeStampedModel

from annotation_tool.users.models import User


class LookupTable(TimeStampedModel):
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


class PatientOutcomeLookup(LookupTable):
    pass


class DEFAULTS(object):
    CharField = dict(max_length=100, blank=True)
    ForeignKey = dict(blank=True, null=True, on_delete=models.SET_NULL)
    IntegerField = dict(null=True, blank=True)
    TextField = dict(blank=True)
    ManyToManyField = dict(blank=True)


class Entry(TimeStampedModel):
    user = models.ForeignKey(

        settings.AUTH_USER_MODEL, editable=False, related_name='pubmed_entries',
        on_delete=models.PROTECT)

    pubmed_id = models.PositiveIntegerField()
    gene = models.CharField(**DEFAULTS.CharField)
    structure = models.ForeignKey(StructureLookup, **DEFAULTS.ForeignKey)
    mutation_type = models.ForeignKey(MutationTypeLookup, **DEFAULTS.ForeignKey)
    syntax = models.ForeignKey(SyntaxLookup, **DEFAULTS.ForeignKey)
    syntax_text = models.CharField(**DEFAULTS.CharField)
    operator = models.ForeignKey(OperatorLookup, **DEFAULTS.ForeignKey)
    rule_level = models.ForeignKey(RuleLevelLookup, **DEFAULTS.ForeignKey)
    chromosome = models.CharField(**DEFAULTS.CharField)
    start = models.PositiveIntegerField(**DEFAULTS.IntegerField)
    stop = models.PositiveIntegerField(**DEFAULTS.IntegerField)
    breakend_strand = models.ForeignKey(

        BreakendStrandLookup, **DEFAULTS.ForeignKey)

    breakend_direction = models.ForeignKey(

        BreakendDirectionLookup, **DEFAULTS.ForeignKey)

    mate_chromosome = models.CharField(**DEFAULTS.CharField)
    mate_start = models.PositiveIntegerField(**DEFAULTS.IntegerField)
    mate_end = models.PositiveIntegerField(**DEFAULTS.IntegerField)
    mate_breakend_strand = models.ForeignKey(

        BreakendStrandLookup, related_name='mate_breakend_strand',
        **DEFAULTS.ForeignKey)

    mate_breakend_direction = models.ForeignKey(

        BreakendDirectionLookup, related_name='mate_breakend_direction',
        **DEFAULTS.ForeignKey)

    minimum_number_of_copies = models.PositiveIntegerField(
        **DEFAULTS.IntegerField)

    maximum_number_of_copies = models.PositiveIntegerField(
        **DEFAULTS.IntegerField)

    coordinate_predicate = models.CharField(**DEFAULTS.CharField)
    partner_coordinate_predicate = models.CharField(**DEFAULTS.CharField)
    variant_type = models.ForeignKey(VariantTypeLookup, **DEFAULTS.ForeignKey)
    variant_consequence = models.ForeignKey(

        VariantConsequenceLookup, **DEFAULTS.ForeignKey)

    variant_clinical_grade = models.PositiveIntegerField(
        choices=Choices(*range(1, 6)), **DEFAULTS.IntegerField)

    disease = models.ManyToManyField(DiseaseLookup, **DEFAULTS.ManyToManyField)
    treatment_1 = models.CharField(**DEFAULTS.CharField)
    treatment_2 = models.CharField(**DEFAULTS.CharField)
    treatment_3 = models.CharField(**DEFAULTS.CharField)
    treatment_4 = models.CharField(**DEFAULTS.CharField)
    treatment_5 = models.CharField(**DEFAULTS.CharField)
    population_size = models.PositiveIntegerField(**DEFAULTS.IntegerField)
    sex = models.ForeignKey(SexLookup, **DEFAULTS.ForeignKey)
    ethnicity = models.CharField(**DEFAULTS.CharField)
    assessed_patient_outcomes = models.ManyToManyField(

        PatientOutcomeLookup, related_name='assessed_patient_outcomes',
        **DEFAULTS.ManyToManyField)

    significant_patient_outcomes = models.ManyToManyField(

        PatientOutcomeLookup, related_name='significant_patient_outcomes',
        **DEFAULTS.ManyToManyField)

    design = models.TextField(**DEFAULTS.TextField)
    reference_claims = models.TextField(**DEFAULTS.TextField)
    comments = models.TextField(**DEFAULTS.TextField)

    tracker = FieldTracker()

    def get_absolute_url(self):
        return reverse('pubmed:detail', kwargs={
            'pk': self.id
        })

    def __str__(self):
        gene = ':%s' % self.gene if self.gene else ''
        return '%s:%s%s' % (self.pubmed_id, self.id, gene)

    class Meta:
        verbose_name_plural = 'Entries'


class EntryMeta(object):
    model = Entry
    fields = (

        'pubmed_id', 'gene', 'structure', 'mutation_type', 'syntax',
        'syntax_text', 'operator', 'rule_level', 'chromosome', 'start', 'stop',
        'breakend_strand', 'breakend_direction', 'mate_chromosome',
        'mate_start', 'mate_end', 'mate_breakend_strand',
        'mate_breakend_direction', 'minimum_number_of_copies',
        'maximum_number_of_copies', 'coordinate_predicate',
        'partner_coordinate_predicate', 'variant_type', 'variant_consequence',
        'variant_clinical_grade', 'disease', 'treatment_1', 'treatment_2',
        'treatment_3', 'treatment_4', 'treatment_5', 'population_size', 'sex',
        'ethnicity', 'assessed_patient_outcomes',
        'significant_patient_outcomes', 'design', 'reference_claims',
        'comments')
    # fields = Entry._meta.get_fields(include_parents=False)[1:]
