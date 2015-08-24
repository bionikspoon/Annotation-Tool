#!/usr/bin/env python
# coding=utf-8
from collections import namedtuple
from pprint import pprint

LookupChoice = namedtuple('LookupChoice', ('cls', 'pk', 'choice'))


class InitialData(object):
    @classmethod
    def export(cls):
        return (

            LookupChoice(subclass.__name__, pk, choice)

            for subclass in cls.__subclasses__()

            for pk, choice in enumerate(subclass.choices)

        )


def populate_lookup_tables(apps, schema_editor):
    for entry in InitialData.export():
        Model = apps.get_model('pubmed', entry.cls)
        Model.objects.create(pk=entry.pk, choice=entry.choice)


def unpopulate_lookup_tables(apps, schema_editor):
    for sublcass in InitialData.__subclasses__():
        Model = apps.get_model('pubmed', sublcass.__name__)
        Model.objects.all().delete()



if __name__ == '__main__':
    pprint(list(InitialData.export()))
