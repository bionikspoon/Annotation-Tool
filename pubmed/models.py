from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from model_utils import FieldTracker
from model_utils.models import TimeStampedModel
from annotation_tool.users.models import User


class Entry(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False,
                             related_name='pubmed_entries',
                             on_delete=models.PROTECT)
    pubmed_id = models.IntegerField()
    gene = models.CharField(max_length=100, blank=True)
    # structure = models.ForeignKey(StructureLookup)
    # mutation_type = models.ForeignKey(MutationTypeLookup)
    # syntax = models.ForeignKey(SyntaxLookup)
    syntax_text = models.CharField(max_length=100, blank=True)
    # operator = models.ForeignKey(OperatorLookup)
    # rule_level = models.ForeignKey(RuleLevelLookup)
    chromosome = models.CharField(max_length=100, blank=True)
    start = models.IntegerField(null=True, blank=True)
    stop = models.IntegerField(null=True, blank=True)
    # breakend_strand = models.ForeignKey(BreakendStrandLookup)
    # breakend_direction = models.ForeignKey(BreakendDirectionLookup)
    mate_chromosome = models.CharField(max_length=100, blank=True)
    mate_start = models.IntegerField(null=True, blank=True)
    mate_end = models.IntegerField(null=True, blank=True)
    # mate_breakend_strand = models.ForeignKey(MateBreakendStrandLookup)
    minimum_number_of_copies = models.IntegerField(null=True, blank=True)
    maximum_number_of_copies = models.IntegerField(null=True, blank=True)
    coordinate_predicate = models.CharField(max_length=100, blank=True)
    partner_coordinate_predicate = models.CharField(max_length=100, blank=True)
    # variant_type = models.ForeignKey(VariantTypeLookup)
    # variant_consequence = models.ForeignKey(VariantConsequenceLookup)
    variant_clinical_grade = models.IntegerField(null=True, blank=True)
    disease = models.CharField(max_length=100, blank=True)
    treatment_1 = models.CharField(max_length=100, blank=True)
    treatment_2 = models.CharField(max_length=100, blank=True)
    treatment_3 = models.CharField(max_length=100, blank=True)
    treatment_4 = models.CharField(max_length=100, blank=True)
    treatment_5 = models.CharField(max_length=100, blank=True)
    population_size = models.IntegerField(null=True, blank=True)
    # sex = models.ForeignKey(SexLookup)
    ethnicity = models.CharField(max_length=100, blank=True)
    # assessed_patient_outcomes = models.ManyToManyField(
    #     AssessedPatientOutcomeLookup, blank=True)
    # significant_patient_outcomes = models.ManyToManyField(
    #     SignificantPatientOutcomeLookup, blank=True)
    design = models.TextField(blank=True)
    reference_claims = models.TextField(blank=True)
    comments = models.TextField(blank=True)

    tracker = FieldTracker()

    def get_absolute_url(self):
        return reverse('pubmed:detail', kwargs={'pk': self.id})
