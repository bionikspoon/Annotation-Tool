#!/usr/bin/env python
# coding=utf-8
"""Build and load initial gene data."""

import json
import re
from functools import reduce
from pathlib import Path
from pprint import pprint
from uuid import UUID

import yaml
from django.core.management.base import BaseCommand


class Config:
    """Config constants."""
    _CWD = Path(__file__, '..').resolve()
    DATA_DIR = (_CWD / '_gene_data').resolve()
    FIXTURES_DIR = (_CWD / '../..' / "fixtures").resolve()
    APP = 'pubmed'
    MODEL = 'Gene'


class Command(BaseCommand):
    """Get gene data."""
    help = __doc__

    def add_arguments(self, parser):
        """
        Add command arguments.

        :param django.core.management.base.CommandParser parser: CommandParser object.
        """
        parser.add_argument('--get', default=False, action='store_true', help='Check db for updates')
        parser.add_argument('--load', default=False, action='store_true', help='Load Gene fixtures into DB.')

    def handle(self, *args, **options):
        """
        Command Handle.

        :param args:
        :param dict options: Arguments from Parser object.
        :return:
        """
        get, load = options.get('get'), options.get('load')
        if get:
            # TODO Pull data from API.
            pass

        docs = self.get_docs()
        fixtures = [self.build_fixture(doc) for doc in docs]
        fixture_chunks = self.chunk(fixtures)
        # self._print_max_lengths(fixtures)
        # self._get_fixture('b2d38ea3-65b2-478c-89d3-0f4c1c2559db', fixtures)

        print('Processing complete! Saving to file.  Be Patient')
        self.dump(fixture_chunks)
        print('%s fixture(s) created! %s records in %s files.' % (Config.MODEL, len(fixtures), len(fixture_chunks)))
        if load:
            self.persist_genes()

    @staticmethod
    def build_fixture(doc):
        """
        Build fixture from raw data.

        :param dict doc: Flat dictionary data
        :return: Fixture representation.
        """
        try:
            # Clean obscure keys.
            if doc.get('pseudogene.org'):
                del doc['pseudogene.org']
            if doc.get('mamit-trnadb'):
                del doc['mamit-trnadb']
        except KeyError as e:
            print('Unknown exception.')
            raise KeyError from e

        for key in doc.keys():
            if isinstance(doc[key], list):
                try:
                    # do a better job at parsing array's of strings from json.
                    doc[key] = [item.strip() for item in re.split(', ?|\s+', doc[key][0])]
                except (TypeError, AttributeError):
                    """Optional key doesn't exist"""

        pk = UUID(doc.pop('uuid')).urn
        fixture = {'pk': pk, 'model': '%s.%s' % (Config.APP, Config.MODEL), 'fields': doc}

        # remove underscores.
        fixture['fields']['version'] = fixture['fields'].pop('_version_')

        return fixture

    @staticmethod
    def get_docs(filepath=Config.DATA_DIR, filename='hgnc_complete_set.json'):
        """
        Get gene data from json file.

        :param pathlib.Path filepath: Directory of json data.
        :param filename: json data file name.
        :return: List of docs.
        :rtype: [dict]
        """
        with filepath.joinpath(filename).open() as f:
            data = json.load(f)
        return data['response']['docs']

    @staticmethod
    def dump(chunks, filepath=Config.FIXTURES_DIR, model=Config.MODEL):
        """
        Save fixtures to files.

        :param [tuple] chunks: Chunks of fixtures.
        :param pathlib.Path filepath: Output dir.
        :param str model: Model to used in filename.
        """
        for i, fixtures in chunks:
            file_name = '%s-%s.yaml' % (model, i)
            print('Writing %s records to %s' % (len(fixtures), file_name))
            with filepath.joinpath(file_name).open('w') as f:
                yaml.dump(fixtures, f)

    @staticmethod
    def _print_max_lengths(fixtures):
        length = {}
        for fixture in fixtures:
            for key, value in fixture['fields'].items():
                try:
                    if isinstance(value, list):
                        current = reduce(lambda a, b: max(a, len(b)), value, 0)
                    else:
                        current = length.get(key, 0)

                    length[key] = max(current, len(value))
                except TypeError:
                    print(value)
                    pass

        pprint(length)

    @staticmethod
    def _get_fixture(needle, fixtures):
        """
        Debug helper utility.  Find fixture by uuid suffix. Start `ipdb`.

        :param needle: UUID to search for.
        :param fixtures: List of fixtures.
        """

        import ipdb
        # noinspection PyUnresolvedReferences
        from pprint import pprint

        """Import pprint into debug context."""

        # noinspection PyUnusedLocal
        fixture = [fixture for fixture in fixtures if fixture.get('pk').endswith(needle)][0]
        """Load fixture into debug context."""

        ipdb.set_trace()

    @staticmethod
    def chunk(fixtures, chunk_size=5000):
        """
        Utility break large list in chunks.

        :param [dict] fixtures: List of fixtures.
        :param int chunk_size: Size of chunks.
        :return: List of tuples.  [(id, fixtures)]
        :rtype: [tuple]
        """

        start = 0
        stop = chunk_size
        chunks = []
        for i in range(len(fixtures) // chunk_size + 1):
            if start > len(fixtures):
                break

            chunks.append((i + 1, fixtures[start:stop]))
            start, stop = stop, stop + chunk_size

        return chunks

    @staticmethod
    def persist_genes():
        """Save fixtures to db."""
        # TODO Save fixtures to db.
        pass
