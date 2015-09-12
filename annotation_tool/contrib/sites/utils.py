#!/usr/bin/env python
# coding=utf-8


from django.conf import settings


def update_site_forward(apps, schema_editor):
    """Set site domain and name."""
    Site = apps.get_model("sites", "Site")
    Site.objects.update_or_create(id=settings.SITE_ID, defaults={
        "domain": settings.ALLOWED_HOSTS[0],
        "name": settings.PROJECT_NAME
    })


def update_site_backward(apps, schema_editor):
    """Revert site domain and name to default."""
    Site = apps.get_model("sites", "Site")
    Site.objects.update_or_create(id=settings.SITE_ID, defaults={
        "domain": "example.com",
        "name": "example.com"
    })
