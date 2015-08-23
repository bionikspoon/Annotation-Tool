#!/usr/bin/env python
# coding=utf-8
from django.conf.urls import url

from . import views
urlpatterns = [

    url(regex=r'^$', view=views.EntryListView.as_view(), name='list'),
    url(regex=r'^(?P<pk>\d+)/$', view=views.EntryDetailView.as_view(),
        name='detail'),
    url(regex=r'^new/$', view=views.EntryCreateView.as_view(), name='create'),
    url(regex=r'^(?P<pk>\d+)/edit$', view=views.EntryUpdateView.as_view(),
        name='update'),

]

