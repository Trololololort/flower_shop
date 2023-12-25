from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    partonymic = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    rules = models.BooleanField(blank=False)

