# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('pubmed_id', models.IntegerField(unique=True)),
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
                ('design', models.TextField()),
                ('reference_claims', models.TextField()),
                ('comments', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
