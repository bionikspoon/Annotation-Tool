# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0005_auto_20151005_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='refseq_accession',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.CharField(max_length=64)),
        ),
    ]
