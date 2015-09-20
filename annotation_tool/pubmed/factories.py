"""
Pubmed factory definitions.
"""

# Python Libraries
import logging

# Third Party Packages
from factory import DjangoModelFactory, Iterator, SubFactory
from faker import Faker


# Local Application
from . import lookups
from ..core.utils.factories import make, many_to_many
from ..users.factories import UserFactory

faker = Faker()

logger = logging.getLogger(__name__)


class EntryFactory(DjangoModelFactory):
    """Create empty pubmed entry for testing."""

    # noinspection PyDocstring
    class Meta:
        model = 'pubmed.Entry'

    pubmed_id = make(faker.random_int)
    user = SubFactory(UserFactory)

    gene = make(faker.text, max_nb_chars=100)
    structure = Iterator(lookups.StructureLookup.objects.all())
    mutation_type = Iterator(lookups.MutationTypeLookup.objects.all())
    syntax = Iterator(lookups.SyntaxLookup.objects.all())
    syntax_text = make(faker.text, max_nb_chars=100)
    operator = Iterator(lookups.OperatorLookup.objects.all())
    rule_level = Iterator(lookups.RuleLevelLookup.objects.all())
    chromosome = make(faker.text, max_nb_chars=100)
    start = make(faker.random_int)
    stop = make(faker.random_int)
    breakend_strand = Iterator(lookups.BreakendStrandLookup.objects.all())
    breakend_direction = Iterator(lookups.BreakendDirectionLookup.objects.all())
    mate_chromosome = make(faker.text, max_nb_chars=100)
    mate_start = make(faker.random_int)
    mate_end = make(faker.random_int)
    mate_breakend_strand = Iterator(lookups.BreakendStrandLookup.objects.all())
    minimum_number_of_copies = make(faker.random_int)
    maximum_number_of_copies = make(faker.random_int)
    coordinate_predicate = make(faker.text, max_nb_chars=100)
    partner_coordinate_predicate = make(faker.text, max_nb_chars=100)
    variant_type = Iterator(lookups.VariantTypeLookup.objects.all())
    variant_consequence = Iterator(lookups.VariantConsequenceLookup.objects.all())
    variant_clinical_grade = make(faker.random_int)
    disease = many_to_many(lookups.DiseaseLookup, 'disease')
    treatment_1 = make(faker.text, max_nb_chars=100)
    treatment_2 = make(faker.text, max_nb_chars=100)
    treatment_3 = make(faker.text, max_nb_chars=100)
    treatment_4 = make(faker.text, max_nb_chars=100)
    treatment_5 = make(faker.text, max_nb_chars=100)
    population_size = make(faker.random_int)
    sex = Iterator(lookups.SexLookup.objects.all())
    ethnicity = make(faker.text, max_nb_chars=100)
    assessed_patient_outcomes = many_to_many(lookups.PatientOutcomesLookup,
                                             'assessed_patient_outcomes')
    significant_patient_outcomes = many_to_many(lookups.PatientOutcomesLookup,
                                                'significant_patient_outcomes')
    design = make(faker.paragraph, nb_sentences=15)
    reference_claims = make(faker.paragraph, nb_sentences=15)
    comments = make(faker.paragraph, nb_sentences=15)
