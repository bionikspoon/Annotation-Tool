from ...core.utils.test import BaseAPITestCase
from ..factories import EntryFactory


class PubmedListAPITestCase(BaseAPITestCase):
    PATH = '/api/pubmed/'

    def test_api_returns_an_empty_list__no_data(self):
        self.get()
        self.assertEqual(self.data, [])
        self.assertEqual(len(self.data), 0)

    def test_api_returns_a_list_of_entries__single_entry(self):
        EntryFactory()

        with self.assertNumQueries(4):
            self.get()
        self.assertEqual(len(self.data), 1)

    def test_api_returns_a_list_of_entries__multiple_entries(self):
        for _ in range(10):
            EntryFactory()
        with self.assertNumQueries(4):
            self.get()
        self.assertEqual(len(self.data), 10)

    def test_depth_is_zero(self):
        EntryFactory()

        self.get()
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

        self.get()
        entry = self.data[0]

        self.assertTrue(entry['url'].startswith(self.url('api/pubmed')))

    def test_api_readonly(self):
        payload = {
            'pubmed_id': 100
        }
        self.post(data=payload)
        self.assert_405()

        self.put(data=payload)
        self.assert_405()

        self.patch(data=payload)
        self.assert_405()

        self.delete(data=payload)
        self.assert_405()

        self.delete(data=payload)
        self.assert_405()


class PubmedRetreiveAPITestCase(BaseAPITestCase):
    PATH = '/api/pubmed/%s/'

    def test_api_returns_404_not_found__no_data(self):
        self.get()
        self.assert_404()

    def test_api_returns_a_single_item(self):
        entry = EntryFactory()

        self.get(pk=entry.pk)

        self.assertEqual(len(self.data), 43)
        self.assert_200()

    def test_results_have_depth_1(self):
        entry = EntryFactory()

        self.get(pk=entry.pk)

        self.assertTrue(self.data['user']['url'].startswith(self.url('api/users')))
        self.assertTrue(
            self.data['disease'][0]['url'].startswith(self.url('api/lookup/diseaselookup')))

    def test_efficient_orm_usage(self):
        entry = EntryFactory()

        # 4: 1 SELECT * with joins, 1 each many to many relationship(3).
        with self.assertNumQueries(4):
            self.get(pk=entry.pk)
