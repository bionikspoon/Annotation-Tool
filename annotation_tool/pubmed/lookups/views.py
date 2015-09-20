# Third Party Packages
from rest_framework.viewsets import ReadOnlyModelViewSet

# Local Application
from . import models, serializers


class LookupTableViewSet(ReadOnlyModelViewSet):
    pass


class StructureLookupViewSet(LookupTableViewSet):
    queryset = models.StructureLookup.objects.all()
    serializer_class = serializers.StructureLookupSerializer


class MutationTypeLookupViewSet(LookupTableViewSet):
    queryset = models.MutationTypeLookup.objects.all()
    serializer_class = serializers.MutationTypeLookupSerializer


class SyntaxLookupViewSet(LookupTableViewSet):
    queryset = models.SyntaxLookup.objects.all()
    serializer_class = serializers.SyntaxLookupSerializer


class OperatorLookupViewSet(LookupTableViewSet):
    queryset = models.OperatorLookup.objects.all()
    serializer_class = serializers.OperatorLookupSerializer


class RuleLevelLookupViewSet(LookupTableViewSet):
    queryset = models.RuleLevelLookup.objects.all()
    serializer_class = serializers.RuleLevelLookupSerializer


class BreakendStrandLookupViewSet(LookupTableViewSet):
    queryset = models.BreakendStrandLookup.objects.all()
    serializer_class = serializers.BreakendStrandLookupSerializer


class BreakendDirectionLookupViewSet(LookupTableViewSet):
    queryset = models.BreakendDirectionLookup.objects.all()
    serializer_class = serializers.BreakendDirectionLookupSerializer


class VariantTypeLookupViewSet(LookupTableViewSet):
    queryset = models.VariantTypeLookup.objects.all()
    serializer_class = serializers.VariantTypeLookupSerializer


class VariantConsequenceLookupViewSet(LookupTableViewSet):
    queryset = models.VariantConsequenceLookup.objects.all()
    serializer_class = serializers.VariantConsequenceLookupSerializer


class SexLookupViewSet(LookupTableViewSet):
    queryset = models.SexLookup.objects.all()
    serializer_class = serializers.SexLookupSerializer


class DiseaseLookupViewSet(LookupTableViewSet):
    queryset = models.DiseaseLookup.objects.all()
    serializer_class = serializers.DiseaseLookupSerializer


class PatientOutcomesLookupViewSet(LookupTableViewSet):
    queryset = models.PatientOutcomesLookup.objects.all()
    serializer_class = serializers.PatientOutcomesLookupSerializer
