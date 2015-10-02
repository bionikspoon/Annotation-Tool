# Create your views here.
from rest_framework import viewsets

from .models import Pubmed
from .serializers import PubmedSerializer


class PubmedViewSet(viewsets.ModelViewSet):
    queryset = Pubmed.objects.all()
    serializer_class = PubmedSerializer
