#!/usr/bin/env python
# coding=utf-8
"""
Base class.  Aggregate all data.
"""
from collections import namedtuple
from pprint import pprint

LookupChoice = namedtuple('LookupChoice', ('cls', 'pk', 'choice'))


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


def populate_lookup_tables(apps, schema_editor):
    """
    Create each lookup table entry.

    :param apps:
    :param schema_editor:
    :return:
    """
    for entry in InitialData.export_flat():
        try:
            Model = apps.get_model('pubmed', entry.cls)
            Model.objects.create(pk=entry.pk, choice=entry.choice)
        except LookupError:
            pass


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
