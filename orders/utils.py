import uuid

from carts.const import ORDER_STATUS
from carts.models import Cart
from django.utils import timezone
from carts.const import ORDER_STATUS


def create_order(user):
    carts = Cart.objects.filter(user=user).filter(ordered=None)
    carts.update(ordered=timezone.now())
    carts.update(order_uuid=uuid.uuid4())
    status = ORDER_STATUS[1][0]
    carts.update(status=status)
