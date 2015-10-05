import json
from pathlib import Path
from pprint import pprint

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
        with config.DATA_DIR.joinpath('hgnc_complete_set.json').open() as f:
            hgnc = json.load(f)

        docs = hgnc['response']['docs']
        fixtures = [self.build_fixture(doc) for doc in docs]
        with config.FIXTURES_DIR.joinpath('%s.yaml' % config.MODEL).open('w') as f:
            yaml.dump(fixtures, f)

    @staticmethod
    def build_fixture(doc):
        fixture = {}
        fixture['pk'] = doc.pop('uuid')
        fixture['model'] = '%s.%s' % (config.APP, config.MODEL)
        fixture['fields'] = doc
        return fixture
