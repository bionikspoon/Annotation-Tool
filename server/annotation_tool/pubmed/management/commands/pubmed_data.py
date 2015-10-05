#!/usr/bin/env python
# coding=utf-8
"""Build and load initial pubmed data."""

import re
from itertools import chain
from pathlib import Path

import yaml
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.serializers.base import DeserializationError


class Config:
    """Command constants."""
    _CWD = Path(__file__, '..').resolve()
    DATA_DIR = (_CWD / '_pubmed_data').resolve()
    FIXTURES_DIR = (_CWD / '../..' / "fixtures").resolve()
    APP = 'pubmed'


class Command(BaseCommand):
    """Load initial data."""
    help = __doc__

    def add_arguments(self, parser):
        """
        Command arguments.

        :param django.core.management.base.CommandParser parser: Parse arguments.
        """
        parser.add_argument('--build-only', '-b', default=False, action='store_true',
                            help="Only build from source. Skip import.")
        parser.add_argument('--import-only', '-i', default=False, action='store_true',
                            help='Only import existing fixtures.  Skip building from source.')
        parser.add_argument('--all', '-a', default=False, action='store_true', help='Import gene fixtures too.')

    def handle(self, *args, **options):
        """
        Command handle.

        :param args:
        :param options: Argument map from `add_arguments`.
        """
        build_only, import_only, import_all = options.get('build_onl'), options.get('import_only'), options.get('all')

        if build_only:
            self.build_from_source()
            return

        if import_only:
            self.load_fixtures(import_all)
            return

        self.build_from_source()
        self.load_fixtures(import_all)

    @staticmethod
    def parse_choices(file):
        """
        Get set of choices from raw data file.

        :param pathlib.Path file: Path object, referencing file.
        :return: Set of choices.
        :rtype: set
        """
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

    @staticmethod
    def build_fixtures(choices, model, app=Config.APP):
        """
        Build fixtures from choices.

        :param set choices: Set of choices.
        :param str model: Model to be referenced in fixture.
        :param str app: Django app to be referenced in fixture.
        :return: List of fixtures.
        :rtype: [dict]
        """
        fixture_name = '%s.%s' % (app, model)
        return [dict(model=fixture_name, pk=pk, fields={'choice': choice}) for pk, choice in
                enumerate(sorted(choices), start=1)]

    @staticmethod
    def dump(fixtures, name, filepath=Config.FIXTURES_DIR):
        """
        Dump fixtures to `.yaml` file.

        :param [dict] fixtures: List of fixtures.
        :param name: Name for file output.
        :param pathlib.Path filepath: Path object pointing to fixtures directory.
        """
        file = filepath.joinpath('%s.yaml' % name)
        with file.open('w') as f:
            yaml.dump(fixtures, f)

        print('Fixture generated:', file)

    def build_from_source(self):
        """Build process.  Get files -> get choices -> build fixtures -> dump yaml."""
        for file in Config.DATA_DIR.glob('*.txt'):
            choices = self.parse_choices(file)
            fixtures = self.build_fixtures(choices, file.stem)
            self.dump(fixtures, file.stem)

    @staticmethod
    def load_fixtures(import_all):
        """Save fixtures into db."""

        for file in Config.FIXTURES_DIR.glob('*.yaml'):
            if not import_all and '-' in file.stem:
                continue
            try:
                call_command('loaddata', file.name)
            except (KeyError, LookupError, DeserializationError):

                print('Model in fixture %s not found. Import skipped' % Config.APP, file.stem)
