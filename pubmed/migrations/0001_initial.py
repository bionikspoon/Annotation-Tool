# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BreakendDirectionLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BreakendStrandLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DiseaseLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('pubmed_id', models.PositiveIntegerField()),
                ('gene', models.CharField(blank=True, max_length=100)),
                ('syntax_text', models.CharField(blank=True, max_length=100)),
                ('chromosome', models.CharField(blank=True, max_length=100)),
                ('start', models.PositiveIntegerField(blank=True, null=True)),
                ('stop', models.PositiveIntegerField(blank=True, null=True)),
                ('mate_chromosome', models.CharField(blank=True, max_length=100)),
                ('mate_start', models.PositiveIntegerField(blank=True, null=True)),
                ('mate_end', models.PositiveIntegerField(blank=True, null=True)),
                ('minimum_number_of_copies', models.PositiveIntegerField(blank=True, null=True)),
                ('maximum_number_of_copies', models.PositiveIntegerField(blank=True, null=True)),
                ('coordinate_predicate', models.CharField(blank=True, max_length=100)),
                ('partner_coordinate_predicate', models.CharField(blank=True, max_length=100)),
                ('variant_clinical_grade', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], blank=True, null=True)),
                ('treatment_1', models.CharField(blank=True, max_length=100)),
                ('treatment_2', models.CharField(blank=True, max_length=100)),
                ('treatment_3', models.CharField(blank=True, max_length=100)),
                ('treatment_4', models.CharField(blank=True, max_length=100)),
                ('treatment_5', models.CharField(blank=True, max_length=100)),
                ('population_size', models.PositiveIntegerField(blank=True, null=True)),
                ('ethnicity', models.CharField(blank=True, max_length=100)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperatorLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientOutcomesLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RuleLevelLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SexLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StructureLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SyntaxLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VariantConsequenceLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VariantTypeLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('choice', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='assessed_patient_outcomes',
            field=models.ManyToManyField(to='pubmed.PatientOutcomesLookup', blank=True, related_name='assessed_patient_outcomes'),
        ),
        migrations.AddField(
            model_name='entry',
            name='breakend_direction',
            field=models.ForeignKey(blank=True, null=True, to='pubmed.BreakendDirectionLookup', on_delete=django.db.models.deletion.SET_NULL, related_name='breakend_direction'),
        ),
        migrations.AddField(
            model_name='entry',
            name='breakend_strand',
            field=models.ForeignKey(blank=True, null=True, to='pubmed.BreakendStrandLookup', on_delete=django.db.models.deletion.SET_NULL, related_name='breakend_strand'),
        ),
        migrations.AddField(
            model_name='entry',
            name='disease',
            field=models.ManyToManyField(blank=True, to='pubmed.DiseaseLookup'),
        ),
        migrations.AddField(
            model_name='entry',
            name='mate_breakend_direction',
            field=models.ForeignKey(blank=True, null=True, to='pubmed.BreakendDirectionLookup', on_delete=django.db.models.deletion.SET_NULL, related_name='mate_breakend_direction'),
        ),
        migrations.AddField(
            model_name='entry',
            name='mate_breakend_strand',
            field=models.ForeignKey(blank=True, null=True, to='pubmed.BreakendStrandLookup', on_delete=django.db.models.deletion.SET_NULL, related_name='mate_breakend_strand'),
        ),
        migrations.AddField(
            model_name='entry',
            name='mutation_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed.MutationTypeLookup'),
        ),
        migrations.AddField(
            model_name='entry',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed.OperatorLookup'),
        ),
        migrations.AddField(
            model_name='entry',
            name='rule_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed.RuleLevelLookup'),
        ),
        migrations.AddField(
            model_name='entry',
            name='sex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed.SexLookup'),
        ),
        migrations.AddField(
            model_name='entry',
            name='significant_patient_outcomes',
            field=models.ManyToManyField(to='pubmed.PatientOutcomesLookup', blank=True, related_name='significant_patient_outcomes'),
        ),
        migrations.AddField(
            model_name='entry',
            name='structure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed.StructureLookup'),
        ),
        migrations.AddField(
            model_name='entry',
            name='syntax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed.SyntaxLookup'),
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT, related_name='pubmed_entries'),
        ),
        migrations.AddField(
            model_name='entry',
            name='variant_consequence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed.VariantConsequenceLookup'),
        ),
        migrations.AddField(
            model_name='entry',
            name='variant_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed.VariantTypeLookup'),
        ),
    ]
