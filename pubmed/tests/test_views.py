#!/usr/bin/env python
# coding=utf-8

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from .. import views, factories
from annotation_tool.utils import BaseTestCase, BaseCBVTestCase


class EntryListViewTest(BaseCBVTestCase):
    view = views.EntryListView

    def test_normal_response_with_empty_list(self):
        response = self.assertGoodView(self.view)

        self.assertContains(response, 'Pubmed Entries')
        self.assertTemplateUsed(response, 'pubmed/entry_list.html')
        self.assertFalse(self.get_context('entry_list'))

    def test_normal_response_with_populated_list(self):
        entry = factories.EntryFactory()

        self.assertGoodView(self.view)
        self.assertIn(entry, self.get_context('entry_list'))


class EntryDetailViewTest(BaseCBVTestCase):
    view = views.EntryDetailView

    def test_normal_response(self):
        entry = factories.EntryFactory()

        response = self.assertGoodView(self.view, pk=entry.pk)
        self.assertContains(response, 'Pubmed Entry')
        self.assertTemplateUsed(response, 'pubmed/entry_detail.html')

        self.assertEqual(entry, response.context_data['entry'])

    def test_not_found_response(self):
        with self.assertRaises(Http404), self.assertRaises(ObjectDoesNotExist):
            self.get(self.view, pk=1)
            self.response_404()


# noinspection PyUnresolvedReferences
class EntryFormMixin(object):
    url = NotImplemented
    action = NotImplemented
    entry = NotImplemented
    user = NotImplemented
    data_url = NotImplemented
    template = 'pubmed/entry_form.html'
    data = {'data': {'pubmed_id': 1}}

    def setUp(self):
        self.user = self.make_user()
        self.data_url = dict(self.url, **self.data)

    def test_auth_required(self):
        """Test login required."""
        self.assertLoginRequired(**self.url)

    def test_without_logged_in_user(self):
        """Test template is not even accessed for anonymous users"""
        response = self.get(**self.url)

        self.response_302()
        self.assertTemplateNotUsed(response, self.template)

    def test_with_logged_in_user(self):
        """Test view works with auth user."""

        with self.login(self.user):
            response = self.assertGoodView(**self.url)
        self.assertContains(response, '%s Entry' % self.action)
        self.assertTemplateUsed(response, self.template)
        self.assertContext('action_text', self.action)

    def test_without_logged_in_user__post_with_data(self):
        self.post(**self.data_url)
        self.response_403()

    def test_with_logged_in_user__post_with_data(self):
        with self.login(self.user):
            self.post(**self.data_url)
        self.response_201()

    def test_with_logged_in_user__post_without_data(self):
        with self.login(self.user):
            self.post(**self.url)
        self.response_302()


class EntryCreateViewTest(EntryFormMixin, BaseTestCase):
    url = {'url_name': 'pubmed:create'}
    action = 'Create'


class EntryUpdateViewTest(EntryFormMixin, BaseTestCase):
    entry = factories.EntryFactory()
    url = {'url_name': 'pubmed:update', 'pk': entry.pk}
    action = 'Update'

    def setUp(self):
        self.entry.save()
        super().setUp()
