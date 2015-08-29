# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pubmed


class Migration(migrations.Migration):
    dependencies = [('pubmed', '0001_initial'), ]

    operations = [migrations.RunPython(

        code=pubmed.migrations.initial_data.populate_lookup_tables,
        reverse_code=pubmed.migrations.initial_data.clean_lookup_tables,

    )]
