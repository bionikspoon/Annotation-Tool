# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from .models import (Pubmed, StructureLookup, MutationTypeLookup, SyntaxLookup, RuleLevelLookup, VariantTypeLookup,
    VariantConsequenceLookup, DiseaseLookup, PatientOutcomesLookup)
from .serializers import (PubmedSerializer, DiseaseSerializer, VariantConsequenceSerializer, VariantTypeSerializer,
    RuleLevelSerializer, PatientOutcomesSerializer, StructureSerializer, MutationTypeSerializer, SyntaxSerializer)


class StructureViewSet(viewsets.ModelViewSet):
    queryset = StructureLookup.objects.all()
    serializer_class = StructureSerializer


class MutationTypeViewSet(viewsets.ModelViewSet):
    queryset = MutationTypeLookup.objects.all()
    serializer_class = MutationTypeSerializer


class SyntaxViewSet(viewsets.ModelViewSet):
    queryset = SyntaxLookup.objects.all()
    serializer_class = SyntaxSerializer


class RuleLevelViewSet(viewsets.ModelViewSet):
    queryset = RuleLevelLookup.objects.all()
    serializer_class = RuleLevelSerializer


class VariantTypeViewSet(viewsets.ModelViewSet):
    queryset = VariantTypeLookup.objects.all()
    serializer_class = VariantTypeSerializer


class VariantConsequenceViewSet(viewsets.ModelViewSet):
    queryset = VariantConsequenceLookup.objects.all()
    serializer_class = VariantConsequenceSerializer


class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = DiseaseLookup.objects.all()
    serializer_class = DiseaseSerializer


class PatientOutcomesViewSet(viewsets.ModelViewSet):
    queryset = PatientOutcomesLookup.objects.all()
    serializer_class = PatientOutcomesSerializer


class PubmedViewSet(viewsets.ModelViewSet):
    queryset = Pubmed.objects.prefetch_related('disease', 'assessed_patient_outcomes',
                                               'significant_patient_outcomes').all()
    serializer_class = PubmedSerializer
    # permission_classes = (DjangoModelPermissions,)
