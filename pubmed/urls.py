"""
Pubmed url definitions.
"""

# Django Packages
from django.conf.urls import url

# Local Application
from .views import EntryCreateView, EntryDetailView, EntryListView, EntryUpdateView

urlpatterns = [

    url(r'^$', EntryListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', EntryDetailView.as_view(), name='detail'),
    url(r'^new/$', EntryCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', EntryUpdateView.as_view(), name='update'),

]
