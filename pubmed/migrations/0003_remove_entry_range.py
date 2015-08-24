# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0002_auto_20150824_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='range',
        ),
    ]
