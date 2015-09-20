# Compatibility
from __future__ import unicode_literals

# Django Packages
from django.db import migrations

# Annotation Tool Project


class Migration(migrations.Migration):
    dependencies = [('lookups', '0001_initial'), ]

    operations = [migrations.RunPython(

        code=lookups.migrations.initial_data.populate_lookup_tables,
        reverse_code=lookups.migrations.initial_data.clean_lookup_tables,

    )]
