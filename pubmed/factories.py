"""
Pubmed factory definitions.
"""

from factory import SubFactory, DjangoModelFactory, Iterator, LazyAttribute
from faker import Faker

import annotation_tool.users.factories
from . import lookups
from . import Entry

faker = Faker()
_ = lambda field, **kw: LazyAttribute(lambda __: field(**kw))


class EntryFactory(DjangoModelFactory):
    """Create empty pubmed entry for testing."""

    # noinspection PyDocstring
    class Meta:
        model = Entry

    pubmed_id = _(faker.random_int)
    user = SubFactory(annotation_tool.users.factories.UserFactory)

    gene = _(faker.text, max_nb_chars=100)
    structure = Iterator(lookups.StructureLookup.objects.all())
    mutation_type = Iterator(lookups.MutationTypeLookup.objects.all())
    syntax = Iterator(lookups.SyntaxLookup.objects.all())
    syntax_text = _(faker.text, max_nb_chars=100)
    operator = Iterator(lookups.OperatorLookup.objects.all())
    rule_level = Iterator(lookups.RuleLevelLookup.objects.all())
    chromosome = _(faker.text, max_nb_chars=100)
    start = _(faker.random_int)
    stop = _(faker.random_int)
    breakend_strand = Iterator(lookups.BreakendStrandLookup.objects.all())
    breakend_direction = Iterator(
        lookups.BreakendDirectionLookup.objects.all())
    mate_chromosome = _(faker.text, max_nb_chars=100)
    mate_start = _(faker.random_int)
    mate_end = _(faker.random_int)
    mate_breakend_strand = Iterator(
        lookups.BreakendStrandLookup.objects.all())
    minimum_number_of_copies = _(faker.random_int)
    maximum_number_of_copies = _(faker.random_int)
    coordinate_predicate = _(faker.text, max_nb_chars=100)
    partner_coordinate_predicate = _(faker.text, max_nb_chars=100)
    variant_type = Iterator(lookups.VariantTypeLookup.objects.all())
    variant_consequence = Iterator(
        lookups.VariantConsequenceLookup.objects.all())
    variant_clinical_grade = _(faker.random_int)
    # disease = lookups.ManyToManyField(DiseaseLookup,
    # **DEFAULTS.ManyToManyField)
    treatment_1 = _(faker.text, max_nb_chars=100)
    treatment_2 = _(faker.text, max_nb_chars=100)
    treatment_3 = _(faker.text, max_nb_chars=100)
    treatment_4 = _(faker.text, max_nb_chars=100)
    treatment_5 = _(faker.text, max_nb_chars=100)
    population_size = _(faker.random_int)
    sex = Iterator(lookups.SexLookup.objects.all())
    ethnicity = _(faker.text, max_nb_chars=100)
    # assessed_patient_outcomes = lookups.ManyToManyField(
    # AssessedPatientOutcomeLookup,
    #     **DEFAULTS.ManyToManyField)
    # significant_patient_outcomes = lookups.ManyToManyField(
    #     SignificantPatientOutcomeLookup, **DEFAULTS.ManyToManyField)
    design = _(faker.paragraphs)
    reference_claims = _(faker.paragraphs)
    comments = _(faker.paragraphs)
