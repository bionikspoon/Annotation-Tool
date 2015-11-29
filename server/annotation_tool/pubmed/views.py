from rest_framework.filters import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet

from .filters import IncludeOrExcludeIdFilterBackend
from .models import (Pubmed, StructureLookup, MutationTypeLookup, SyntaxLookup, RuleLevelLookup, VariantTypeLookup,
                     VariantConsequenceLookup, DiseaseLookup, PatientOutcomesLookup)
from .serializers import (PubmedSerializer, DiseaseSerializer, VariantConsequenceSerializer, VariantTypeSerializer,
                          RuleLevelSerializer, PatientOutcomesSerializer, StructureSerializer, MutationTypeSerializer,
                          SyntaxSerializer)


class StructureViewSet(ModelViewSet):
    queryset = StructureLookup.objects.all()
    serializer_class = StructureSerializer


class MutationTypeViewSet(ModelViewSet):
    queryset = MutationTypeLookup.objects.all()
    serializer_class = MutationTypeSerializer


class SyntaxViewSet(ModelViewSet):
    queryset = SyntaxLookup.objects.all()
    serializer_class = SyntaxSerializer


class RuleLevelViewSet(ModelViewSet):
    queryset = RuleLevelLookup.objects.all()
    serializer_class = RuleLevelSerializer


class VariantTypeViewSet(ModelViewSet):
    queryset = VariantTypeLookup.objects.all()
    serializer_class = VariantTypeSerializer


class VariantConsequenceViewSet(ModelViewSet):
    queryset = VariantConsequenceLookup.objects.all()
    serializer_class = VariantConsequenceSerializer


class DiseaseViewSet(ModelViewSet):
    queryset = DiseaseLookup.objects.all()
    serializer_class = DiseaseSerializer


class PatientOutcomesViewSet(ModelViewSet):
    queryset = PatientOutcomesLookup.objects.all()
    serializer_class = PatientOutcomesSerializer


class PubmedViewSet(ModelViewSet):
    queryset = Pubmed.objects.prefetch_related('disease', 'assessed_patient_outcomes', 'significant_patient_outcomes',
                                               'user').all()
    serializer_class = PubmedSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (DjangoFilterBackend, IncludeOrExcludeIdFilterBackend)
    filter_fields = ('pubmed_id',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
