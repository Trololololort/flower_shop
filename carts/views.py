from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from carts.forms import OrderForm
from carts.models import Cart
from carts.utils import get_cart_contents
from goods.models import Goods


def get_total(a_queryset):
    sum = 0
    [sum := sum + elem.goods.price * elem.quantity for elem in a_queryset]
    return sum


class CartDetailView(LoginRequiredMixin,
                     TemplateView):
    template_name = "carts/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = get_cart_contents(self.request.user)
        context["object_list"] = object_list
        context["order_form"] = OrderForm()
        context["total"] = get_total(object_list)
        return context


class AddToCart(LoginRequiredMixin,
                View):
    def post(self, request):
        goods_id = request.POST.get('goods_id')
        addend = int(request.POST.get('addend'))
        referer = request.POST.get('referer')

        goods = Goods.objects.filter(pk=goods_id).first()

        if goods:

            the_goods_already_in_cart = Cart.objects.filter(user=request.user, goods=goods, order=None).first()

            if the_goods_already_in_cart:
                the_goods_already_in_cart.quantity = (the_goods_already_in_cart.quantity + addend)
                the_goods_already_in_cart.save()
            else:
                Cart.objects.create(user=request.user, goods=goods, quantity=1)
            messages.add_message(request, messages.INFO, 'Товар "{}" добавлен в корзину'.format(goods.name))
            return redirect(referer)
        elif not goods:
            return HttpResponse("Wrong goods id", status=400)
