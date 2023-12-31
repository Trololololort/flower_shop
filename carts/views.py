from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from carts.forms import OrderForm
from carts.service import get_cart_contents, add_goods_to_cart


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
        """
        Добавить или убрать товар из корзины.
        Если товар не может быть добавлен в корзину, сообщить об этом.
        Если товара не хватает для добавления, ничего не

        goods_id - id товара.
        addend - может быть +1 (добавить) или -1 (удалить).

        Товар можно добавить, каталога, карточки товара и из корзины. Т.е. из разных мест.
        Поэтому сообщение показать на странице, где добавлялся товар.
        """
        goods_id = request.POST.get('goods_id')
        addend = int(request.POST.get('addend'))

        assert (addend == 1 or addend == -1)

        status = add_goods_to_cart(goods_id, request.user, addend)

        if status["status"] == 200:
            messages.add_message(request, messages.INFO, status["message"])
            return redirect(request.META['HTTP_REFERER'])
        else:
            return HttpResponse(status["message"], status=status)
