from django.core.management.base import BaseCommand

from server.annotation_tool.pubmed.factories import PubmedFactory
from server.annotation_tool.pubmed.models import Pubmed


class Command(BaseCommand):
    """Populate fake data."""
    help = __doc__

    def add_arguments(self, parser):
        """:type parser: django.core.management.base.CommandParser"""
        parser.add_argument('--scale', '-s', default=1, type=int, help="Multiplier for record generation.")

    def handle(self, *args, **options):
        scale = options.get('scale')
        base = 20
        for _ in range(base * scale):
            PubmedFactory.create()

        print('%s Pubmed entries created.  %s Total' % (base * scale, Pubmed.objects.count()))
