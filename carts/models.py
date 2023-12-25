from django.contrib.auth.models import User
from django.db import models


class Cart(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="Пользователь")
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

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"