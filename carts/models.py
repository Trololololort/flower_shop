from django.contrib.auth.models import User
from django.db import models
import uuid

from carts.const import ORDER_STATUS


class Cart(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="Пользователь", )
    goods = models.ForeignKey("goods.goods",
                              on_delete=models.CASCADE,
                              verbose_name="Товар")
    # Магазин торгует только штучными товарами.
    # Теоретически, возможна продажа весового товара (например, удобрений).
    # Но для интернет-магазина это довольно странно. А т.к. в ТЗ ничего не сказано,
    # поэтому трактуем самостоятельно: только штучный.
    quantity = models.IntegerField(blank=False,
                                   null=False,
                                   default=0,
                                   verbose_name="Количество")

    ordered = models.DateTimeField(verbose_name="Заказано", null=True)
    order_uuid = models.UUIDField(verbose_name="ID заказа",
                                  null=True,
                                  )

    status = models.CharField(max_length=9,
                              choices=ORDER_STATUS,
                              verbose_name="Статус",
                              blank=True,
                              null=False,
                              default="---")

    def price(self):
        return self.goods.price

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


