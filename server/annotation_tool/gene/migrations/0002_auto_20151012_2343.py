# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gene', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gene',
            name='alias_name',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.CharField(max_length=128)),
        ),
        migrations.AddField(
            model_name='gene',
            name='alias_symbol',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.CharField(max_length=128)),
        ),
        migrations.AddField(
            model_name='gene',
            name='ccds_id',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.CharField(max_length=128)),
        ),
        migrations.AddField(
            model_name='gene',
            name='ena',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.CharField(max_length=128)),
        ),
        migrations.AddField(
            model_name='gene',
            name='enzyme_id',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.CharField(max_length=128)),
        ),
        migrations.AddField(
            model_name='gene',
            name='gene_family',
            field=django.contrib.postgres.fields.ArrayField(default=[], size=None, base_field=models.CharField(null=True, max_length=128)),
        ),
        migrations.AddField(
            model_name='gene',
            name='gene_family_id',
            field=django.contrib.postgres.fields.ArrayField(default=[], size=None, base_field=models.BigIntegerField(null=True)),
        ),
        migrations.AddField(
            model_name='gene',
            name='lsdb',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.CharField(max_length=128)),
        ),
        migrations.AddField(
            model_name='gene',
            name='mgd_id',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.CharField(max_length=128)),
        ),
        migrations.AddField(
            model_name='gene',
            name='omim_id',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.BigIntegerField()),
        ),
        migrations.AddField(
            model_name='gene',
            name='prev_name',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.CharField(max_length=128)),
        ),
        migrations.AddField(
            model_name='gene',
            name='prev_symbol',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.CharField(max_length=128)),
        ),
        migrations.AddField(
            model_name='gene',
            name='pubmed_id',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.BigIntegerField()),
        ),
        migrations.AddField(
            model_name='gene',
            name='refseq_accession',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.CharField(max_length=128)),
        ),
        migrations.AddField(
            model_name='gene',
            name='rgd_id',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.CharField(max_length=128)),
        ),
        migrations.AddField(
            model_name='gene',
            name='uniprot_ids',
            field=django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.CharField(max_length=128)),
        ),
    ]
