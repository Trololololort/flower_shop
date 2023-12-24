from django.db import models

from general.models import NameMixin
from django.urls import reverse


class Category(NameMixin, models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Extra(NameMixin, models.Model):
    class Meta:
        verbose_name = "Дополнительная характеристика"
        verbose_name_plural = "Дополнительные характеристики"


class Package(NameMixin, models.Model):
    class Meta:
        verbose_name = "Тип упаковки"
        verbose_name_plural = "Типы упаковки"


class Color(NameMixin, models.Model):
    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


class Type(NameMixin, models.Model):
    class Meta:
        verbose_name = "Вид товара"
        verbose_name_plural = "Виды товара"


class Country(NameMixin, models.Model):
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class GoodsManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset().order_by("-added")
        return queryset


class Goods(NameMixin, models.Model):
    objects = GoodsManager()

    added = models.DateTimeField(auto_now_add=True,
                                 verbose_name="Дата добавления")

    # 800 x 400 px.
    photo = models.ImageField(verbose_name="Фото")
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name="Цена")
    origin = models.ForeignKey(
        "Country",
        on_delete=models.CASCADE,
        verbose_name="Страна-производитель",
    )

    type = models.ForeignKey(
        "Type",
        on_delete=models.CASCADE,
        verbose_name="Вид",
    )

    color = models.ForeignKey(
        "Color",
        on_delete=models.CASCADE,
        verbose_name="Цвет",
    )

    package = models.ForeignKey(
        "Package",
        on_delete=models.CASCADE,
        verbose_name="Упаковка",
    )

    extra = models.ForeignKey(
        "Extra",
        on_delete=models.CASCADE,
        verbose_name="Дополнительная характеристика",
    )

    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )

    present = models.BooleanField(null=False,
                                  default=True,
                                  verbose_name="В наличии")

    def get_absolute_url(self):
        return reverse('goods-detail', kwargs={"pk": self.id})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
