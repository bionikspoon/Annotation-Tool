import json
import re
from functools import reduce
from pathlib import Path
from pprint import pprint
from uuid import UUID

import ipdb
import yaml
from django.core.management.base import BaseCommand


class config:
    _CWD = Path(__file__, '..').resolve()
    DATA_DIR = (_CWD / '_hgnc').resolve()
    FIXTURES_DIR = (_CWD / '../..' / "fixtures").resolve()
    APP = 'pubmed'
    MODEL = 'Gene'


class Command(BaseCommand):
    """Get gene hgnc gene data."""
    help = __doc__

    def add_arguments(self, parser):
        """:type parser: django.core.management.base.CommandParser"""
        parser.add_argument('--get', default=False, action='store_true', help='Check db for updates')
        parser.add_argument('--load', default=False, action='store_true', help='Load Gene fixtures into DB.')

    def handle(self, *args, **options):
        get, load = options.get('get'), options.get('load')
        if get:
            pass

        docs = self.get_docs()
        fixtures = [self.build_fixture(doc) for doc in docs]
        fixture_chunks = self.chunk(fixtures)
        # self._print_max_lengths(fixtures)
        # self._get_fixture('b2d38ea3-65b2-478c-89d3-0f4c1c2559db', fixtures)

        print('Processing complete! Saving to file.  Be Patient')
        self.dump(fixture_chunks)
        print('%s fixture(s) created! %s records in %s files.' % (config.MODEL, len(fixtures), len(fixture_chunks)))
        if load:
            self.persist_genes()

    @staticmethod
    def build_fixture(doc):
        try:
            if doc.get('pseudogene.org'):
                del doc['pseudogene.org']
            if doc.get('mamit-trnadb'):
                del doc['mamit-trnadb']
        except KeyError as e:
            print('Unkown exception.')
            raise KeyError from e
        for key in doc.keys():
            if isinstance(doc[key], list):
                try:
                    doc[key] = [item.strip() for item in re.split(', ?|\s+', doc[key][0])]
                except (TypeError, AttributeError):
                    pass

        fixture = {}
        fixture['pk'] = UUID(doc.pop('uuid')).urn
        fixture['model'] = '%s.%s' % (config.APP, config.MODEL)
        fixture['fields'] = doc
        fixture['fields']['version'] = fixture['fields'].pop('_version_')

        return fixture

    @staticmethod
    def get_docs():
        with config.DATA_DIR.joinpath('hgnc_complete_set.json').open() as f:
            hgnc = json.load(f)
        return hgnc['response']['docs']

    @staticmethod
    def dump(chunks):
        for i, fixtures in chunks:
            file_name = '%s-%s.yaml' % (config.MODEL, i)
            print('Writing %s records to %s' % (len(fixtures), file_name))
            with config.FIXTURES_DIR.joinpath(file_name).open('w') as f:
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
    def _get_fixture(needle, fixtures, field='pk'):
        # noinspection PyUnresolvedReferences
        from pprint import pprint

        fixture = [fixture for fixture in fixtures if fixture.get(field).endswith(needle)][0]
        ipdb.set_trace()

    @staticmethod
    def chunk(fixtures):
        chunk_size = 5000
        start = 0
        stop = chunk_size
        chunks = []
        for i in range(len(fixtures) // 5000 + 1):
            if start > len(fixtures):
                break

            chunks.append((i + 1, fixtures[start:stop]))
            start, stop = stop, stop + chunk_size

        return chunks

    @staticmethod
    def persist_genes():
        pass
