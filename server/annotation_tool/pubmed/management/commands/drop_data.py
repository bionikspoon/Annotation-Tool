from django.core.management.base import BaseCommand

from ...models import Pubmed
from ....users.models import User


class Command(BaseCommand):
    """Drop pubmed data."""
    help = __doc__

    def handle(self, *args, **options):
        print('Dropping %s pubmed entries.' % Pubmed.objects.count())
        Pubmed.objects.all().delete()

        print('Dropping %s users.' % User.objects.exclude(username='admin').count())
        User.objects.exclude(username='admin').delete()

        msg = 'Refresh complete.  Currently %s pubmed entries and %s users'
        print(msg % (Pubmed.objects.count(), User.objects.count()))
