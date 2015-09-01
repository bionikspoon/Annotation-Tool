# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='assessed_patient_outcomes',
            field=models.ManyToManyField(blank=True, to='pubmed_lookup.PatientOutcomesLookup', related_name='assessed_patient_outcomes_entry_set'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='breakend_direction',
            field=models.ForeignKey(null=True, to='pubmed_lookup.BreakendDirectionLookup', on_delete=django.db.models.deletion.SET_NULL, related_name='breakend_direction_entry_set', blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='breakend_strand',
            field=models.ForeignKey(null=True, to='pubmed_lookup.BreakendStrandLookup', on_delete=django.db.models.deletion.SET_NULL, related_name='breakend_strand_entry_set', blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='mate_breakend_direction',
            field=models.ForeignKey(null=True, to='pubmed_lookup.BreakendDirectionLookup', on_delete=django.db.models.deletion.SET_NULL, related_name='mate_breakend_direction_entry_set', blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='mate_breakend_strand',
            field=models.ForeignKey(null=True, to='pubmed_lookup.BreakendStrandLookup', on_delete=django.db.models.deletion.SET_NULL, related_name='mate_breakend_strand_entry_set', blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='significant_patient_outcomes',
            field=models.ManyToManyField(blank=True, to='pubmed_lookup.PatientOutcomesLookup', related_name='significant_patient_outcomes_entry_set'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, related_name='entry_set'),
        ),
    ]
