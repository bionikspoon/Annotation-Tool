# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssessedPatientOutcomeLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BreakendDirectionLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BreakendStrandLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DiseaseLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
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
                ('variant_clinical_grade', models.PositiveIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
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
            name='MateBreakendStrandLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MutationTypeLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperatorLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientOutcomeLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RuleLevelLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SexLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SignificantPatientOutcomeLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StructureLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SyntaxLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VariantConsequenceLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VariantTypeLookup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('choice', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='assessed_patient_outcomes',
            field=models.ManyToManyField(related_name='assessed_patient_outcomes', blank=True, to='pubmed.PatientOutcomeLookup'),
        ),
        migrations.AddField(
            model_name='entry',
            name='breakend_direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='pubmed.BreakendDirectionLookup', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='breakend_strand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='pubmed.BreakendStrandLookup', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='disease',
            field=models.ManyToManyField(blank=True, to='pubmed.DiseaseLookup'),
        ),
        migrations.AddField(
            model_name='entry',
            name='mate_breakend_strand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='pubmed.MateBreakendStrandLookup', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='mutation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='pubmed.MutationTypeLookup', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='pubmed.OperatorLookup', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='rule_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='pubmed.RuleLevelLookup', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='pubmed.SexLookup', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='significant_patient_outcomes',
            field=models.ManyToManyField(related_name='significant_patient_outcomes', blank=True, to='pubmed.PatientOutcomeLookup'),
        ),
        migrations.AddField(
            model_name='entry',
            name='structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='pubmed.StructureLookup', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='syntax',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='pubmed.SyntaxLookup', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, editable=False, related_name='pubmed_entries'),
        ),
        migrations.AddField(
            model_name='entry',
            name='variant_consequence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='pubmed.VariantConsequenceLookup', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='variant_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='pubmed.VariantTypeLookup', blank=True, null=True),
        ),
    ]
