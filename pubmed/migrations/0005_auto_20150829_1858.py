# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0004_entry_mate_breakend_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mate_breakend_direction',
            field=models.ForeignKey(null=True, to='pubmed.BreakendDirectionLookup', blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mate_breakend_direction'),
        ),
    ]
