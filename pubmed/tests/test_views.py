#!/usr/bin/env python
# coding=utf-8

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from .. import views
from annotation_tool.utils import BaseTestCase, BaseCBVTestCase
from pubmed.factories import EntryFactory


# noinspection PyUnresolvedReferences
class EntryListViewTest(BaseCBVTestCase):
    view = views.EntryListView

    def test_normal_response_with_empty_list(self):
        response = self.assertGoodView(self.view)

        self.assertContains(response, 'Pubmed Entries')
        self.assertTemplateUsed(response, 'pubmed/entry_list.html')
        self.assertFalse(self.get_context('entry_list'))

    def test_normal_response_with_populated_list(self):
        entry = EntryFactory()

        self.assertGoodView(self.view)
        self.assertIn(entry, self.get_context('entry_list'))


# noinspection PyUnresolvedReferences
class EntryDetailViewTest(BaseCBVTestCase):
    view = views.EntryDetailView

    def test_normal_response(self):
        entry = EntryFactory()

        response = self.assertGoodView(self.view, pk=entry.pk)
        self.assertContains(response, 'Pubmed Entry')
        self.assertTemplateUsed(response, 'pubmed/entry_detail.html')

        self.assertEqual(entry, response.context_data['entry'])

    def test_not_found_response(self):
        with self.assertRaises(Http404), self.assertRaises(ObjectDoesNotExist):
            self.get(self.view, pk=1)
            self.response_404()


# noinspection PyUnresolvedReferences
class EntryCreateViewTest(BaseTestCase):
    url = 'pubmed:create'

    def test_with_logged_in_user(self):
        user = self.make_user()

        with self.login(user):
            response = self.assertGoodView(self.url)
        self.assertContains(response, 'Create Entry')
        self.assertTemplateUsed(response, 'pubmed/entry_form.html')

    def test_auth_required(self):
        self.assertLoginRequired(self.url)

    def test_with_anonymous_user(self):
        response = self.get(self.url)
        redirect_url = "%s?next=%s" % (
            self.reverse('account_login'), self.reverse(self.url))

        self.assertRedirects(response, redirect_url)


# noinspection PyUnresolvedReferences
class EntryUpdateViewTest(BaseTestCase):
    url = 'pubmed:update'

    def test_normal_response(self):
        entry = EntryFactory()

        response = self.assertGoodView(self.url, pk=entry.pk)
        self.assertContains(response, 'Pubmed Entry')
        self.assertTemplateUsed(response, 'pubmed/entry_form.html')
