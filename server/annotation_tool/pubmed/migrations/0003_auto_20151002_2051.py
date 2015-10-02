# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0002_auto_20151002_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('choice', models.CharField(unique=True, db_index=True, max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RuleLevelLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
            name='mutation_type',
            field=models.ForeignKey(related_name='pubmed_entries', null=True, to='pubmed.MutationTypeLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='rule_level',
            field=models.ForeignKey(related_name='pubmed_entries', null=True, to='pubmed.RuleLevelLookup'),
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
            name='variant_consequence',
            field=models.ForeignKey(related_name='pubmed_entries', null=True, to='pubmed.VariantConsequenceLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='variant_type',
            field=models.ForeignKey(related_name='pubmed_entries', null=True, to='pubmed.VariantTypeLookup'),
        ),
    ]
