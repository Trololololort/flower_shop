from django.core.management.base import BaseCommand, CommandError
from carts.models import Cart

# https://stackoverflow.com/questions/11764709/can-you-add-parameters-to-django-custom-admin-actions
class Command(BaseCommand):
    pass