# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0006_auto_20151005_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='date_approved_reserved',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='date_modified',
            field=models.DateTimeField(null=True),
        ),
    ]
