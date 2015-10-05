# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0002_auto_20151005_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='ccds_id',
            field=django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=32), size=None),
        ),
    ]
