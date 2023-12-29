from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.validators import cyrillic_validator, latin_space_hyphen, gte_6


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, blank=False, validators=[
        cyrillic_validator, ], verbose_name="Имя")
    surname = models.CharField(max_length=100, blank=False, validators=[
        cyrillic_validator, ], verbose_name="Фамилия")
    partonymic = models.CharField(max_length=100, blank=False, validators=[
        cyrillic_validator, ], verbose_name="Отчество")
    login = models.CharField(max_length=100, blank=False, validators=[
        latin_space_hyphen, ], verbose_name="Логин")
    password = models.CharField(max_length=100, blank=False, validators=[
        gte_6, ], verbose_name="Пароль")
    email = models.EmailField(blank=False, verbose_name="Емейл")
    rules = models.BooleanField(blank=False, null=False, default=False,
                                verbose_name="Согласен с правилами регистрации")
