#!/usr/bin/env python
# coding=utf-8
"""Build and load initial gene data."""

import json
import re
from functools import reduce, wraps
from pathlib import Path
from pprint import pprint
from queue import Queue
from threading import Thread
from uuid import UUID
import yaml
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.serializers.base import DeserializationError

DEBUG = False

LOOKUP_MODEL = {
    'ccds_id': 'CcdsIdLookup',
    'alias_name': 'AliasNameLookup',
    'alias_symbol': 'AliasSymbolLookup',
    'gene_family': 'GeneFamilyLookup',
    'gene_family_id': 'GeneFamilyIdLookup',
    'refseq_accession': 'RefseqAccessionLookup',
    'ena': 'EnaLookup',
    'pubmed_id': 'PubmedIdLookup',
    'rgd_id': 'RgdIdLookup',
    'uniprot_ids': 'UniprotIdsLookup',
    'mgd_id': 'MgdIdLookup',
    'omim_id': 'OmimIdLookup',
    'enzyme_id': 'EnzymeIdLookup',
    'lsdb': 'LsdbLookup',
    'prev_name': 'PrevNameLookup',
    'prev_symbol': 'PrevSymbolLookup'
}


class Config:
    """Config constants."""
    _CWD = Path(__file__, '..').resolve()
    DATA_DIR = (_CWD / '_gene_init').resolve()
    FIXTURES_DIR = (_CWD / '../..' / 'fixtures').resolve()
    APP = 'gene'
    MODEL = 'Gene'


class Command(BaseCommand):
    """Get gene data."""
    help = __doc__
    references_built = False
    q = NotImplemented
    LOOKUP_FIELDS = {
        'ccds_id': {},
        'alias_name': {},
        'alias_symbol': {},
        'gene_family': {},
        'gene_family_id': {},
        'refseq_accession': {},
        'ena': {},
        'pubmed_id': {},
        'rgd_id': {},
        'uniprot_ids': {},
        'mgd_id': {},
        'omim_id': {},
        'enzyme_id': {},
        'lsdb': {},
        'prev_name': {},
        'prev_symbol': {}
    }

    def add_arguments(self, parser):
        """
        Add command arguments.

        :param django.core.management.base.CommandParser parser: CommandParser object.
        """
        parser.add_argument('--get', default=False, action='store_true', help='Check db for updates')
        parser.add_argument('--skip-lookup', '-l', default=False, action='store_true', help='Check db for updates')
        parser.add_argument('--skip-build', '-b', default=False, action='store_true', help='Check db for updates')
        parser.add_argument('--init', '-i', default=False, action='store_true', help='Load Gene fixtures into DB.')

    def handle(self, *args, **options):
        """
        Command Handle.

        :param args:
        :param dict options: Arguments from Parser object.
        :return:
        """
        get, init, skip_build, skip_lookup = options['get'], options['init'], options['skip_build'], options[
            'skip_lookup']
        if get:
            # TODO Pull data from API.
            pass

        docs = [self.clean_doc(doc) for doc in self.get_docs()]

        if not skip_lookup:
            print('Building lookups  ' + '#' * 20)
            self.dump_lookup_fixture(docs)

        if not skip_build:
            print('Building fixtures ' + '#' * 20)
            self.build_gene_fixtures(docs)

        if init:
            print('Loading fixtures  ' + '#' * 20)
            self.init_fixtures()

    def build_gene_fixtures(self, docs):
        """

        :param docs:
        """
        if not self.references_built:
            self.LOOKUP_FIELDS = self.load_references()

        fixtures = [self.format_gene_fixture(doc) for doc in docs]

        # self._print_max_lengths(fixtures)
        # self._get_fixture('b2d38ea3-65b2-478c-89d3-0f4c1c2559db', fixtures)

        self.dump(fixtures)

    def dump_lookup_fixture(self, docs):
        """
        Save lookup fixture.

        :param [dict] docs: Source.
        """

        if not self.references_built:
            self.build_references(docs)

        def async_dump(q, fixtures, model):
            q.put(self.dump(fixtures, model=model))

        q = Queue()
        for field, choices in self.LOOKUP_FIELDS.items():
            model = LOOKUP_MODEL[field]
            fixtures = [self.format_lookup_fixture(pk, choice, model) for choice, pk in choices.items()]
            t = Thread(target=async_dump, args=(q, fixtures, model))
            t.daemon = True
            t.start()
            # q.put(lambda: self.dump(fixtures, model=model))

        while not q.empty():
            q.get()
            q.task_done()
        q.join()

    def build_references(self, docs):
        """
        Build reference data.

        :param [dict] docs:
        """
        for field in self.LOOKUP_FIELDS.keys():
            data = {item for doc in docs if doc.get(field) for item in doc.get(field)}
            self.LOOKUP_FIELDS[field] = {item: pk for pk, item in enumerate(sorted(data), start=1)}

        t = Thread(target=self.dump_references, args=(self.LOOKUP_FIELDS,))
        t.daemon = True
        t.start()
        self.dump_references = True
        # self.dump_references(self.LOOKUP_FIELDS)

    @staticmethod
    def clean_doc(doc):
        """
        Remove malformed data.

        :param dict doc: Single doc.
        :return:
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
                    doc[key] = [item.strip() for item in re.split(',', doc[key][0])]
                except (TypeError, AttributeError):
                    """Optional key doesn't exist"""

        # remove underscores.
        doc['version'] = doc.pop('_version_')
        return doc

    @staticmethod
    def format_lookup_fixture(pk, choice, model):
        """
        Format lookup doc into fixture.

        :param int pk: pk for model
        :param int|str choice:
        :param str model: Combined with `Config.APP` for fixture.
        :return:
        """
        return {
            'pk': pk,
            'model': '%s.%s' % (Config.APP, model),
            'fields': {
                'choice': choice
            }
        }

    def format_gene_fixture(self, doc):
        """
        Build fixture from raw data.

        :param dict doc: Flat dictionary data
        :return: Fixture representation.
        """
        pk = UUID(doc.pop('uuid')).urn
        doc = self.inject_pk_ref(doc)

        fixture = {
            'pk': pk,
            'model': '%s.%s' % (Config.APP, Config.MODEL),
            'fields': doc
        }

        return fixture

    def inject_pk_ref(self, doc):
        """
        Replace arrays with arrays of fks.

        :param dict doc:
        :return: Updated doc
        """
        for list_field in self.LOOKUP_FIELDS.keys():
            if list_field in doc.keys():
                doc[list_field] = [self.LOOKUP_FIELDS[list_field][list_item] for list_item in doc[list_field]]
        return doc

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

    def dump(self, fixtures, filepath=Config.FIXTURES_DIR, model=Config.MODEL):
        """
        Save fixtures to files.

        :param [{}] fixtures: Chunks of fixtures.
        :param pathlib.Path filepath: Output dir.
        :param str model: Model to used in filename.
        """

        fixture_chunks = self.chunk(fixtures)
        for i, fixtures in fixture_chunks:
            file_name = '%s-%s.yaml' % (model, i)
            print('Writing %s records to %s' % (len(fixtures), file_name))
            with filepath.joinpath(file_name).open('w') as f:
                yaml.dump(fixtures, f)
        print('### %s fixture(s) created! %s records in %s files.\n' % (model, len(fixtures), len(fixture_chunks)))

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

    def init_fixtures(self):
        """Save fixtures into db."""

        for field, choices in self.LOOKUP_FIELDS.items():
            model = LOOKUP_MODEL[field]
            fixtures = [self.format_lookup_fixture(pk, choice, model) for choice, pk in choices.items()]

            # def worker():
            #     while True:
            #         file = q.get()
            #         if file is None:
            #             break
            #         self.loaddata(file)
            #         q.task_done()
            #
            # q = Queue()
            # threads = []
            # number_of_worker_threads = 10
            # for i in range(number_of_worker_threads):
            #     t = Thread(target=worker)
            #     t.start()
            #     threads.append(t)



            # q.put(lambda: self.dump(fixtures, model=model))

        for file in Config.FIXTURES_DIR.glob('*Lookup-*.yaml'):
            # q.put(file)
            # self.loaddata(file)
            pass

            # q.join()
            for file in Config.FIXTURES_DIR.glob('Gene-*.yaml'):
                # q.put(file)
                self.loaddata(file)

                #
                # q.join()
                # for i in range(number_of_worker_threads):
                #     q.put(None)
                # for t in threads:
                #     t.join()

    # noinspection PyMethodMayBeStatic
    def loaddata(self, file):
        """
        Call django's loaddata command.

        :param file: Fixture to load.
        :return:
        """
        try:
            print('Loading %s' % file)
            call_command('loaddata', file.name, database='genes')
        except (KeyError, LookupError, DeserializationError) as e:

            print('Model in fixture %s.%s could not be loaded. Import skipped.\n        Error:%s' % (
                Config.APP, file.stem, str(e).split(':')[-1]))

    # noinspection PyMethodMayBeStatic
    def dump_references(self, data):
        """
        Serialize reference data.

        :param dict data: Data to serialize.
        """

        print('Serializing references...')
        with Config.DATA_DIR.joinpath('reference.yaml').open('w') as f:
            yaml.dump(data, f)
        print('Processing complete! Saving to file.  Be Patient')

    # noinspection PyMethodMayBeStatic
    def load_references(self):
        """
        Deserialize reference data.

        :return: Dictionary of enumerated choices for lookup tables.
        """

        print('Deserializing references...')
        with Config.DATA_DIR.joinpath('reference.yaml').open() as f:
            return yaml.load(f)
