from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView, ListView

from carts.views import get_total
from orders.models import Order
from orders.utils import create_order


class OrdersListView(LoginRequiredMixin,
                     ListView):
    model = Order
    template_name = "orders/order_list.html"
    paginate_by = 5

    def get_queryset(self):
        result = Order.objects.filter(user=self.request.user).order_by(
            "-ordered")
        return result


class OrderDetailView(LoginRequiredMixin,
                      DetailView):
    model = Order
    template_name = "orders/order_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goods'] = self.object.cart_set.all()
        context['total'] = get_total(context['goods'])
        return context


class CreateOrder(LoginRequiredMixin,
                  View):

    def post(self, request):

        user = request.user
        password = request.POST.get("password")

        try:
            validate_password(password=password, user=user)
        except ValidationError:
            messages.add_message(request, messages.INFO, "Неверный пароль")
            return redirect("cart-detail", user.id)


        create_order(user, request)

        return redirect("orders-list")


class DeleteOrder(LoginRequiredMixin,
                  View):

    def post(self, request):
        order_id = request.POST.get("order")

        if order_id:
            order_obj = Order.objects.filter(pk=order_id).first()
            order_obj.delete()
            messages.add_message(request, messages.INFO, "Удален заказ {}.".format(order_id))
        else:
            messages.add_message(request, messages.INFO, "Не удалось удалить заказ.")
        return redirect("orders-list")