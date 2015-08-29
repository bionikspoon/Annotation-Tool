# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0003_auto_20150829_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='mate_breakend_direction',
            field=models.ForeignKey(to='pubmed.BreakendStrandLookup', on_delete=django.db.models.deletion.SET_NULL, null=True, related_name='mate_breakend_direction', blank=True),
        ),
    ]
