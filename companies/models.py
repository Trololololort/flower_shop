from django.db import models

from general.models import NameMixin


class Company(NameMixin,
              models.Model):
    address = models.CharField(max_length=1000,
                               default="",
                               null=False,
                               blank=False)
    phone = models.CharField(max_length=100,
                             default="",
                             null=False,
                             blank=False)

    email = models.EmailField()

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
