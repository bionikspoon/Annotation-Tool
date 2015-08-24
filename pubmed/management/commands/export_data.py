#!/usr/bin/env python
# coding=utf-8
from itertools import chain
import json
import io
import re

from django.core.management.base import BaseCommand
from django.conf import settings


class CONFIG(object):
    data = settings.ROOT_DIR.path('pubmed', 'management', 'data')
    input = data.path('input')
    output = data.path('output')
    db = settings.ROOT_DIR.path('pubmed', 'db')
    summary = 'generated_data.py'


buffer = io.StringIO()


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        prepare_summary()

        process_input('AssessedPatientOutcome')

        process_input('SignificantPatientOutcome')
        # process('Treatment')
        process_input('VariantConsequence')
        process_input('VariantType')

        print_summary()


def get_data(fp):
    with CONFIG.input.file(fp) as f:
        raw_text = f.read().splitlines()

    # split by newline and ";",  filter empty, flatten
    data = set(chain(*[re.split(r'; ?', line) for line in raw_text if line]))

    # clean data. replace "_" and title case
    data = map(lambda x: x.replace('_', ' ').title(), data)

    # remove obscure symbols
    data = map(lambda x: re.sub(r'[^\w\s\-\(\)]', '', x), data)

    # clean whitespace. run generator
    data = [re.sub(r' +', ' ', item.strip()) for item in data if item]
    return set(data)


def compile_data_objects(data_set, model):
    full_model_name = 'pubmed.%s' % model
    return [dict(model=full_model_name, pk=key, fields={'choice': data}) for
            key, data in enumerate(sorted(data_set))]


def dump_pretty_json(data, fp):
    with CONFIG.output.file(fp, 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4, separators=(',', ': '))


def prepare_summary(module_path='.initial_data'):
    buffer.write('from %s import InitialData\n\n' % module_path)


def add_to_summary(data, name):
    buffer.write("class %s(InitialData):\n" % name)
    buffer.write("    choices = [\n")
    for choice in sorted(data):
        buffer.write("        '%s',\n" % choice)
    buffer.write("    ]\n\n\n")


def print_summary():
    print(buffer.getvalue())
    with CONFIG.db.file(CONFIG.summary, 'w') as f:
        f.write(buffer.getvalue())
        buffer.close()


def process_input(file_name):
    model_name = '%sLookup' % file_name
    data_set = get_data('%s.txt' % file_name)

    data_objects = compile_data_objects(data_set, model_name)
    add_to_summary(data_set, model_name)
    dump_pretty_json(data_objects, '%s.json' % file_name)


if __name__ == '__main__':
    process_input('AssessedPatientOutcome')
    process_input('SignificantPatientOutcome')
    # process('Treatment')
    process_input('VariantConsequence')
    process_input('VariantType')

    print_summary()
