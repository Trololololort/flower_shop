# Generated by Django 5.0 on 2023-12-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_package_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='present',
            field=models.BooleanField(default=True, verbose_name='В наличии'),
        ),
    ]
