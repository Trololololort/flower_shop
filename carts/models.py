from django.contrib.auth.models import User
from django.db import models

from general.model_mixins import UserMixin


class Cart(UserMixin,
           models.Model):
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


    order = models.ForeignKey("orders.Order",
                              on_delete=models.CASCADE,
                              null=True,
                              blank=True,)


    def price(self):
        return self.goods.price

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"


