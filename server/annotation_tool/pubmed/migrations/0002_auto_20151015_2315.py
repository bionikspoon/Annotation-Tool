# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mutationtypelookup',
            options={'default_permissions': ('custom_add', 'custom_change', 'delete')},
        ),
        migrations.AlterModelOptions(
            name='structurelookup',
            options={'default_permissions': ('custom_add', 'custom_change', 'delete')},
        ),
    ]
