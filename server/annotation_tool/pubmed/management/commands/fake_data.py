from django.core.management.base import BaseCommand

from ...factories import PubmedFactory
from ...models import Pubmed
from ....users.factories import UserFactory
from ....users.models import User


class Command(BaseCommand):
    """Populate fake data."""
    help = __doc__

    def add_arguments(self, parser):
        """:type parser: django.core.management.base.CommandParser"""
        parser.add_argument('--scale', '-s', default=1, type=int, help="Multiplier for record generation.")

    def handle(self, *args, **options):
        scale = options.get('scale') * 10
        user_multiplier = 1
        pubmed_multiplier = 3

        admin = User.objects.filter(username='admin').first()
        if not admin:
            admin = User.objects.create_superuser('admin', 'admin@anno.com', 'secret')
            print('Admin user created:', admin)

        users = UserFactory.create_batch(scale * user_multiplier)
        entries = PubmedFactory.create_batch(scale * pubmed_multiplier)

        print('%s random users created.  %s Total' % (len(users), User.objects.count()))
        print('%s pubmed entries created.  %s Total' % (len(entries), Pubmed.objects.count()))
