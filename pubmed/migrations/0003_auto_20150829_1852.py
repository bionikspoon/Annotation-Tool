# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0002_populate_lookups'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AssessedPatientOutcomeLookup',
        ),
        migrations.DeleteModel(
            name='SignificantPatientOutcomeLookup',
        ),
        migrations.AlterField(
            model_name='entry',
            name='mate_breakend_strand',
            field=models.ForeignKey(related_name='mate_breakend_strand', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed.BreakendStrandLookup'),
        ),
        migrations.DeleteModel(
            name='MateBreakendStrandLookup',
        ),
    ]
