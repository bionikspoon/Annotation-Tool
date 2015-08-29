#!/usr/bin/env python
# coding=utf-8
from django.conf.urls import url, include

from .views import *

api_urlpatterns = [

    url(r'^$', EntryListCreateView.as_view(), name='entry_rest_api'),
    url(r'^(?P<pk>\d+)/$', EntryReadUpdateDeleteView.as_view(),
        name='entry_rest_api'),

]

urlpatterns = [

    url(r'^$', EntryListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', EntryDetailView.as_view(), name='detail'),
    url(r'^new/$', EntryCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit$', EntryUpdateView.as_view(), name='update'),

]
