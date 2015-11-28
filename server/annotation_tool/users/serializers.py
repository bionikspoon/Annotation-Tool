from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from .models import User
from ..pubmed.models import PUBMED_ENTRIES


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = 'url', 'username', 'name', PUBMED_ENTRIES


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'username', 'email', 'name', 'groups', 'get_all_permissions', 'is_superuser'
