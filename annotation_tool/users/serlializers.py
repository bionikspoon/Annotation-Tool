

from rest_framework.relations import HyperlinkedIdentityField, \
    HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    pubmed_entries = HyperlinkedRelatedField(view_name='entry-detail',
                                             read_only=True, many=True)
    url = HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email',
                  'date_joined', 'name', 'pubmed_entries')
