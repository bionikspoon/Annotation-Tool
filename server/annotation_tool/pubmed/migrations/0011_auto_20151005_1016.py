# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0010_auto_20151005_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='lncrnadb',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
