#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from annotation_tool.users.views import UserViewSet
from pubmed import views
from pubmed.views import EntryViewSet





router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'pubmed', EntryViewSet)

lookup_router = DefaultRouter()

lookup_router.register(r'structurelookup', views.StructureLookupViewSet)
lookup_router.register(r'mutationtypelookup', views.MutationTypeLookupViewSet)
lookup_router.register(r'syntaxlookup', views.SyntaxLookupViewSet)
lookup_router.register(r'operatorlookup', views.OperatorLookupViewSet)
lookup_router.register(r'rulelevellookup', views.RuleLevelLookupViewSet)
lookup_router.register(r'breakendstrandlookup', views.BreakendStrandLookupViewSet)
lookup_router.register(r'breakenddirectionlookup',
                       views.BreakendDirectionLookupViewSet)
lookup_router.register(r'varianttypelookup', views.VariantTypeLookupViewSet)
lookup_router.register(r'variantconsequencelookup',
                       views.VariantConsequenceLookupViewSet)
lookup_router.register(r'sexlookup', views.SexLookupViewSet)
lookup_router.register(r'diseaselookup', views.DiseaseLookupViewSet)
# lookup_router.register(r'patientoutcomelookup', views.PatientOutcomesLookupViewSet)
router.register(r'lookup', lookup_router.get_api_root_view, base_name='lookup')
urlpatterns = [

    url(r'^', include(router.urls)),

    url(r'^lookup/', include(lookup_router.urls))

]
