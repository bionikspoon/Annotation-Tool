"""
Serialize Pubmed objects.
"""

from rest_framework.serializers import HyperlinkedModelSerializer

from annotation_tool.users.serlializers import UserSerializer
from .models import EntryMeta


class EntryUserSerializer(UserSerializer):
    """
    Remove `pubmed_entries` from User serializer.
    """

    # noinspection PyDocstring
    class Meta(UserSerializer.Meta):
        fields = tuple(field for field in UserSerializer.Meta.fields if
                       field != 'pubmed_entries')


class EntrySerializer(HyperlinkedModelSerializer):
    """
    Serialize pubmed entries.
    """

    user = EntryUserSerializer()

    # noinspection PyDocstring
    class Meta:
        model = EntryMeta.model
        fields = ('url', 'pubmed_id') + EntryMeta.all_fields
        depth = 1
