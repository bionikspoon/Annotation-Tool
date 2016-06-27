#!/usr/bin/env python
# coding=utf-8

from pathlib import Path
from random import randint, choice

import yaml
from django.db import OperationalError
from factory import DjangoModelFactory, Iterator, LazyAttribute
from faker import Faker

from .models import (StructureLookup, MutationTypeLookup, SyntaxLookup, RuleLevelLookup, VariantTypeLookup,
                     PatientOutcomesLookup, Choices, VariantConsequenceLookup, DiseaseLookup, Pubmed)
from ..core.utils.factory_utils import lazy_callback, sample_from_many
from ..users.models import User

faker = Faker()


def gene_pool():
    try:
        # gene_count = Gene.objects.count()
        # gene_offset = randint(0, gene_count // 100)
        # return [gene.symbol for gene in Gene.objects.all()[gene_offset:gene_offset + 100]]
        raise OperationalError
    except OperationalError:
        with Config.DATA_DIR.joinpath('_gene_sample.yaml').open() as f:
            return yaml.load(f)


class Config:
    """Command constants."""
    _CWD = Path(__file__, '..').resolve()
    DATA_DIR = (_CWD / '../core/utils/_gene_sample').resolve()


class PubmedFactory(DjangoModelFactory):
    """Generate pubmed entry for testing with fake data."""

    class Meta:
        """Pubmed Factory"""
        model = Pubmed

    pubmed_id = lazy_callback(faker.random_int)
    user = LazyAttribute(lambda _: choice(User.objects.all()))

    gene = Iterator(gene_pool())
    structure = Iterator(StructureLookup.objects.all())
    mutation_type = Iterator(MutationTypeLookup.objects.all())
    syntax = Iterator(SyntaxLookup.objects.all())
    syntax_text = lazy_callback(faker.text, max_nb_chars=128)
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
    coordinate_predicate = lazy_callback(faker.text, max_nb_chars=32)
    partner_coordinate_predicate = lazy_callback(faker.text, max_nb_chars=32)
    variant_type = Iterator(VariantTypeLookup.objects.all())
    variant_consequence = Iterator(VariantConsequenceLookup.objects.all())
    variant_clinical_grade = Iterator(choice[0] for choice in Choices.RANGE_FIVE)
    disease = sample_from_many(DiseaseLookup, 'disease')
    treatment_number_of_arms = Iterator(choice[0] for choice in Choices.RANGE_FIVE)
    population_size = lazy_callback(faker.random_int)
    sex = Iterator(choice[0] for choice in Choices.SEX)
    ethnicity = lazy_callback(faker.text, max_nb_chars=128)
    assessed_patient_outcomes = sample_from_many(PatientOutcomesLookup, 'assessed_patient_outcomes')
    significant_patient_outcomes = sample_from_many(PatientOutcomesLookup, 'significant_patient_outcomes')
    study_design = lazy_callback(faker.paragraph, nb_sentences=15)
    reference_claims = lazy_callback(faker.paragraph, nb_sentences=15)
    comments = lazy_callback(faker.paragraph, nb_sentences=15)
