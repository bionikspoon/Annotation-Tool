# Compatibility
from __future__ import unicode_literals

# Django Packages
from django.db import migrations

# Local Application
from .initial_data import clean_lookup_tables, populate_lookup_tables


class Migration(migrations.Migration):
    dependencies = [('lookups', '0001_initial'), ]

    operations = [migrations.RunPython(

        code=populate_lookup_tables, reverse_code=clean_lookup_tables,

    )]
