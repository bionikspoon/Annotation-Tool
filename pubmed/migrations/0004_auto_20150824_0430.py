# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0003_auto_20150824_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='assessed_patient_outcomes',
            field=models.ManyToManyField(to='pubmed.AssessedPatientOutcomeLookup', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='significant_patient_outcomes',
            field=models.ManyToManyField(to='pubmed.SignificantPatientOutcomeLookup', blank=True),
        ),
    ]
