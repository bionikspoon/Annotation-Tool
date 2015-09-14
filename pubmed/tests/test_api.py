from core.utils.test import BaseAPITestCase
from pubmed.factories import EntryFactory


class PubmedListAPITestCase(BaseAPITestCase):
    def test_api_returns_an_empty_list__no_data(self):
        self.get('/api/pubmed/')
        self.assertEqual(self.data, [])
        self.assertEqual(len(self.data), 0)

    def test_api_returns_a_list_of_entries__single_entry(self):
        EntryFactory()

        with self.assertNumQueries(4):
            self.get('/api/pubmed/')
        self.assertEqual(len(self.data), 1)

    def test_api_returns_a_list_of_entries__multiple_entries(self):
        for _ in range(10):
            EntryFactory()
        with self.assertNumQueries(4):
            self.get('/api/pubmed/')
        self.assertEqual(len(self.data), 10)

    def test_depth_is_zero(self):
        EntryFactory()

        self.get('/api/pubmed/')
        entry = self.data[0]

        self.assertIsInstance(entry['user'], str)

        # Is a hyperlink to `users` api.
        self.assertTrue(entry['user'].startswith(self.url('api/users')))

        # A unique case for safe keeping(foreign key with multiple relations)
        self.assertIsInstance(entry['mate_breakend_strand'], str)

        # Many to many field.
        self.assertIsInstance(entry['disease'], list)
        # Factory should guarantee at least one related item.
        self.assertIsInstance(entry['disease'][0], str)
        self.assertTrue(entry['disease'][0].startswith(self.url('api/lookup/diseaselookup')))

    def test_entry_includes_link_to_self(self):
        EntryFactory()

        self.get('/api/pubmed/')
        entry = self.data[0]

        self.assertTrue(entry['url'].startswith(self.url('api/pubmed')))
