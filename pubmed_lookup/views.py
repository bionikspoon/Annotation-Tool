from rest_framework.viewsets import ModelViewSet
from pubmed_lookup.models import *
from pubmed_lookup.serializers import *


class LookupTableViewSet(ModelViewSet):
    pass


class StructureLookupViewSet(LookupTableViewSet):
    queryset = StructureLookup.objects.all()
    serializer_class = StructureLookupSerializer


class MutationTypeLookupViewSet(LookupTableViewSet):
    queryset = MutationTypeLookup.objects.all()
    serializer_class = MutationTypeLookupSerializer


class SyntaxLookupViewSet(LookupTableViewSet):
    queryset = SyntaxLookup.objects.all()
    serializer_class = SyntaxLookupSerializer


class OperatorLookupViewSet(LookupTableViewSet):
    queryset = OperatorLookup.objects.all()
    serializer_class = OperatorLookupSerializer


class RuleLevelLookupViewSet(LookupTableViewSet):
    queryset = RuleLevelLookup.objects.all()
    serializer_class = RuleLevelLookupSerializer


class BreakendStrandLookupViewSet(LookupTableViewSet):
    queryset = BreakendStrandLookup.objects.all()
    serializer_class = BreakendStrandLookupSerializer


class BreakendDirectionLookupViewSet(LookupTableViewSet):
    queryset = BreakendDirectionLookup.objects.all()
    serializer_class = BreakendDirectionLookupSerializer


class VariantTypeLookupViewSet(LookupTableViewSet):
    queryset = VariantTypeLookup.objects.all()
    serializer_class = VariantTypeLookupSerializer


class VariantConsequenceLookupViewSet(LookupTableViewSet):
    queryset = VariantConsequenceLookup.objects.all()
    serializer_class = VariantConsequenceLookupSerializer


class SexLookupViewSet(LookupTableViewSet):
    queryset = SexLookup.objects.all()
    serializer_class = SexLookupSerializer


class DiseaseLookupViewSet(LookupTableViewSet):
    queryset = DiseaseLookup.objects.all()
    serializer_class = DiseaseLookupSerializer


class PatientOutcomesLookupViewSet(LookupTableViewSet):
    queryset = PatientOutcomesLookup.objects.all()
    serializer_class = PatientOutcomesLookupSerializer
