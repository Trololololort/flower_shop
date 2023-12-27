from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, ListView

from carts.models import Cart
from orders.utils import create_order


class OrdersListView(ListView):
    model = Cart
    template_name = "orders/order_list.html"
    paginate_by = 5

    def get_queryset(self):
        result = Cart.objects.filter(user=self.request.user).values('order_uuid', "ordered").order_by(
            "-ordered").distinct()
        return result


class OrderDetailView(TemplateView):
    template_name = "orders/order_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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


        create_order(user)

        return redirect("home")
