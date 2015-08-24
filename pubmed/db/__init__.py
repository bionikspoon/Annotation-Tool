#!/usr/bin/env python
# coding=utf-8
from pprint import pprint

from pubmed.db.initial_data import InitialData, populate_lookup_tables
from pubmed.db.entered_data import *
from pubmed.db.generated_data import *

if __name__ == '__main__':
    pprint(list(InitialData.export()))
