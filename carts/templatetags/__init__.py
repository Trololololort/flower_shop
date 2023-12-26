from django import template
from carts.models import Cart

register = template.Library()


@register.simple_tag
def cart_script(user):
    cart = Cart.objects.filter(user=user)
    result = "<script>"
    result += "<script>"
