# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import pubmed_lookup.migrations.initial_data


class Migration(migrations.Migration):
    dependencies = [('pubmed', '0001_initial'),
                    ('pubmed_lookup', '0001_initial'), ]

    operations = [migrations.RunPython(

        code=pubmed_lookup.migrations.initial_data.populate_lookup_tables,
        reverse_code=pubmed_lookup.migrations.initial_data.clean_lookup_tables,

    )]
