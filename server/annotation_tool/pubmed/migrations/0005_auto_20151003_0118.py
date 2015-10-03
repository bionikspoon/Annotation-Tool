# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0004_auto_20151003_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='pubmed',
            name='mate_breakend_direction',
            field=models.CharField(choices=[('LEFT', 'Left'), ('RIGHT', 'Right')], blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='mate_breakend_strand',
            field=models.CharField(choices=[('FORWARD', 'Forward'), ('REVERSE', 'Reverse')], blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='partner_coordinate_predicate',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='pubmed',
            name='assessed_patient_outcomes',
            field=models.ManyToManyField(related_name='assessed_patient_outcomes_pubmed_entries', blank=True, to='pubmed.PatientOutcomesLookup'),
        ),
        migrations.AlterField(
            model_name='pubmed',
            name='significant_patient_outcomes',
            field=models.ManyToManyField(related_name='significant_patient_outcomes_pubmed_entries', blank=True, to='pubmed.PatientOutcomesLookup'),
        ),
    ]
