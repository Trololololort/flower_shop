from django.contrib.auth.models import User
from django.db import models


class UserMixin(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="Пользователь", )

    class Meta:
        abstract = True