from django.db import models

class Order(models.Model):
    added = models.DateTimeField(auto_now_add=True,
                                 verbose_name="Дата создания")
    cart = models.ForeignKey("carts.Cart", on_delete=models.CASCADE, verbose_name="Корзина")

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"