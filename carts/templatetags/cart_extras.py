from django import template
from django.utils.safestring import mark_safe

from carts.models import Cart

register = template.Library()


@register.simple_tag
def cart_script(user):
    if not user:
        return

    cart = Cart.objects.filter(user=user)
    result = "<script>"
    # result += "{trololo}"
    result += "</script>"
    return mark_safe(result)