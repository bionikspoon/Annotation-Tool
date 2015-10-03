# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0003_auto_20151002_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='pubmed',
            name='assessed_patient_outcomes',
            field=models.ManyToManyField(blank=True, to='pubmed.PatientOutcomesLookup', related_name='assessed_patient_outcomes_entry_set'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='disease',
            field=models.ManyToManyField(blank=True, to='pubmed.DiseaseLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='significant_patient_outcomes',
            field=models.ManyToManyField(blank=True, to='pubmed.PatientOutcomesLookup', related_name='significant_patient_outcomes_entry_set'),
        ),
        migrations.AlterField(
            model_name='pubmed',
            name='breakend_direction',
            field=models.CharField(blank=True, choices=[('LEFT', 'Left'), ('RIGHT', 'Right')], max_length=32),
        ),
        migrations.AlterField(
            model_name='pubmed',
            name='breakend_strand',
            field=models.CharField(blank=True, choices=[('FORWARD', 'Forward'), ('REVERSE', 'Reverse')], max_length=32),
        ),
        migrations.AlterField(
            model_name='pubmed',
            name='operator',
            field=models.CharField(blank=True, choices=[('CONTAINS', 'Contains'), ('NOT CONTAINS', 'Not Contains')], max_length=32),
        ),
        migrations.AlterField(
            model_name='pubmed',
            name='sex',
            field=models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('MIXED', 'Mixed'), ('UNKNOWN', 'Unknown')], max_length=32),
        ),
    ]
