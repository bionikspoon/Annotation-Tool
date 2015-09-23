from django import template
# from django.forms import widgets
from floppyforms import widgets

register = template.Library()


@register.filter
def is_input(field):
    return isinstance(field.field.widget, widgets.TextInput)


@register.filter
def is_textarea(field):
    return isinstance(field.field.widget, widgets.Textarea)
