from django.contrib import messages
from django.db import transaction

from carts.models import Cart
from general.const import RESULT
from orders.models import Order


@transaction.atomic
def create_order(user):
    """
    Создать заказ и обновить корзину (добавить значение для внешнего ключа - номер заказа).

    """
    carts = Cart.objects.filter(user=user, order=None)

    new_order = Order.objects.create(user=user)

    carts.update(order=new_order)

    return new_order.pk


def delete_order(order_id):
    order_obj = Order.objects.filter(pk=order_id).first()

    if order_obj:
        order_obj.delete()
        result = RESULT.SUCCESS
    else:
        result = RESULT.FAILURE

    return result
