"""
Build API router.
"""

# Django Packages
from django.conf.urls import include, url

# Third Party Packages
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSet

# Annotation Tool Project
from annotation_tool.pubmed.views import EntryViewSet
from annotation_tool.users.views import UserViewSet
from annotation_tool.pubmed import lookups

lookup_router = DefaultRouter()
lookup_router.register(r'structurelookup', lookups.StructureLookupViewSet,
                       base_name='structurelookup')
lookup_router.register(r'mutationtypelookup', lookups.MutationTypeLookupViewSet,
                       base_name='mutationtypelookup')
lookup_router.register(r'syntaxlookup', lookups.SyntaxLookupViewSet, base_name='syntaxlookup')
lookup_router.register(r'operatorlookup', lookups.OperatorLookupViewSet, base_name='operatorlookup')
lookup_router.register(r'rulelevellookup', lookups.RuleLevelLookupViewSet,
                       base_name='rulelevellookup')
lookup_router.register(r'breakendstrandlookup', lookups.BreakendStrandLookupViewSet,
                       base_name='breakendstrandlookup')
lookup_router.register(r'breakenddirectionlookup', lookups.BreakendDirectionLookupViewSet,
                       base_name='breakenddirectionlookup')
lookup_router.register(r'varianttypelookup', lookups.VariantTypeLookupViewSet,
                       base_name='varianttypelookup')
lookup_router.register(r'variantconsequencelookup', lookups.VariantConsequenceLookupViewSet,
                       base_name='variantconsequencelookup')
lookup_router.register(r'sexlookup', lookups.SexLookupViewSet, base_name='sexlookup')
lookup_router.register(r'diseaselookup', lookups.DiseaseLookupViewSet, base_name='diseaselookup')
lookup_router.register(r'patientoutcomeslookup', lookups.PatientOutcomesLookupViewSet,
                       base_name='patientoutcomeslookup')


class GenericListViewSet(ViewSet):
    def list(self, requst, *args, **kwargs):
        pass


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'pubmed', EntryViewSet)
router.register(r'lookup', GenericListViewSet, base_name='lookup')

urlpatterns = [

    url(r'^lookup/', include(lookup_router.urls)),

    url(r'^', include(router.urls)),

]
