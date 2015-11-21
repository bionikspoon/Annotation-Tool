#!/usr/bin/env python
# coding=utf-8
from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from annotation_tool.pubmed.views import (PubmedViewSet, MutationTypeViewSet, SyntaxViewSet, RuleLevelViewSet,
    VariantTypeViewSet, VariantConsequenceViewSet, DiseaseViewSet, PatientOutcomesViewSet)
from annotation_tool.pubmed.views import StructureViewSet
from annotation_tool.users.views import UserViewSet, ProfileRetrieveAPIView

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('pubmed', PubmedViewSet)
# router.register('genes', GeneViewSet)
router.register('lookup-structure', StructureViewSet)
router.register('lookup-mutation-type', MutationTypeViewSet)
router.register('lookup-syntax', SyntaxViewSet)
router.register('lookup-rule-level', RuleLevelViewSet)
router.register('lookup-variant-type', VariantTypeViewSet)
router.register('lookup-variant-consequence', VariantConsequenceViewSet)
router.register('lookup-disease', DiseaseViewSet)
router.register('lookup-patient-outcomes', PatientOutcomesViewSet)

urlpatterns = [  # :off
    url(r'^', include(router.urls)),
    url(r'^auth/login/', obtain_jwt_token),
    url(r'^auth/refresh/', refresh_jwt_token),
    url(r'^auth/verify/', verify_jwt_token),
    url(r'^auth/profile/', ProfileRetrieveAPIView.as_view()),
]  # :on
