# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
from django.conf import settings
import django.utils.timezone
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BreakendDirectionLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BreakendStrandLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DiseaseLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('pubmed_id', models.PositiveIntegerField()),
                ('gene', models.CharField(max_length=100, blank=True)),
                ('syntax_text', models.CharField(max_length=100, blank=True)),
                ('chromosome', models.CharField(max_length=100, blank=True)),
                ('start', models.PositiveIntegerField(null=True, blank=True)),
                ('stop', models.PositiveIntegerField(null=True, blank=True)),
                ('mate_chromosome', models.CharField(max_length=100, blank=True)),
                ('mate_start', models.PositiveIntegerField(null=True, blank=True)),
                ('mate_end', models.PositiveIntegerField(null=True, blank=True)),
                ('minimum_number_of_copies', models.PositiveIntegerField(null=True, blank=True)),
                ('maximum_number_of_copies', models.PositiveIntegerField(null=True, blank=True)),
                ('coordinate_predicate', models.CharField(max_length=100, blank=True)),
                ('partner_coordinate_predicate', models.CharField(max_length=100, blank=True)),
                ('variant_clinical_grade', models.PositiveIntegerField(null=True, blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('treatment_1', models.CharField(max_length=100, blank=True)),
                ('treatment_2', models.CharField(max_length=100, blank=True)),
                ('treatment_3', models.CharField(max_length=100, blank=True)),
                ('treatment_4', models.CharField(max_length=100, blank=True)),
                ('treatment_5', models.CharField(max_length=100, blank=True)),
                ('population_size', models.PositiveIntegerField(null=True, blank=True)),
                ('ethnicity', models.CharField(max_length=100, blank=True)),
                ('design', models.TextField(blank=True)),
                ('reference_claims', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Entries',
            },
        ),
        migrations.CreateModel(
            name='MutationTypeLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperatorLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientOutcomeLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RuleLevelLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SexLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StructureLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SyntaxLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VariantConsequenceLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VariantTypeLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='assessed_patient_outcomes',
            field=models.ManyToManyField(blank=True, to='pubmed.PatientOutcomeLookup', related_name='assessed_patient_outcomes'),
        ),
        migrations.AddField(
            model_name='entry',
            name='breakend_direction',
            field=models.ForeignKey(to='pubmed.BreakendDirectionLookup', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='entry',
            name='breakend_strand',
            field=models.ForeignKey(to='pubmed.BreakendStrandLookup', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='entry',
            name='disease',
            field=models.ManyToManyField(blank=True, to='pubmed.DiseaseLookup'),
        ),
        migrations.AddField(
            model_name='entry',
            name='mate_breakend_direction',
            field=models.ForeignKey(to='pubmed.BreakendDirectionLookup', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mate_breakend_direction'),
        ),
        migrations.AddField(
            model_name='entry',
            name='mate_breakend_strand',
            field=models.ForeignKey(to='pubmed.BreakendStrandLookup', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mate_breakend_strand'),
        ),
        migrations.AddField(
            model_name='entry',
            name='mutation_type',
            field=models.ForeignKey(to='pubmed.MutationTypeLookup', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='entry',
            name='operator',
            field=models.ForeignKey(to='pubmed.OperatorLookup', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='entry',
            name='rule_level',
            field=models.ForeignKey(to='pubmed.RuleLevelLookup', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='entry',
            name='sex',
            field=models.ForeignKey(to='pubmed.SexLookup', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='entry',
            name='significant_patient_outcomes',
            field=models.ManyToManyField(blank=True, to='pubmed.PatientOutcomeLookup', related_name='significant_patient_outcomes'),
        ),
        migrations.AddField(
            model_name='entry',
            name='structure',
            field=models.ForeignKey(to='pubmed.StructureLookup', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='entry',
            name='syntax',
            field=models.ForeignKey(to='pubmed.SyntaxLookup', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='pubmed_entries'),
        ),
        migrations.AddField(
            model_name='entry',
            name='variant_consequence',
            field=models.ForeignKey(to='pubmed.VariantConsequenceLookup', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='entry',
            name='variant_type',
            field=models.ForeignKey(to='pubmed.VariantTypeLookup', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
