#!/usr/bin/env python
# coding=utf-8
import re

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

register = template.Library()


@register.simple_tag(takes_context=True)
def active_url(context, label, url, *args, **kwargs):
    template_string = '<li{li_attrs}><a href="{url}">{label}</a></li>'
    try:
        url = reverse(url, args=args, kwargs=kwargs)
        pattern = '^%s$' % url
    except NoReverseMatch:
        pattern = url

    path = context['request'].path
    li_attrs = ' class="active"' if re.search(pattern, path) else ''
    return format_html(template_string, li_attrs=mark_safe(li_attrs), url=url,
                       label=_(label))
