# templatetags/custom_filters.py
from django import template
from django.utils.translation import gettext as _

register = template.Library()


@register.filter(name='template_trans')
def template_trans(text):
    try:
        return _(text)
    except Exception as e:
        return text
