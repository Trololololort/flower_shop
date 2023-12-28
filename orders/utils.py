from django.contrib import messages
from django.db import transaction

from carts.models import Cart
from orders.models import Order


@transaction.atomic
def create_order(user, request):
    carts = Cart.objects.filter(user=user, order=None)

    new_order = Order.objects.create(user=user)

    carts.update(order=new_order)

    messages.add_message(request, messages.INFO, "Ваш заказ номер {} принят к исполнению.".format(new_order.pk))
