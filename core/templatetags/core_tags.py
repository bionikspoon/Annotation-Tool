#!/usr/bin/env python
# coding=utf-8
"""
Core template tags.
"""
import re

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

register = template.Library()


@register.simple_tag(takes_context=True)
def active_url(context, label, url, *args, **kwargs):
    """
    Create link with `class='active'`.

    :type context: django.template.context.RequestContext
    :type label: django.utils.safestring.SafeText Human readable link text.
    :type url: SafeText or str URL name or path.
    :param args: *args for `reverse()`.
    :param kwargs: **kwargs for `reverse()`.
    :return: Link with `<li>` tag.
    :rtype : SafeString
    """
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
