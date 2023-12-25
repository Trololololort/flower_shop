from django.shortcuts import render
from django.views.generic import TemplateView

from carts.models import Cart


class CartDetailView(TemplateView):
    template_name = "carts/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.GET.get('user')
        context["object_list"] = Cart.objects.filter(user=user)
        return context

