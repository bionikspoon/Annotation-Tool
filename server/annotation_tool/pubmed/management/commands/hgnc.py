import json
import re
from pathlib import Path
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

    def handle(self, *args, **options):
        get = options.get('get')
        if get:
            pass

        docs = self.get_docs()
        fixtures = [self.build_fixture(doc) for doc in docs][:10000]
        fixture = [fixture for fixture in fixtures if
                   fixture.get('pk').endswith('e446aed5-1a17-4f89-8168-5fec55a93117')]
        # ipdb.set_trace()
        self.dump(fixtures)
        print('%s fixture created with %s records.' % (config.MODEL, len(fixtures)))

    @staticmethod
    def build_fixture(doc):
        try:
            del doc['pseudogene.org']
        except KeyError:
            pass
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
    def dump(fixtures):
        with config.FIXTURES_DIR.joinpath('%s.yaml' % config.MODEL).open('w') as f:
            yaml.dump(fixtures, f)
