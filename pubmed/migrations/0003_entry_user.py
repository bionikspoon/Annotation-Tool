# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pubmed', '0002_auto_20150823_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(related_name='pubmed_entries', to=settings.AUTH_USER_MODEL, editable=False, default=1),
            preserve_default=False,
        ),
    ]
