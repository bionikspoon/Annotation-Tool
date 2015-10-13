# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gene', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lsdblookup',
            name='choice',
            field=models.CharField(unique=True, max_length=512, db_index=True),
        ),
    ]
