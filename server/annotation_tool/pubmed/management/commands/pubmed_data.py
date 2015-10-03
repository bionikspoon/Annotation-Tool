#!/usr/bin/env python
# coding=utf-8
import re
from itertools import chain
from pathlib import Path

import yaml
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.serializers.base import DeserializationError


class config:
    _CWD = Path(__file__, '..').resolve()
    DATA_DIR = (_CWD / '_pubmed_data').resolve()
    FIXTURES_DIR = (_CWD / '../..' / "fixtures").resolve()
    APP = 'pubmed'


def parse_choices(file):
    with file.open() as f:
        data = f.read().splitlines()

    # split by newline and ";",  filter empty, flatten
    data = set(chain(*[re.split(r'; ?', line) for line in data if line]))

    # clean data. replace "_" and title case
    data = map(lambda x: x.replace('_', ' ').title(), data)

    # remove obscure symbols
    data = map(lambda x: re.sub(r'[^\w\s\-\(\)]', '', x), data)

    # clean whitespace. run generator
    data = (re.sub(r' +', ' ', item.strip()) for item in data if item)

    return set(data)


def build_fixtures(choices, model, app=config.APP):
    fixture_name = '%s.%s' % (app, model)
    return [dict(model=fixture_name, pk=pk, fields={'choice': choice}) for pk, choice in
            enumerate(sorted(choices), start=1)]


def save_fixture_to_file(data, name):
    file = config.FIXTURES_DIR.joinpath('%s.yaml' % name)
    with file.open('w') as f:
        yaml.dump(data, f)

    print('Fixture generated:', file)


def build_from_source():
    for file in config.DATA_DIR.glob('*.txt'):
        choices = parse_choices(file)
        fixtures = build_fixtures(choices, file.stem)
        save_fixture_to_file(fixtures, file.stem)


def load_fixtures():
    for file in config.FIXTURES_DIR.glob('*.yaml'):
        try:
            call_command('loaddata', file.name)
        except (KeyError, LookupError, DeserializationError):
            import sys

            print('Model %s.%s not found. Import skipped' % (config.APP, file.stem), file=sys.stdout)


class Command(BaseCommand):
    """Load initial data."""
    help = __doc__

    def add_arguments(self, parser):
        """:type parser: django.core.management.base.CommandParser"""
        parser.add_argument('--build-only', '-b', default=False, action='store_true',
                            help="Only build from source. Skip import.")
        parser.add_argument('--import-only', '-i', default=False, action='store_true',
                            help='Only import existing fixtures.  Skip building from source.')

    def handle(self, *args, **options):
        build_only, import_only = options.get('build_onl'), options.get('import_only')

        if build_only:
            build_from_source()
            return

        if import_only:
            load_fixtures()
            return

        build_from_source()
        load_fixtures()
