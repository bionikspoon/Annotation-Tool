# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0003_auto_20151005_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='gene_family',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(null=True, max_length=64), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='gene_family_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(null=True), size=None),
        ),
    ]
