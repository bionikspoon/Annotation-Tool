#!/usr/bin/env python
# coding=utf-8
from random import randint

from factory import DjangoModelFactory, Iterator, SubFactory, LazyAttribute
from faker import Faker

from .models import (StructureLookup, MutationTypeLookup, SyntaxLookup, RuleLevelLookup, VariantTypeLookup,
                     PatientOutcomesLookup, Choices, VariantConsequenceLookup, DiseaseLookup, Pubmed)
from ..users.factories import UserFactory
from ..utils import make, many_to_many

faker = Faker()


class PubmedFactory(DjangoModelFactory):
    class Meta:
        model = Pubmed

    pubmed_id = make(faker.random_int)
    user = SubFactory(UserFactory)

    gene = make(faker.text, max_nb_chars=128)
    structure = Iterator(StructureLookup.objects.all())
    mutation_type = Iterator(MutationTypeLookup.objects.all())
    syntax = Iterator(SyntaxLookup.objects.all())
    syntax_text = make(faker.text, max_nb_chars=128)
    operator = Iterator(Choices.OPERATOR)
    rule_level = Iterator(RuleLevelLookup.objects.all())
    chromosome = make(faker.text, max_nb_chars=128)
    chromosome_range = LazyAttribute(lambda _: (randint(12, 12), randint(12, 24)))
    breakend_strand = Iterator(Choices.STRAND)
    breakend_direction = Iterator(Choices.DIRECTION)
    mate_chromosome = make(faker.text, max_nb_chars=128)
    mate_chromosome_range = LazyAttribute(lambda _: (randint(12, 12), randint(12, 24)))
    mate_breakend_strand = Iterator(Choices.STRAND)
    number_of_copies = LazyAttribute(lambda _: (randint(12, 12), randint(12, 24)))
    coordinate_predicate = make(faker.text, max_nb_chars=32)
    partner_coordinate_predicate = make(faker.text, max_nb_chars=32)
    variant_type = Iterator(VariantTypeLookup.objects.all())
    variant_consequence = Iterator(VariantConsequenceLookup.objects.all())
    variant_clinical_grade = Iterator(range(1, 6))
    disease = many_to_many(DiseaseLookup, 'disease')
    treatment_number_of_arms = Iterator(range(1, 6))
    population_size = make(faker.random_int)
    sex = Iterator(Choices.SEX)
    ethnicity = make(faker.text, max_nb_chars=128)
    assessed_patient_outcomes = many_to_many(PatientOutcomesLookup, 'assessed_patient_outcomes')
    significant_patient_outcomes = many_to_many(PatientOutcomesLookup, 'significant_patient_outcomes')
    study_design = make(faker.paragraph, nb_sentences=15)
    reference_claims = make(faker.paragraph, nb_sentences=15)
    comments = make(faker.paragraph, nb_sentences=15)
