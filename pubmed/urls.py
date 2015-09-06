#!/usr/bin/env python
# coding=utf-8
"""
Pubmed url definitions.
"""
from django.conf.urls import url

from .views import *

urlpatterns = [

    url(r'^$', EntryListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', EntryDetailView.as_view(), name='detail'),
    url(r'^new/$', EntryCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', EntryUpdateView.as_view(), name='update'),

]
