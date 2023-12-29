from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    # name = models.CharField(max_length=100, blank=False, verbose_name="Имя")
    # surname = models.CharField(max_length=100, blank=False, verbose_name="Фамилия")
    partonymic = models.CharField(max_length=100, blank=False, verbose_name="Отчество")
    # login = models.CharField(max_length=100, blank=False, verbose_name="Логин")
    # password = models.CharField(max_length=100, blank=False, verbose_name="Пароль")
    # email = models.EmailField(blank=False, verbose_name="Емейл")
    rules = models.BooleanField(verbose_name="Согласен с правилами регистрации",
                                blank=False,
                                null=False,
                                )
