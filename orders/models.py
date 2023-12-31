import uuid

from django.db import models

from general.model_mixins import UserMixin
from orders.const import ORDER_STATUS


class Order(UserMixin,
            models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    ordered = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Дата заказа")
    status = models.CharField(max_length=9,
                              choices=ORDER_STATUS,
                              verbose_name="Статус",
                              blank=True,
                              null=False,
                              default="NEW")

    cancellation_cause = models.TextField(verbose_name="Причина отказа",
                                          default="",
                                          null=False,
                                          blank=True)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
