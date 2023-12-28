from django.contrib.auth.models import User
from django.db import models

from accounts.models import CustomUser


class UserMixin(models.Model):
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             verbose_name="Пользователь", )

    class Meta:
        abstract = True
