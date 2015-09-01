#!/usr/bin/env python
# coding=utf-8
from factory import SubFactory, DjangoModelFactory, Iterator
from faker import Faker

from annotation_tool.users.factories import UserFactory
import pubmed_lookup
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
    structure = Iterator(pubmed_lookup.StructureLookup.objects.all())
    mutation_type = Iterator(pubmed_lookup.MutationTypeLookup.objects.all())
    syntax = Iterator(pubmed_lookup.SyntaxLookup.objects.all())
    syntax_text = faker.text(max_nb_chars=100)
    operator = Iterator(pubmed_lookup.OperatorLookup.objects.all())
    rule_level = Iterator(pubmed_lookup.RuleLevelLookup.objects.all())
    chromosome = faker.text(max_nb_chars=100)
    start = faker.random_int()
    stop = faker.random_int()
    breakend_strand = Iterator(pubmed_lookup.BreakendStrandLookup.objects.all())
    breakend_direction = Iterator(
        pubmed_lookup.BreakendDirectionLookup.objects.all())
    mate_chromosome = faker.text(max_nb_chars=100)
    mate_start = faker.random_int()
    mate_end = faker.random_int()
    mate_breakend_strand = Iterator(
        pubmed_lookup.BreakendStrandLookup.objects.all())
    minimum_number_of_copies = faker.random_int()
    maximum_number_of_copies = faker.random_int()
    coordinate_predicate = faker.text(max_nb_chars=100)
    partner_coordinate_predicate = faker.text(max_nb_chars=100)
    variant_type = Iterator(pubmed_lookup.VariantTypeLookup.objects.all())
    variant_consequence = Iterator(
        pubmed_lookup.VariantConsequenceLookup.objects.all())
    variant_clinical_grade = faker.random_int()
    # disease = pubmed_lookup.ManyToManyField(DiseaseLookup,
    # **DEFAULTS.ManyToManyField)
    treatment_1 = faker.text(max_nb_chars=100)
    treatment_2 = faker.text(max_nb_chars=100)
    treatment_3 = faker.text(max_nb_chars=100)
    treatment_4 = faker.text(max_nb_chars=100)
    treatment_5 = faker.text(max_nb_chars=100)
    population_size = faker.random_int()
    sex = Iterator(pubmed_lookup.SexLookup.objects.all())
    ethnicity = faker.text(max_nb_chars=100)
    # assessed_patient_outcomes = pubmed_lookup.ManyToManyField(
    # AssessedPatientOutcomeLookup,
    #     **DEFAULTS.ManyToManyField)
    # significant_patient_outcomes = pubmed_lookup.ManyToManyField(
    #     SignificantPatientOutcomeLookup, **DEFAULTS.ManyToManyField)
    design = faker.paragraphs()
    reference_claims = faker.paragraphs()
    comments = faker.paragraphs()
