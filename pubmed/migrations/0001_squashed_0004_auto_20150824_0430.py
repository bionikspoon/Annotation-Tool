# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone
from django.conf import settings
import django.db.models.deletion
import pubmed.db.initial_data


class Migration(migrations.Migration):

    replaces = [('pubmed', '0001_initial'), ('pubmed', '0002_initial_data'), ('pubmed', '0003_auto_20150824_0419'), ('pubmed', '0004_auto_20150824_0430')]

    dependencies = [

        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [

        migrations.CreateModel(
            name='AssessedPatientOutcomeLookup',
            fields=[

                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('choice', models.CharField(max_length=100, unique=True)),

            ],
            options={
                'abstract': False,
            },
        ),

        migrations.CreateModel(
            name='BreakendDirectionLookup',
            fields=[

                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
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
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
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
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('pubmed_id', models.IntegerField()),
                ('gene', models.CharField(max_length=100, blank=True)),
                ('syntax_text', models.CharField(max_length=100, blank=True)),
                ('chromosome', models.CharField(max_length=100, blank=True)),
                ('start', models.IntegerField(null=True, blank=True)),
                ('stop', models.IntegerField(null=True, blank=True)),
                ('mate_chromosome', models.CharField(max_length=100, blank=True)),
                ('mate_start', models.IntegerField(null=True, blank=True)),
                ('mate_end', models.IntegerField(null=True, blank=True)),
                ('minimum_number_of_copies', models.IntegerField(null=True, blank=True)),
                ('maximum_number_of_copies', models.IntegerField(null=True, blank=True)),
                ('coordinate_predicate', models.CharField(max_length=100, blank=True)),
                ('partner_coordinate_predicate', models.CharField(max_length=100, blank=True)),
                ('variant_clinical_grade', models.IntegerField(null=True, blank=True)),
                ('disease', models.CharField(max_length=100, blank=True)),
                ('treatment_1', models.CharField(max_length=100, blank=True)),
                ('treatment_2', models.CharField(max_length=100, blank=True)),
                ('treatment_3', models.CharField(max_length=100, blank=True)),
                ('treatment_4', models.CharField(max_length=100, blank=True)),
                ('treatment_5', models.CharField(max_length=100, blank=True)),
                ('population_size', models.IntegerField(null=True, blank=True)),
                ('ethnicity', models.CharField(max_length=100, blank=True)),
                ('design', models.TextField(blank=True)),
                ('reference_claims', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='pubmed_entries', on_delete=django.db.models.deletion.PROTECT, editable=False)),

            ],
            options={
                'abstract': False,
            },
        ),

        migrations.CreateModel(
            name='MateBreakendStrandLookup',
            fields=[

                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('choice', models.CharField(max_length=100, unique=True)),

            ],
            options={
                'abstract': False,
            },
        ),

        migrations.CreateModel(
            name='MutationTypeLookup',
            fields=[

                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
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
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
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
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
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
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('choice', models.CharField(max_length=100, unique=True)),

            ],
            options={
                'abstract': False,
            },
        ),

        migrations.CreateModel(
            name='SignificantPatientOutcomeLookup',
            fields=[

                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
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
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
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
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
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
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
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
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('choice', models.CharField(max_length=100, unique=True)),

            ],
            options={
                'abstract': False,
            },
        ),

        migrations.AddField(
            model_name='entry',
            name='breakend_direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='pubmed.BreakendDirectionLookup', null=True),
        ),

        migrations.AddField(
            model_name='entry',
            name='breakend_strand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='pubmed.BreakendStrandLookup', null=True),
        ),

        migrations.AddField(
            model_name='entry',
            name='mate_breakend_strand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='pubmed.MateBreakendStrandLookup', null=True),
        ),

        migrations.AddField(
            model_name='entry',
            name='mutation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='pubmed.MutationTypeLookup', null=True),
        ),

        migrations.AddField(
            model_name='entry',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='pubmed.OperatorLookup', null=True),
        ),

        migrations.AddField(
            model_name='entry',
            name='rule_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='pubmed.RuleLevelLookup', null=True),
        ),

        migrations.AddField(
            model_name='entry',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='pubmed.SexLookup', null=True),
        ),

        migrations.AddField(
            model_name='entry',
            name='structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='pubmed.StructureLookup', null=True),
        ),

        migrations.AddField(
            model_name='entry',
            name='syntax',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='pubmed.SyntaxLookup', null=True),
        ),

        migrations.AddField(
            model_name='entry',
            name='variant_consequence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='pubmed.VariantConsequenceLookup', null=True),
        ),

        migrations.AddField(
            model_name='entry',
            name='variant_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='pubmed.VariantTypeLookup', null=True),
        ),

        migrations.AddField(
            model_name='entry',
            name='assessed_patient_outcomes',
            field=models.ManyToManyField(blank=True, to='pubmed.AssessedPatientOutcomeLookup'),
        ),

        migrations.AddField(
            model_name='entry',
            name='significant_patient_outcomes',
            field=models.ManyToManyField(blank=True, to='pubmed.SignificantPatientOutcomeLookup'),
        ),

        migrations.RunPython(
            code=pubmed.db.populate_lookup_tables, ),

    ]
