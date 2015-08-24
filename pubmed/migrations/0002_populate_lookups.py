# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

import pubmed


class Migration(migrations.Migration):
    dependencies = [('pubmed', '0001_initial'), ]

    operations = [

        migrations.RunPython(

            code=pubmed.db.populate_lookup_tables,
            reverse_code=pubmed.db.unpopulate_lookup_tables,

        ), ]
