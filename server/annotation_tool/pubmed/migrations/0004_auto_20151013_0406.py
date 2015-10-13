# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0003_auto_20151012_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseaselookup',
            name='created',
        ),
        migrations.RemoveField(
            model_name='diseaselookup',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='mutationtypelookup',
            name='created',
        ),
        migrations.RemoveField(
            model_name='mutationtypelookup',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='patientoutcomeslookup',
            name='created',
        ),
        migrations.RemoveField(
            model_name='patientoutcomeslookup',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='rulelevellookup',
            name='created',
        ),
        migrations.RemoveField(
            model_name='rulelevellookup',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='structurelookup',
            name='created',
        ),
        migrations.RemoveField(
            model_name='structurelookup',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='syntaxlookup',
            name='created',
        ),
        migrations.RemoveField(
            model_name='syntaxlookup',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='variantconsequencelookup',
            name='created',
        ),
        migrations.RemoveField(
            model_name='variantconsequencelookup',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='varianttypelookup',
            name='created',
        ),
        migrations.RemoveField(
            model_name='varianttypelookup',
            name='modified',
        ),
    ]
