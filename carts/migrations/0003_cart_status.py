# Generated by Django 5.0 on 2023-12-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_alter_cart_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(blank=True, default='---', max_length=9, verbose_name='Статус'),
        ),
    ]
