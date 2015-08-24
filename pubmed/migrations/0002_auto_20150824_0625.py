# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.ranges


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0001_squashed_0004_auto_20150824_0430'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'Entries'},
        ),
        migrations.AddField(
            model_name='entry',
            name='range',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(null=True, blank=True),
        ),
    ]
