# Generated by Django 5.0 on 2023-12-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_alter_goods_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Остаток товара'),
        ),
    ]