#!/usr/bin/env python
# coding=utf-8

import logging

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from test_plus import TestCase
from test_plus.test import CBVTestCase

from .. import views, factories
from core.utils.test import BaseTestMixin

logger = logging.getLogger(__name__)


class EntryListViewTest(BaseTestMixin, CBVTestCase):
    view = views.EntryListView

    def test_get_list_view__with_no_items(self):
        response = self.assertGoodView(self.view)

        self.assertContains(response, 'Pubmed Entries')
        self.assertTemplateUsed(response, 'pubmed/entry_list.html')
        self.assertFalse(self.get_context('entry_list'))

    def test_get_list_view__with_many_items(self):
        entry = factories.EntryFactory()

        self.assertGoodView(self.view)
        self.assertIn(entry, self.get_context('entry_list'))


class EntryDetailViewTest(BaseTestMixin, CBVTestCase):
    view = views.EntryDetailView

    def test_get_detail_view__with_one_item(self):
        entry = factories.EntryFactory()

        response = self.assertGoodView(self.view, pk=entry.pk)
        self.assertContains(response, 'Pubmed Entry')
        self.assertTemplateUsed(response, 'pubmed/entry_detail.html')

        self.assertEqual(entry, response.context_data['entry'])

    def ttest_get_detail_view__with_no_items(self):
        with self.assertRaises(Http404), self.assertRaises(ObjectDoesNotExist):
            self.get(self.view, pk=1)
            self.response_404()


# noinspection PyUnresolvedReferences
class EntryFormMixin(object):
    post_to_url = NotImplemented
    expected_action = NotImplemented
    entry = NotImplemented
    user = NotImplemented
    data_url = NotImplemented
    template = 'pubmed/entry_form.html'
    data = {
        'data': {
            'pubmed_id': 1
        }
    }

    def setUp(self):
        self.user = self.make_user()
        self.data_url = dict(self.post_to_url, **self.data)

    def test_auth_required(self):
        """Test login required."""
        self.assertLoginRequired(**self.post_to_url)

    def test_get_form__logged_in_user(self):
        """Test view works with auth user."""

        with self.login(self.user):
            response = self.assertGoodView(**self.post_to_url)
        self.assertContains(response, '%s Entry' % self.expected_action)
        self.assertTemplateUsed(response, self.template)
        self.assertContext('action_text', self.expected_action)
        self.response_200()

    def test_get_form__anonymous_in_user(self):
        """Test template is not even accessed for anonymous users"""
        response = self.get(**self.post_to_url)

        self.response_302()
        self.assertTemplateNotUsed(response, self.template)

    def test_post_form__logged_in_user__data(self):
        """Test data is posted if user is logged in."""
        with self.login(self.user):
            response = self.post(**self.data_url)
        logger.debug(response)
        self.response_200()

    def test_post_form__logged_in_user__no_data(self):
        """Test form error displayed when posted with empty data."""
        with self.login(self.user):
            response = self.post(**self.post_to_url)
        self.response_200()
        self.assertFormError(response, 'form', 'pubmed_id',
                             'This field is required.')

    def test_post_form__anonymous_user__data(self):
        """Test 401 response if posted from anonymous user."""
        self.post(**self.data_url)
        self.response_401()


class EntryCreateViewTest(EntryFormMixin, BaseTestMixin, TestCase):
    post_to_url = {
        'url_name': 'pubmed:create'
    }
    expected_action = 'Create'


class EntryUpdateViewTest(EntryFormMixin, BaseTestMixin, TestCase):
    entry = factories.EntryFactory()
    post_to_url = {
        'url_name': 'pubmed:update',
        'pk': entry.pk
    }
    expected_action = 'Update'

    def setUp(self):
        self.entry.save()
        super().setUp()
