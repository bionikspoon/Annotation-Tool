# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import django.contrib.postgres.fields.ranges
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pubmed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pubmed',
            name='breakend_direction',
            field=models.CharField(choices=[('Left', 'Left'), ('Right', 'Right')], max_length=32, blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='breakend_strand',
            field=models.CharField(choices=[('Forward', 'Forward'), ('Reverse', 'Reverse')], max_length=32, blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='chromosome_range',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='coordinate_predicate',
            field=models.CharField(max_length=32, blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='ethnicity',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='mate_chromosome',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='mate_chromosome_range',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='number_of_copies',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='operator',
            field=models.CharField(choices=[('Contains', 'Contains'), ('Not Contains', 'Not Contains')], max_length=32, blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='population_size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='reference_claims',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Mixed', 'Mixed'), ('Unknown', 'Unknown')], max_length=32, blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='study_design',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='syntax_text',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='treatment_number_of_arms',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1, related_name='pubmed_entries'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pubmed',
            name='variant_clinical_grade',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], blank=True, null=True),
        ),
    ]
