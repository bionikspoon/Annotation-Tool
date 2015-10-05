from django.conf import settings
from django.contrib.postgres import fields as postgres
from django.core.validators import MaxValueValidator
from django.db import models
from model_utils.models import TimeStampedModel

from ..utils import choices


class Choices:
    OPERATOR = choices('Contains', 'Not Contains')
    STRAND = choices('Forward', 'Reverse')
    DIRECTION = choices('Left', 'Right')
    SEX = choices('Male', 'Female', 'Mixed', 'Unknown')
    RANGE_FIVE = choices(*range(1, 6))
    RANGE_TWENTY_THREE = choices(*range(1, 24))


PUBMED_ENTRIES = 'pubmed_entries'


class Gene(TimeStampedModel):
    uuid = models.UUIDField(primary_key=True)
    version = models.PositiveIntegerField()
    hgnc_id = models.CharField(max_length=16, unique=True, db_index=True)
    ccds_id = postgres.ArrayField(models.CharField(max_length=32))
    cosmic = models.CharField(max_length=32)
    date_modified = models.DateField()
    date_approved_reserved = models.DateField()
    name = models.CharField(max_length=32)
    symbol = models.CharField(max_length=16, db_index=True)
    alias_name = postgres.ArrayField(models.CharField(max_length=64))  # 2
    alias_symbol = postgres.ArrayField(models.CharField(max_length=16))  # 2
    location = models.CharField(max_length=16)
    location_sortable = models.CharField(max_length=16)
    locus_type = models.CharField(max_length=32)
    locus_group = models.CharField(max_length=32)
    gene_family = postgres.ArrayField(models.CharField(max_length=64))
    gene_family_id = postgres.ArrayField(models.PositiveIntegerField())

    status = models.CharField(max_length=16)
    entrez_id = models.PositiveIntegerField()
    ensembl_gene_id = models.CharField(max_length=32)
    refseq_accession = postgres.ArrayField(models.CharField(max_length=16))

    ena = postgres.ArrayField(models.CharField(max_length=16))
    pubmed_id = postgres.ArrayField(models.PositiveIntegerField())
    rgd_id = postgres.ArrayField(models.CharField(max_length=16))
    snornabase = models.CharField(max_length=16)
    ucsc_id = models.CharField(max_length=16)
    uniprot_ids = postgres.ArrayField(models.CharField(max_length=16))
    vega_id = models.CharField(max_length=16)
    mgd_id = postgres.ArrayField(models.CharField(max_length=16))
    omim_id = postgres.ArrayField(models.PositiveIntegerField())
    enzyme_id = postgres.ArrayField(models.CharField(max_length=16))
    homeodb = models.PositiveIntegerField
    horde_id = models.CharField(max_length=16)
    lsdb = postgres.ArrayField(models.CharField(max_length=64))
    kznf_gene_catalog = models.PositiveIntegerField
    lncrnadb = models.PositiveIntegerField
    bioparadigms_slc = models.CharField(max_length=16)
    cd = models.CharField(max_length=16)
    date_name_changed = models.DateField()
    date_symbol_changed = models.DateField()
    imgt = models.CharField(max_length=16)
    intermediate_filament_db = models.CharField(max_length=16)
    iuphar = models.CharField(max_length=16)
    merops = models.CharField(max_length=16)
    mirbase = models.CharField(max_length=16)
    orphanet = models.CharField(max_length=16)
    prev_name = postgres.ArrayField(models.CharField(max_length=64))
    prev_symbol = postgres.ArrayField(models.CharField(max_length=16))


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
    chromosome = models.PositiveSmallIntegerField(blank=True, null=True, choices=Choices.RANGE_TWENTY_THREE,
                                                  validators=[MaxValueValidator(23)])
    chromosome_range = postgres.IntegerRangeField(null=True, blank=True)
    breakend_strand = models.CharField(max_length=32, choices=Choices.STRAND, blank=True)
    breakend_direction = models.CharField(max_length=32, choices=Choices.DIRECTION, blank=True)
    mate_chromosome = models.PositiveSmallIntegerField(blank=True, null=True, choices=Choices.RANGE_TWENTY_THREE,
                                                       validators=[MaxValueValidator(23)])
    mate_chromosome_range = postgres.IntegerRangeField(null=True, blank=True)
    mate_breakend_strand = models.CharField(max_length=32, choices=Choices.STRAND, blank=True)
    mate_breakend_direction = models.CharField(max_length=32, choices=Choices.DIRECTION, blank=True)
    number_of_copies = postgres.IntegerRangeField(null=True, blank=True)
    coordinate_predicate = models.CharField(max_length=32, blank=True)
    partner_coordinate_predicate = models.CharField(max_length=32, blank=True)
    variant_type = models.ForeignKey(VariantTypeLookup, related_name=PUBMED_ENTRIES, null=True)
    variant_consequence = models.ForeignKey(VariantConsequenceLookup, related_name=PUBMED_ENTRIES, null=True)
    variant_clinical_grade = models.PositiveSmallIntegerField(choices=Choices.RANGE_FIVE, null=True, blank=True,
                                                              validators=[MaxValueValidator(5)])
    disease = models.ManyToManyField(DiseaseLookup, related_name=PUBMED_ENTRIES, blank=True)
    treatment_number_of_arms = models.PositiveSmallIntegerField(choices=Choices.RANGE_FIVE, null=True, blank=True,
                                                                validators=[MaxValueValidator(5)])
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
