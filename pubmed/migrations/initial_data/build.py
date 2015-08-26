#!/usr/bin/env python
# coding=utf-8
"""
Compile generated_data.py from raw data.
"""
from io import StringIO
from itertools import chain
import json
import re

from django.conf import settings


class CONFIG(object):
    """ Config object. """
    data = settings.ROOT_DIR.path('pubmed', 'migrations', 'initial_data',
                                  'data')
    module = 'pubmed'
    input = data.path('input')
    output = data.path('output')

    summary_fp = data - 1
    summary = 'generated_data.py'


# noinspection PyUnresolvedReferences
class SummaryManager(object):
    """Generated Data."""

    IMPORT_LINE = "from . import InitialData"
    OUT_FILE = lambda *args: CONFIG.summary_fp.file(CONFIG.summary, 'w')

    def __init__(self):
        self.buffer = StringIO()
        self.build_header()

    def write(self, line='', indent=0):
        TAB = '    '
        line = '%s%s' % (TAB * indent, line)
        self.buffer.write('%s\n' % line)

    def build_header(self):
        self.write('#!/usr/bin/env python')
        self.write('# coding=utf-8')
        self.write('"""\n%s\n"""\n' % self.__doc__)
        self.write(self.IMPORT_LINE)
        self.write()

    def add_model(self, model, choices):
        if not choices:
            return

        self.write('class %s(InitialData):' % model)
        self.write('choices = [', indent=1)
        self.write()
        [self.write('\'%s\'' % choice, indent=2) for choice in sorted(choices)]
        self.write()
        self.write(']', indent=1)
        self.write('\n')

    def save(self):
        with self.OUT_FILE() as f:
            print(self)
            f.write(str(self))

    def __str__(self):
        return self.buffer.getvalue()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.buffer.close()


class ModelFactory(object):
    data_in = CONFIG.input
    data_out = CONFIG.output
    fixture_prefix = CONFIG.module
    model_name = NotImplemented
    file_name = NotImplemented
    model_choices = NotImplemented
    manager = NotImplemented

    def __init__(self, name):
        self.model_name = '%sLookup' % name
        self.file_name = '%s.txt' % name
        self.json_file_name = '%s.json' % name

        with self.data_in.file(self.file_name) as f:
            raw_data = f.read().splitlines()

        self.model_choices = self.get_choices(raw_data)

        if self.manager:
            self.manager.add_model(self.model_name, self.model_choices)

        fixture = self.prepare_fixture()
        dump_pretty_json(fixture, self.json_file_name)

    @classmethod
    def with_manager(cls, manager):
        cls.manager = manager
        return cls

    def get_choices(self, data):
        # split by newline and ";",  filter empty, flatten
        data = set(chain(*[re.split(r'; ?', line) for line in data if line]))

        # clean data. replace "_" and title case
        data = map(lambda x: x.replace('_', ' ').title(), data)

        # remove obscure symbols
        data = map(lambda x: re.sub(r'[^\w\s\-\(\)]', '', x), data)

        # clean whitespace. run generator
        data = (re.sub(r' +', ' ', item.strip()) for item in data if item)

        return set(data)

    def prepare_fixture(self):
        fixture_name = '%s.%s' % (self.fixture_prefix, self.model_name)
        return [{'model': fixture_name, 'pk': pk, 'fields': data} for pk, data
                in enumerate(sorted(self.model_choices))]


def dump_pretty_json(data, fp):
    with CONFIG.output.file(fp, 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4, separators=(',', ': '))


def generate_data():
    summary = SummaryManager()
    process = ModelFactory.with_manager(summary)
    process('AssessedPatientOutcome')
    process('Disease')

    process('SignificantPatientOutcome')
    # process('Treatment')
    process('VariantConsequence')
    process('VariantType')

    summary.save()
