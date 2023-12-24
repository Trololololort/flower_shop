from django.db import models

from general.models import NameMixin
from django.urls import reverse


class Category(NameMixin, models.Model):
    class Meta:
        verbose_name = "Категория/Вид товара"
        verbose_name_plural = "Категории/Виды товаров"


class Color(NameMixin, models.Model):
    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


class Country(NameMixin, models.Model):
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Goods(NameMixin, models.Model):
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

    color = models.ForeignKey(
        "Color",
        on_delete=models.CASCADE,
        verbose_name="Цвет",
    )

    # Т.к. для страницы "Каталог" в ТЗ под категорией понимается
    # цветы, упаковка, дополнительно,
    # а для страницы "Товар" надо отразить вид товара,
    # то категорию считаем эквивалентной виду товара.
    # Потому что цветы, упаковка и дополнительно -
    # попадает под определение вида товара.
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        verbose_name="Категория / Вид товара",
    )

    present = models.BooleanField(null=False,
                                  default=True,
                                  verbose_name="В наличии")

    def get_absolute_url(self):
        return reverse('goods-detail', kwargs={"pk": self.id})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
