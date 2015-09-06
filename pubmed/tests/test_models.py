#!/usr/bin/env python
# coding=utf-8

# Python Libraries
import logging

# Django Packages
from django.test import TestCase

# Annotation Tool Project
from pubmed import EntryMeta
from pubmed.factories import EntryFactory

logger = logging.getLogger(__name__)


class EntryModelTestCase(TestCase):
    def setUp(self):
        self.entry = EntryFactory()

    def test_entry_absulate_url_resolves_entry_instance(self):
        self.assertEqual(self.entry.get_absolute_url(),
                         '/pubmed/%s/' % self.entry.pk)

    def test_str_representation_joins_id_pubmed_and_gene(self):
        self.assertEqual(str(self.entry), "%s:%s:%s" % (
            self.entry.pubmed_id, self.entry.pk, self.entry.gene,))


class EntryMetaTestCase(TestCase):
    def test_all_fields_property(self):
        expected_tuple = (

            'id', 'created', 'modified', 'user', 'pubmed_id', 'gene',
            'structure', 'mutation_type', 'syntax', 'syntax_text', 'operator',
            'rule_level', 'chromosome', 'start', 'stop', 'breakend_strand',
            'breakend_direction', 'mate_chromosome', 'mate_start', 'mate_end',
            'mate_breakend_strand', 'mate_breakend_direction',
            'minimum_number_of_copies', 'maximum_number_of_copies',
            'coordinate_predicate', 'partner_coordinate_predicate',
            'variant_type', 'variant_consequence', 'variant_clinical_grade',
            'disease', 'treatment_1', 'treatment_2', 'treatment_3',
            'treatment_4', 'treatment_5', 'population_size', 'sex', 'ethnicity',
            'assessed_patient_outcomes', 'significant_patient_outcomes',
            'design', 'reference_claims', 'comments'

        )
        self.assertTupleEqual(EntryMeta.all_fields, expected_tuple)

    def test_relationship_fields_property(self):
        expected_tuple = (

            'user', 'structure', 'mutation_type', 'syntax', 'operator',
            'rule_level', 'breakend_strand', 'breakend_direction',
            'mate_breakend_strand', 'mate_breakend_direction', 'variant_type',
            'variant_consequence', 'disease', 'sex',
            'assessed_patient_outcomes', 'significant_patient_outcomes'

        )
        self.assertTupleEqual(EntryMeta.relationship_fields, expected_tuple)

    def test_foreign_fields_property(self):
        expected_tuple = (

            'user', 'structure', 'mutation_type', 'syntax', 'operator',
            'rule_level', 'breakend_strand', 'breakend_direction',
            'mate_breakend_strand', 'mate_breakend_direction', 'variant_type',
            'variant_consequence', 'sex'

        )
        self.assertTupleEqual(EntryMeta.foreign_fields, expected_tuple)

    def test_many_to_many_fields_property(self):
        expected_tuple = (

            'disease', 'assessed_patient_outcomes',
            'significant_patient_outcomes'

        )
        self.assertTupleEqual(EntryMeta.many_to_many_fields, expected_tuple)

    def test_text_fields_property(self):
        expected_tuple = (

            'gene', 'syntax_text', 'chromosome', 'mate_chromosome',
            'coordinate_predicate', 'partner_coordinate_predicate',
            'treatment_1', 'treatment_2', 'treatment_3', 'treatment_4',
            'treatment_5', 'ethnicity', 'design', 'reference_claims', 'comments'

        )
        self.assertTupleEqual(EntryMeta.text_fields, expected_tuple)

    def test_int_fields_property(self):
        expected_tuple = (

            'pubmed_id', 'start', 'stop', 'mate_start', 'mate_end',
            'minimum_number_of_copies', 'maximum_number_of_copies',
            'variant_clinical_grade', 'population_size'

        )
        self.assertTupleEqual(EntryMeta.int_fields, expected_tuple)

    def test_public_fields_property(self):
        expected_tuple = (

            'pubmed_id', 'gene', 'structure', 'mutation_type', 'syntax',
            'syntax_text', 'operator', 'rule_level', 'chromosome', 'start',
            'stop', 'breakend_strand', 'breakend_direction', 'mate_chromosome',
            'mate_start', 'mate_end', 'mate_breakend_strand',
            'mate_breakend_direction', 'minimum_number_of_copies',
            'maximum_number_of_copies', 'coordinate_predicate',
            'partner_coordinate_predicate', 'variant_type',
            'variant_consequence', 'variant_clinical_grade', 'disease',
            'treatment_1', 'treatment_2', 'treatment_3', 'treatment_4',
            'treatment_5', 'population_size', 'sex', 'ethnicity',
            'assessed_patient_outcomes', 'significant_patient_outcomes',
            'design', 'reference_claims', 'comments'

        )
        self.assertTupleEqual(EntryMeta.public_fields, expected_tuple)

    def test_summary_fields_property(self):
        expected_tuple = (

            'modified', 'user', 'gene', 'structure', 'mutation_type', 'syntax',
            'syntax_text', 'operator', 'rule_level'

        )
        self.assertTupleEqual(EntryMeta.summary_fields, expected_tuple)
