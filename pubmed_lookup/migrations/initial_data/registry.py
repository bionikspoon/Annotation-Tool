#!/usr/bin/env python
# coding=utf-8
"""
Base class.  Aggregate all data.
"""
from collections import namedtuple
from pprint import pprint

LookupChoice = namedtuple('LookupChoice', ('cls', 'pk', 'choice'))
LookupModelGroup = namedtuple('LookupModelGroup', ('cls', 'objects'))


class InitialData(object):
    """
    Empty Base Class.  Collect choices from all sub classes.
    """
    choices = NotImplemented

    @classmethod
    def export_flat(cls):
        """
        Format collected data into flat list of objects.

        :return: Flat list of entries.
        """
        return (

            LookupChoice(subclass.__name__, pk, choice)

            for subclass in cls.__subclasses__()

            for pk, choice in enumerate(subclass.choices, start=1)

        )

    @classmethod
    def export_groups(cls):
        """
        Format collected data into grouped list of objects.

        :return:
        """

        def choices(subclass):
            """
            Format choices for model group.

            :param subclass:
            :return:
            """
            return ({
                        'pk': pk,
                        'choice': choice
                    }

                    for pk, choice in enumerate(subclass.choices, start=1))

        return (

            LookupModelGroup(subclass.__name__, choices(subclass))

            for subclass in cls.__subclasses__()

        )


# noinspection PyUnusedLocal
def populate_lookup_tables(apps, schema_editor):
    """
    Create each lookup table entries.

    :param apps:
    :param schema_editor:
    :return:
    """
    for entries in InitialData.export_groups():
        try:
            # noinspection PyPep8Naming
            Model = apps.get_model('pubmed_lookup', entries.cls)
        except LookupError:
            continue

        Model.objects.bulk_create(

            Model(**entry) for entry in entries.objects

        )


# noinspection PyUnusedLocal
def clean_lookup_tables(apps, schema_editor):
    """
    Remove all lookup table entries.

    :param apps:
    :param schema_editor:
    :return:
    """
    for subclass in InitialData.__subclasses__():
        try:
            # noinspection PyPep8Naming
            Model = apps.get_model('pubmed_lookup', subclass.__name__)
            Model.objects.all().delete()
        except LookupError:
            pass


if __name__ == '__main__':
    pprint(list(InitialData.export_flat()))
