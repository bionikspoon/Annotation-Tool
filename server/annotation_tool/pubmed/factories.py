#!/usr/bin/env python
# coding=utf-8
from random import randint, choice
from factory import DjangoModelFactory, Iterator, LazyAttribute
from faker import Faker
from .models import (StructureLookup, MutationTypeLookup, SyntaxLookup, RuleLevelLookup, VariantTypeLookup,
                     PatientOutcomesLookup, Choices, VariantConsequenceLookup, DiseaseLookup, Pubmed, Gene)
from ..users.models import User
from ..utils import make, many_to_many

faker = Faker()

gene_offset = randint(0, Gene.objects.count() // 100)


class PubmedFactory(DjangoModelFactory):
    """Generate pubmed entry for testing with fake data."""

    class Meta:
        """Pubmed Factory"""
        model = Pubmed

    pubmed_id = make(faker.random_int)
    user = LazyAttribute(lambda _: choice(User.objects.all()))

    gene = Iterator(Gene.objects.all()[gene_offset:gene_offset + 100], getter=lambda obj: obj.symbol)
    structure = Iterator(StructureLookup.objects.all())
    mutation_type = Iterator(MutationTypeLookup.objects.all())
    syntax = Iterator(SyntaxLookup.objects.all())
    syntax_text = make(faker.text, max_nb_chars=128)
    operator = Iterator(choice[0] for choice in Choices.OPERATOR)
    rule_level = Iterator(RuleLevelLookup.objects.all())
    chromosome = Iterator(choice[0] for choice in Choices.RANGE_TWENTY_THREE)
    chromosome_range = LazyAttribute(lambda _: (randint(12, 12), randint(12, 24)))
    breakend_strand = Iterator(choice[0] for choice in Choices.STRAND)
    breakend_direction = Iterator(choice[0] for choice in Choices.DIRECTION)
    mate_chromosome = Iterator(choice[0] for choice in Choices.RANGE_TWENTY_THREE)
    mate_chromosome_range = LazyAttribute(lambda _: (randint(12, 12), randint(12, 24)))
    mate_breakend_strand = Iterator(choice[0] for choice in Choices.STRAND)
    number_of_copies = LazyAttribute(lambda _: (randint(12, 12), randint(12, 24)))
    coordinate_predicate = make(faker.text, max_nb_chars=32)
    partner_coordinate_predicate = make(faker.text, max_nb_chars=32)
    variant_type = Iterator(VariantTypeLookup.objects.all())
    variant_consequence = Iterator(VariantConsequenceLookup.objects.all())
    variant_clinical_grade = Iterator(choice[0] for choice in Choices.RANGE_FIVE)
    disease = many_to_many(DiseaseLookup, 'disease')
    treatment_number_of_arms = Iterator(choice[0] for choice in Choices.RANGE_FIVE)
    population_size = make(faker.random_int)
    sex = Iterator(choice[0] for choice in Choices.SEX)
    ethnicity = make(faker.text, max_nb_chars=128)
    assessed_patient_outcomes = many_to_many(PatientOutcomesLookup, 'assessed_patient_outcomes')
    significant_patient_outcomes = many_to_many(PatientOutcomesLookup, 'significant_patient_outcomes')
    study_design = make(faker.paragraph, nb_sentences=15)
    reference_claims = make(faker.paragraph, nb_sentences=15)
    comments = make(faker.paragraph, nb_sentences=15)
