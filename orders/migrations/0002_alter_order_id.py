# Generated by Django 5.0 on 2023-12-29 10:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c2607939-65f5-4b0c-84f4-c2a644ff21cf'), primary_key=True, serialize=False),
        ),
    ]
