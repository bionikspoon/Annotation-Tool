# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0002_gene'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='date_approved_reserved',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='gene',
            name='date_modified',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='gene',
            name='date_name_changed',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='gene',
            name='date_symbol_changed',
            field=models.DateTimeField(),
        ),
    ]
