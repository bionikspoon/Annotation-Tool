# Compatibility
from __future__ import unicode_literals

# Django Packages
from django.db import migrations

# Local Application
from . import update_site_backward, update_site_forward


class Migration(migrations.Migration):
    dependencies = [('sites', '0001_initial'), ]

    operations = [migrations.RunPython(update_site_forward, update_site_backward)]
