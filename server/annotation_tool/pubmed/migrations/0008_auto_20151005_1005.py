# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0007_auto_20151005_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='entrez_id',
            field=models.BigIntegerField(null=True),
        ),
    ]
