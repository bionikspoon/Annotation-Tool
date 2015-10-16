from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Initial user data."""
    help = __doc__

    def handle(self, *args, **options):
        self.create_annotator_group()

    def create_annotator_group(self):
        name = 'annotator'
        if Group.objects.filter(name=name).exists():
            return

        add_pubmed = Permission.objects.filter(codename='add_pubmed').first()

        annotator = Group(name=name).save()
        annotator.permissions.add(add_pubmed).save()
