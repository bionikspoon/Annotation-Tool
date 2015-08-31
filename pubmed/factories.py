#!/usr/bin/env python
# coding=utf-8
from factory import SubFactory, DjangoModelFactory, Iterator
from faker import Faker

from annotation_tool.users.factories import UserFactory
from pubmed_lookup import models as lookup_models
from . import models

faker = Faker()


class EntryFactory(DjangoModelFactory):
    """Create empty pubmed entry for testing."""

    # noinspection PyDocstring
    class Meta:
        model = models.Entry

    pubmed_id = faker.random_int()
    user = SubFactory(UserFactory)


class PopulatedEntryFactory(EntryFactory):
    """Create populated pubmed entry for testing."""
    gene = faker.text(max_nb_chars=100)
    structure = Iterator(lookup_models.StructureLookup.objects.all())
    mutation_type = Iterator(lookup_models.MutationTypeLookup.objects.all())
    syntax = Iterator(lookup_models.SyntaxLookup.objects.all())
    syntax_text = faker.text(max_nb_chars=100)
    operator = Iterator(lookup_models.OperatorLookup.objects.all())
    rule_level = Iterator(lookup_models.RuleLevelLookup.objects.all())
    chromosome = faker.text(max_nb_chars=100)
    start = faker.random_int()
    stop = faker.random_int()
    breakend_strand = Iterator(lookup_models.BreakendStrandLookup.objects.all())
    breakend_direction = Iterator(
        lookup_models.BreakendDirectionLookup.objects.all())
    mate_chromosome = faker.text(max_nb_chars=100)
    mate_start = faker.random_int()
    mate_end = faker.random_int()
    mate_breakend_strand = Iterator(
        lookup_models.BreakendStrandLookup.objects.all())
    minimum_number_of_copies = faker.random_int()
    maximum_number_of_copies = faker.random_int()
    coordinate_predicate = faker.text(max_nb_chars=100)
    partner_coordinate_predicate = faker.text(max_nb_chars=100)
    variant_type = Iterator(lookup_models.VariantTypeLookup.objects.all())
    variant_consequence = Iterator(
        lookup_models.VariantConsequenceLookup.objects.all())
    variant_clinical_grade = faker.random_int()
    # disease = lookup_models.ManyToManyField(DiseaseLookup,
    # **DEFAULTS.ManyToManyField)
    treatment_1 = faker.text(max_nb_chars=100)
    treatment_2 = faker.text(max_nb_chars=100)
    treatment_3 = faker.text(max_nb_chars=100)
    treatment_4 = faker.text(max_nb_chars=100)
    treatment_5 = faker.text(max_nb_chars=100)
    population_size = faker.random_int()
    sex = Iterator(lookup_models.SexLookup.objects.all())
    ethnicity = faker.text(max_nb_chars=100)
    # assessed_patient_outcomes = lookup_models.ManyToManyField(
    # AssessedPatientOutcomeLookup,
    #     **DEFAULTS.ManyToManyField)
    # significant_patient_outcomes = lookup_models.ManyToManyField(
    #     SignificantPatientOutcomeLookup, **DEFAULTS.ManyToManyField)
    design = faker.paragraphs()
    reference_claims = faker.paragraphs()
    comments = faker.paragraphs()
