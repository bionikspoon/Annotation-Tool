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
    Empty Base Class.  Collect choices from all subl classes.
    """
    choices = NotImplemented

    @classmethod
    def export_flat(cls):
        """
        Format collected data.

        :return: Flat list of entries.
        :rtype: list
        """
        return (

            LookupChoice(subclass.__name__, pk, choice)

            for subclass in cls.__subclasses__()

            for pk, choice in enumerate(subclass.choices)

        )

    @classmethod
    def export_groups(cls):
        def choices(subclass):
            return (

                {'pk': pk, 'choice': choice}

                for pk, choice in enumerate(subclass.choices)

            )

        return (

            LookupModelGroup(subclass.__name__, choices(subclass))

            for subclass in cls.__subclasses__()

        )


def populate_lookup_tables(apps, schema_editor):
    """
    Create each lookup table entries.

    :param apps:
    :param schema_editor:
    :return:
    """
    for entries in InitialData.export_groups():
        try:
            Model = apps.get_model('pubmed', entries.cls)
        except LookupError:
            continue

        Model.objects.bulk_create(

            Model(**entry) for entry in entries.objects

        )


def unpopulate_lookup_tables(apps, schema_editor):
    """
    Remove all lookup table entries.

    :param apps:
    :param schema_editor:
    :return:
    """
    for sublcass in InitialData.__subclasses__():
        try:
            Model = apps.get_model('pubmed', sublcass.__name__)
            Model.objects.all().delete()
        except LookupError:
            pass


if __name__ == '__main__':
    pprint(list(InitialData.export_flat()))
