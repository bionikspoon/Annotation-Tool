# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='design',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pubmed_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='reference_claims',
            field=models.TextField(blank=True),
        ),
    ]
