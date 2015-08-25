#!/usr/bin/env python
# coding=utf-8

from django.test import TestCase, RequestFactory
from ..views import EntryListView


class EntryListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_list_view(self):
        request = self.factory.get('/pubmed/')
        response = EntryListView.as_view()(request)

        self.assertContains(response, 'Pubmed Entries')
        self.assertIn('pubmed/entry_list.html', response.template_name)
