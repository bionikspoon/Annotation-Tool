#!/usr/bin/env python
# coding=utf-8
from django.core.urlresolvers import reverse
from django.test import TestCase, SimpleTestCase

from .. import models
from annotation_tool.users.models import User


class EntryListViewTest(SimpleTestCase):
    url = reverse('pubmed:list')

    def test_normal_response_with_empty_list(self):
        response = self.client.get(self.url)
        entry_list = response.context_data['entry_list']

        self.assertContains(response, 'Pubmed Entries')
        self.assertIn('pubmed/entry_list.html', response.template_name)
        self.assertFalse(entry_list)
        self.assertIs(type(entry_list.model), type(models.Entry))

    def test_normal_response_with_populated_list(self):
        user = User.objects.create_user('Jerry')
        entry = models.Entry.objects.create(pubmed_id=1234, user=user)

        response = self.client.get(self.url)
        entry_list = response.context_data['entry_list']

        self.assertIn(entry, entry_list)


class EntryDetailViewTest(TestCase):
    def test_normal_response(self):
        user = User.objects.create_user('Jerry')
        entry = models.Entry.objects.create(pubmed_id=1234, user=user)
        url = reverse('pubmed:detail', kwargs={'pk': entry.pk})

        response = self.client.get(url)
        self.assertContains(response, 'Pubmed Entry')
        self.assertIn('pubmed/entry_detail.html', response.template_name)
        self.assertEqual(entry, response.context_data['entry'])
