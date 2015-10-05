import json
from pathlib import Path
from uuid import UUID

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

    def handle(self, *args, **options):
        get = options.get('get')
        if get:
            pass

        docs = self.get_docs()
        fixtures = [self.build_fixture(doc) for doc in docs][:10]

        self.dump(fixtures)

        print('%s fixture created with %s records.' % (config.MODEL, len(fixtures)))

    @staticmethod
    def build_fixture(doc):
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
    def dump(fixtures):
        with config.FIXTURES_DIR.joinpath('%s.yaml' % config.MODEL).open('w') as f:
            yaml.dump(fixtures, f)
