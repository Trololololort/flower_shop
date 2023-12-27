import uuid

from django.contrib import messages
from carts.models import Cart
from django.utils import timezone
from carts.const import ORDER_STATUS


def create_order(user, request):
    carts = Cart.objects.filter(user=user).filter(ordered=None)
    a_uuid = uuid.uuid4()
    carts.update(ordered=timezone.now(), order_uuid=a_uuid, status = ORDER_STATUS[1][0])

    messages.add_message(request, messages.INFO, "Ваш заказ номер {} принят к исполнению.".format(a_uuid))





