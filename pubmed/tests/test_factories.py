import logging

from django.test import TestCase

from ..factories import EntryFactory
from pubmed.lookups import DiseaseLookup

logger = logging.getLogger(__name__)


class TestEntryFactory(TestCase):
    def test_factory_creates_entry(self):
        entry = EntryFactory()
        self.assertTrue(entry)

    def test_factory_entries_different(self):
        entry1 = EntryFactory()
        entry2 = EntryFactory()

        self.assertNotEqual(entry1, entry2)
        self.assertTrue(entry1.structure)
        self.assertNotEqual(entry1.pubmed_id, entry2.pubmed_id)

    def test_factories_populate_many_to_many_fields(self):
        self.assertGreater(DiseaseLookup.objects.count(), 1)
        entry1 = EntryFactory()

        self.assertGreater(entry1.disease.count(), 0)
        self.assertGreater(entry1.assessed_patient_outcomes.count(), 0)
        self.assertGreater(entry1.significant_patient_outcomes.count(), 0)
