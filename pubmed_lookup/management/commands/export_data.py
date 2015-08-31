#!/usr/bin/env python
# coding=utf-8

from django.core.management.base import BaseCommand

from ...migrations.initial_data.build import generate_data


class Command(BaseCommand):
    help = "Generate initial data used to populate lookup tables."

    def handle(self, *args, **options):
        generate_data()


if __name__ == '__main__':
    Command().handle()
