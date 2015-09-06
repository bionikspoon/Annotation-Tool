# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

import pubmed.lookups.migrations.initial_data
from pubmed.lookups.migrations.initial_data import populate_lookup_tables


class Migration(migrations.Migration):
    dependencies = [('lookups', '0001_initial'), ]

    operations = [migrations.RunPython(

        code=pubmed.lookups.migrations.initial_data.populate_lookup_tables,
        reverse_code=pubmed.lookups.migrations.initial_data.clean_lookup_tables,

    )]
