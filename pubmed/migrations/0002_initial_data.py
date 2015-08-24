# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from pubmed.db.initial_data import populate_lookup_tables


class Migration(migrations.Migration):

    operations = [migrations.RunPython(populate_lookup_tables)

                  ]
