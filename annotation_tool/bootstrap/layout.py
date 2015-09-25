#!/usr/bin/env python
# coding=utf-8
from crispy_forms.layout import Div, BaseInput
from crispy_forms.utils import TEMPLATE_PACK
from django.template.loader import render_to_string

class Button(BaseInput):
    template = "%s/layout/button.html"
    input_type = 'button'

class Submit(Button):
    template = "%s/layout/submit.html"
    input_type = 'submit'
    field_classes = 'mdl-button mdl-js-button mdl-js-ripple-effect mdl-button--raised mdl-button--accent'

class Cancel(Button):
    input_type = 'button'
    field_classes = 'mdl-button mdl-js-button mdl-js-ripple-effect'


class Column6(Div):
    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        if not context:
            context = {}

        context['stacked'] = True
        fields = self.get_rendered_fields(form, form_style, context, template_pack, **kwargs)

        template = self.get_template_name(template_pack)
        return render_to_string(template, {'div': self, 'fields': fields})
