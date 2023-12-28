from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView, View
from django.contrib import messages

from carts.forms import OrderForm
from carts.models import Cart
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
        user = kwargs.get('user')
        object_list = Cart.objects.filter(user=user).filter(order=None)
        context["object_list"] = object_list
        context["order_form"] = OrderForm()
        context["total"] = get_total(object_list)
        return context


class AddToCart(View):
    def post(self, request):
        user_id = request.POST.get('user_id')
        goods_id = request.POST.get('goods_id')
        referer = request.POST.get('referer')

        user = User.objects.filter(pk=user_id).first()
        goods = Goods.objects.filter(pk=goods_id).first()

        if user and goods:

            the_goods_already_in_cart = Cart.objects.filter(user=user, goods=goods, order=None).first()

            if the_goods_already_in_cart:
                the_goods_already_in_cart.quantity=(the_goods_already_in_cart.quantity + 1)
                the_goods_already_in_cart.save()
            else:
                Cart.objects.create(user=user, goods=goods, quantity=1)
            messages.add_message(request, messages.INFO, 'Товар "{}" добавлен в корзину'.format(goods.name))
            return redirect(referer)
        else:
            if not user:
                return HttpResponse("Wrong user", status=400)
            elif not goods:
                return HttpResponse("Wrong goods id", status=400)
