"""
Initialize user data.
"""

from functools import wraps
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

PERMISSION = {
    'annotator': ['add_pubmed'],
    'admin': ['add_diseaselookup', 'change_diseaselookup', 'delete_diseaselookup', 'add_mutationtypelookup',
              'change_mutationtypelookup', 'custom_add_mutationtypelookup', 'custom_change_mutationtypelookup',
              'delete_mutationtypelookup', 'add_patientoutcomeslookup', 'change_patientoutcomeslookup',
              'delete_patientoutcomeslookup', 'add_pubmed', 'change_pubmed', 'delete_pubmed', 'add_rulelevellookup',
              'change_rulelevellookup', 'delete_rulelevellookup', 'add_structurelookup', 'change_structurelookup',
              'custom_add_structurelookup', 'custom_change_structurelookup', 'delete_structurelookup',
              'add_syntaxlookup', 'change_syntaxlookup', 'delete_syntaxlookup', 'add_variantconsequencelookup',
              'change_variantconsequencelookup', 'delete_variantconsequencelookup', 'add_varianttypelookup',
              'change_varianttypelookup', 'delete_varianttypelookup']

}
"""Global config manifest"""


def stats(*, query=None):
    """
    Collect before and after counts for queryset.

    :param  django.db.models.Manager or None query: Manager used to `.count()`.
    :return: Before/after count delta.
    """

    # noinspection PyDocstring
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            """
            Method decorator.  Collect and return before/after stats.

            :param self:
            :param args: `func` args
            :param kwargs: `func` kwargs
            :return: Before/after count delta.
            """
            _query = kwargs.get('query', query)
            """:type django.db.models.Manager"""
            if _query is None:
                raise NotImplementedError('`query` must be passed in via decorator or kwargs')

            before_count = _query.count()
            func(self, *args, **kwargs)
            return abs(before_count - _query.count())

        return wrapper

    return decorator


class Command(BaseCommand):
    """Initial user data."""
    help = __doc__
    sync = NotImplemented

    def add_arguments(self, parser):
        """
        Command arguments.

        :param django.core.management.base.CommandParser parser: Parse arguments.
        """
        parser.add_argument('--sync', '-s', default=False, action='store_true',
                            help="Only build from source. Skip import.")

    def handle(self, *args, **options):
        """
        Execute main command.

        :param args:
        :param options:
        """
        self.sync = options['sync']

        # Run queries, collect stats.
        added_count = self.create_all_groups()
        removed_count = self.sync_all_groups()

        # Print stats
        added_msg = '%s groups created. ' % added_count
        removed_msg = '%s groups removed. ' % removed_count if self.sync else ''
        total_count = Group.objects.count()
        print('%s%s%s total' % (added_msg, removed_msg, total_count))

    def create_group(self, name, permissions_list):
        """
        Create group with permissions.

        :param str name: Group name.
        :param [str] permissions_list: List of permissions to add to group.
        :return: None
        """
        if not self.sync and Group.objects.filter(name=name).exists():
            return

        # Collect models
        permissions = Permission.objects.filter(codename__in=permissions_list).iterator()
        group, created = Group.objects.get_or_create(name=name)

        # Update models, collect stats
        added_count = self.set_group_permissions(permissions, created, query=group.permissions)
        group.save()

        # Print stats
        total_count = group.permissions.count()
        print('%r group saved. Added %s new permissions (%s total).' % (group.name, added_count, total_count))

    @stats()
    def set_group_permissions(self, permissions, created, *, query):
        """
        Add permissions to group.

        :param [str] permissions: List of permissions to add to group.
        :param bool created: Object is new.
        :param django.db.models.fields.related.ManyRelatedManager query: Manager instance of group permissions.
        :return: None
        :rtype: None
        """
        if not created:
            query.clear()
        query.add(*permissions)

    @stats(query=Group.objects)
    def create_all_groups(self):
        """
        Create each group in global `PERMISSION` config object.

        :return: None
        :rtype: None
        """
        for name, permissions in PERMISSION.items():
            self.create_group(name, permissions)

    @stats(query=Group.objects)
    def sync_all_groups(self):
        """
        Remove objects not in global `PERMISSION` config object.

        :return: None
        :rtype: None
        """
        if self.sync:
            Group.objects.exclude(name__in=PERMISSION.keys()).delete()
