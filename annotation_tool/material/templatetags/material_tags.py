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


@register.filter
def is_radio(field):
    return isinstance(field.field.widget, widgets.RadioSelect)

@register.filter
def is_select(field):
    return isinstance(field.field.widget, widgets.Select)

@register.filter
def is_select_multiple(field):
    return isinstance(field.field.widget, widgets.SelectMultiple)
