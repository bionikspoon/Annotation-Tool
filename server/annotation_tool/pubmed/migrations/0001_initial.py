# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import server.annotation_tool.utils.models
import django.utils.timezone
from django.conf import settings
import django.core.validators
import model_utils.fields
import django.contrib.postgres.fields.ranges


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('choice', models.CharField(unique=True, max_length=128, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MutationTypeLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('choice', models.CharField(unique=True, max_length=128, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PatientOutcomesLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('choice', models.CharField(unique=True, max_length=128, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Pubmed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('pubmed_id', models.PositiveIntegerField(db_index=True)),
                ('gene', models.CharField(blank=True, max_length=128)),
                ('syntax_text', models.CharField(blank=True, max_length=128)),
                ('operator', models.CharField(blank=True, max_length=32, choices=[('CONTAINS', 'Contains'), ('NOT CONTAINS', 'Not Contains')])),
                ('chromosome', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(23)], blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23)])),
                ('chromosome_range', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True, blank=True)),
                ('breakend_strand', models.CharField(blank=True, max_length=32, choices=[('FORWARD', 'Forward'), ('REVERSE', 'Reverse')])),
                ('breakend_direction', models.CharField(blank=True, max_length=32, choices=[('LEFT', 'Left'), ('RIGHT', 'Right')])),
                ('mate_chromosome', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(23)], blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23)])),
                ('mate_chromosome_range', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True, blank=True)),
                ('mate_breakend_strand', models.CharField(blank=True, max_length=32, choices=[('FORWARD', 'Forward'), ('REVERSE', 'Reverse')])),
                ('mate_breakend_direction', models.CharField(blank=True, max_length=32, choices=[('LEFT', 'Left'), ('RIGHT', 'Right')])),
                ('number_of_copies', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True, blank=True)),
                ('coordinate_predicate', models.CharField(blank=True, max_length=32)),
                ('partner_coordinate_predicate', models.CharField(blank=True, max_length=32)),
                ('variant_clinical_grade', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(5)], blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('treatment_number_of_arms', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(5)], blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('population_size', models.PositiveIntegerField(null=True, blank=True)),
                ('sex', models.CharField(blank=True, max_length=32, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('MIXED', 'Mixed'), ('UNKNOWN', 'Unknown')])),
                ('ethnicity', models.CharField(blank=True, max_length=128)),
                ('study_design', models.TextField(blank=True)),
                ('reference_claims', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('assessed_patient_outcomes', models.ManyToManyField(related_name='assessed_patient_outcomes_pubmed_entries', blank=True, to='pubmed.PatientOutcomesLookup')),
                ('disease', models.ManyToManyField(related_name='pubmed_entries', blank=True, to='pubmed.DiseaseLookup')),
                ('mutation_type', models.ForeignKey(null=True, related_name='pubmed_entries', to='pubmed.MutationTypeLookup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RuleLevelLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('choice', models.CharField(unique=True, max_length=128, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StructureLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('choice', models.CharField(unique=True, max_length=128, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SyntaxLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('choice', models.CharField(unique=True, max_length=128, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='VariantConsequenceLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('choice', models.CharField(unique=True, max_length=128, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='VariantTypeLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('choice', models.CharField(unique=True, max_length=128, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='rule_level',
            field=models.ForeignKey(null=True, related_name='pubmed_entries', to='pubmed.RuleLevelLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='significant_patient_outcomes',
            field=models.ManyToManyField(related_name='significant_patient_outcomes_pubmed_entries', blank=True, to='pubmed.PatientOutcomesLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='structure',
            field=models.ForeignKey(null=True, related_name='pubmed_entries', to='pubmed.StructureLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='syntax',
            field=models.ForeignKey(null=True, related_name='pubmed_entries', to='pubmed.SyntaxLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='pubmed_entries'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='variant_consequence',
            field=models.ForeignKey(null=True, related_name='pubmed_entries', to='pubmed.VariantConsequenceLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='variant_type',
            field=models.ForeignKey(null=True, related_name='pubmed_entries', to='pubmed.VariantTypeLookup'),
        ),
    ]
