#!/usr/bin/env python
# coding=utf-8
import random

from factory import PostGeneration, LazyAttribute
from model_utils import Choices


def _upper_or_int(arg):
    try:
        return arg.upper()
    except AttributeError:
        return arg


def choices(*args):
    return Choices(*((_upper_or_int(arg), arg) for arg in args))


def make(field, **kwargs):
    return LazyAttribute(lambda _: field(**kwargs))


def many_to_many(model, name):
    def wrapper(self, create, extracted, **_):
        field = getattr(self, name)
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for item in extracted:
                field.add(item)

        else:
            items = model.objects.all()
            ids = [item.id for item in items]
            number_of_items_to_add = random.randint(1, len(ids))
            for _ in range(number_of_items_to_add):
                field.add(random.choice(ids))

    return PostGeneration(wrapper)
