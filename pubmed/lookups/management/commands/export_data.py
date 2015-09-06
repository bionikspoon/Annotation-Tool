#!/usr/bin/env python
# coding=utf-8

from django.core.management.base import NoArgsCommand

from ...migrations.initial_data.build import generate_data


class Command(NoArgsCommand):
    """Generate initial data used to populate lookup tables."""

    def handle_noargs(self, **options):
        generate_data()

    help = __doc__


if __name__ == '__main__':
    Command().handle()
