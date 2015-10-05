# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0003_auto_20151005_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='hgnc_id',
            field=models.CharField(primary_key=True, max_length=16, serialize=False),
        ),
        migrations.AlterField(
            model_name='gene',
            name='uuid',
            field=models.UUIDField(db_index=True, unique=True),
        ),
    ]
