# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0004_auto_20151005_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='gene',
            name='homeodb',
            field=models.BigIntegerField(default=datetime.datetime(2015, 10, 5, 9, 26, 38, 623222, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gene',
            name='kznf_gene_catalog',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gene',
            name='lncrnadb',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gene',
            name='entrez_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='gene',
            name='gene_family_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='hgnc_id',
            field=models.CharField(db_index=True, unique=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='gene',
            name='omim_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='pubmed_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='uuid',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gene',
            name='version',
            field=models.BigIntegerField(),
        ),
    ]
