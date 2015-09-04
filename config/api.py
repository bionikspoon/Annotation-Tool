#!/usr/bin/env python
# coding=utf-8
"""
Build API router.
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from annotation_tool.users.views import UserViewSet
from pubmed.views import EntryViewSet
from pubmed_lookup import views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'pubmed', EntryViewSet)

router.register(r'lookup/structurelookup', views.StructureLookupViewSet,
                base_name='structurelookup')
router.register(r'lookup/mutationtypelookup', views.MutationTypeLookupViewSet,
                base_name='mutationtypelookup')
router.register(r'lookup/syntaxlookup', views.SyntaxLookupViewSet,
                base_name='syntaxlookup')
router.register(r'lookup/operatorlookup', views.OperatorLookupViewSet,
                base_name='operatorlookup')
router.register(r'lookup/rulelevellookup', views.RuleLevelLookupViewSet,
                base_name='rulelevellookup')
router.register(r'lookup/breakendstrandlookup',
                views.BreakendStrandLookupViewSet,
                base_name='breakendstrandlookup')
router.register(r'lookup/breakenddirectionlookup',
                views.BreakendDirectionLookupViewSet,
                base_name='breakenddirectionlookup')
router.register(r'lookup/varianttypelookup', views.VariantTypeLookupViewSet,
                base_name='varianttypelookup')
router.register(r'lookup/variantconsequencelookup',
                views.VariantConsequenceLookupViewSet,
                base_name='variantconsequencelookup')
router.register(r'lookup/sexlookup', views.SexLookupViewSet,
                base_name='sexlookup')
router.register(r'lookup/diseaselookup', views.DiseaseLookupViewSet,
                base_name='diseaselookup')
router.register(r'lookup/patientoutcomeslookup',
                views.PatientOutcomesLookupViewSet,
                base_name='patientoutcomeslookup')
urlpatterns = [

    url(r'^', include(router.urls)),

]
