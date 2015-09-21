# Python Libraries
import re

# Django Packages
from django import template

register = template.Library()

_re_camel_humps = re.compile('([a-z])([A-Z0-9])')
"""
Match camel case word separators.

Note: Numbers are treated like capital letters.

For example:

>>> _re_camel_humps.findall('CamelCaseExample1')
[('l', 'C'), ('e', 'E'), ('e', '1')]

>>> _re_camel_humps.sub(r'\1-\2', 'CamelCaseExample1')
'Camel-Case-Example-1'

"""
_to_kabob = r'\1-\2'
"""Replacement pattern for `re.sub`"""


@register.simple_tag
def css_class(*class_list, **class_bools):
    """
    Create a css class attribute block from a list of classes and conditional classes.

    For example:

    {% css_class 'form-group' %}
    renders: `class="form-group"`

    {% css_class required=True %}
    renders: `class="required"`

    {% css_class 'form-group' hasErrors=field.errors %}
    if `field.errors` is True, renders: `class="form-group has-errors"`
    else renders: `class="form-group"`

    Practical Example with crispy_forms:

    {% css_class 'form-group' wrapper_class hasError=field.errors required=field.field.required %}
    Where `wrapper_class` could be an existing string of classes:
    could render: `class="form-group input text-input has-error required"`

    :param class_list: List of classes to concatenate together.
    :param class_bools: Key-value pair; will include key as a class if value is true.
    :return: Combined `class="..."` block.
    """

    more_classes = tuple(
        _re_camel_humps.sub(_to_kabob, key).lower() for key, value in class_bools.items() if value
    )
    css_classes = ' '.join(str(arg) for arg in set(class_list + more_classes) if arg) or ' '
    return (' class="%s" ' % css_classes) if css_classes else ' '


@register.simple_tag(takes_context=True)
def field_required(context):
    return ' <span class="asteriskField">*</span>' if context['field'].field.required else ''
