# Generated by Django 5.0 on 2023-12-29 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Категория/Вид товара',
                'verbose_name_plural': 'Категории/Виды товаров',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Наименование')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Остаток товара')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.category', verbose_name='Категория / Вид товара')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.color', verbose_name='Цвет')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.country', verbose_name='Страна-производитель')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
