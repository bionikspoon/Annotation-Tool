# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.core.validators
import django.contrib.postgres.fields.ranges
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('choice', models.CharField(unique=True, db_index=True, max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MutationTypeLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('choice', models.CharField(unique=True, db_index=True, max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientOutcomesLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('choice', models.CharField(unique=True, db_index=True, max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pubmed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('pubmed_id', models.PositiveIntegerField(db_index=True)),
                ('gene', models.CharField(max_length=128, blank=True)),
                ('syntax_text', models.CharField(max_length=128, blank=True)),
                ('operator', models.CharField(choices=[('CONTAINS', 'Contains'), ('NOT CONTAINS', 'Not Contains')], max_length=32, blank=True)),
                ('chromosome', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23)], validators=[django.core.validators.MaxValueValidator(23)], null=True, blank=True)),
                ('chromosome_range', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True, blank=True)),
                ('breakend_strand', models.CharField(choices=[('FORWARD', 'Forward'), ('REVERSE', 'Reverse')], max_length=32, blank=True)),
                ('breakend_direction', models.CharField(choices=[('LEFT', 'Left'), ('RIGHT', 'Right')], max_length=32, blank=True)),
                ('mate_chromosome', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23)], validators=[django.core.validators.MaxValueValidator(23)], null=True, blank=True)),
                ('mate_chromosome_range', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True, blank=True)),
                ('mate_breakend_strand', models.CharField(choices=[('FORWARD', 'Forward'), ('REVERSE', 'Reverse')], max_length=32, blank=True)),
                ('mate_breakend_direction', models.CharField(choices=[('LEFT', 'Left'), ('RIGHT', 'Right')], max_length=32, blank=True)),
                ('number_of_copies', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True, blank=True)),
                ('coordinate_predicate', models.CharField(max_length=32, blank=True)),
                ('partner_coordinate_predicate', models.CharField(max_length=32, blank=True)),
                ('variant_clinical_grade', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], validators=[django.core.validators.MaxValueValidator(5)], null=True, blank=True)),
                ('treatment_number_of_arms', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], validators=[django.core.validators.MaxValueValidator(5)], null=True, blank=True)),
                ('population_size', models.PositiveIntegerField(null=True, blank=True)),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('MIXED', 'Mixed'), ('UNKNOWN', 'Unknown')], max_length=32, blank=True)),
                ('ethnicity', models.CharField(max_length=128, blank=True)),
                ('study_design', models.TextField(blank=True)),
                ('reference_claims', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('assessed_patient_outcomes', models.ManyToManyField(related_name='assessed_patient_outcomes_pubmed_entries', blank=True, to='pubmed.PatientOutcomesLookup')),
                ('disease', models.ManyToManyField(related_name='pubmed_entries', blank=True, to='pubmed.DiseaseLookup')),
                ('mutation_type', models.ForeignKey(related_name='pubmed_entries', null=True, to='pubmed.MutationTypeLookup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RuleLevelLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('choice', models.CharField(unique=True, db_index=True, max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StructureLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('choice', models.CharField(unique=True, db_index=True, max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SyntaxLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('choice', models.CharField(unique=True, db_index=True, max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VariantConsequenceLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('choice', models.CharField(unique=True, db_index=True, max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VariantTypeLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('choice', models.CharField(unique=True, db_index=True, max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pubmed',
            name='rule_level',
            field=models.ForeignKey(related_name='pubmed_entries', null=True, to='pubmed.RuleLevelLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='significant_patient_outcomes',
            field=models.ManyToManyField(related_name='significant_patient_outcomes_pubmed_entries', blank=True, to='pubmed.PatientOutcomesLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='structure',
            field=models.ForeignKey(related_name='pubmed_entries', null=True, to='pubmed.StructureLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='syntax',
            field=models.ForeignKey(related_name='pubmed_entries', null=True, to='pubmed.SyntaxLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='user',
            field=models.ForeignKey(related_name='pubmed_entries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='variant_consequence',
            field=models.ForeignKey(related_name='pubmed_entries', null=True, to='pubmed.VariantConsequenceLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='variant_type',
            field=models.ForeignKey(related_name='pubmed_entries', null=True, to='pubmed.VariantTypeLookup'),
        ),
    ]
