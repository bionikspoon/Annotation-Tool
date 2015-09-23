from crispy_forms import layout as crispy_forms_layout

from . import TEMPLATE_PACK


class Card(crispy_forms_layout.Fieldset):
    css_class = 'mdl-card mdl-shadow--2dp mdl-color--white'
    template = "{0}/layout/card.html".format(TEMPLATE_PACK)
