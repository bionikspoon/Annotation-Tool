#!/usr/bin/env python
# coding=utf-8

from pubmed.db.initial_data import (InitialData, populate_lookup_tables,
                                    unpopulate_lookup_tables)
from pubmed.db.entered_data import *
from pubmed.db.generated_data import *

if __name__ == '__main__':
    from pprint import pprint

    pprint(list(InitialData.export()))
