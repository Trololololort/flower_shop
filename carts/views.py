from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from carts.models import Cart


def get_total(a_queryset):
    sum = 0
    [sum := elem.goods.price * elem.quantity for elem in a_queryset]
    return sum


class CartDetailView(LoginRequiredMixin,
                     TemplateView):
    template_name = "carts/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = kwargs.get('user')
        context["object_list"] = Cart.objects.filter(user=user)
        context["total"] = get_total(context["object_list"])
        return context
