# Generated by Django 5.0 on 2024-01-05 19:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cd9bf2be-1e6f-477d-ad22-d120895973da'), primary_key=True, serialize=False),
        ),
    ]
