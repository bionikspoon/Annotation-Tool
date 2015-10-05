# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from .models import (Pubmed, StructureLookup, MutationTypeLookup, SyntaxLookup, RuleLevelLookup, VariantTypeLookup,
                     VariantConsequenceLookup, DiseaseLookup, PatientOutcomesLookup, Gene)
from .serializers import (PubmedSerializer, DiseaseSerializer, VariantConsequenceSerializer, VariantTypeSerializer,
                          RuleLevelSerializer, PatientOutcomesSerializer, StructureSerializer, MutationTypeSerializer,
                          SyntaxSerializer, GeneSerializer)


class GeneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer

    def list(self, request, *args, **kwargs):
        # TODO remove limit, add pagination
        queryset = self.filter_queryset(self.get_queryset())[:100]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
