# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Gene
from .serializers import GeneSerializer


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
