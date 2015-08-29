# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0002_populate_lookups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mate_end',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='mate_start',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='maximum_number_of_copies',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='minimum_number_of_copies',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='population_size',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pubmed_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='start',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='stop',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='variant_clinical_grade',
            field=models.PositiveIntegerField(null=True, blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
