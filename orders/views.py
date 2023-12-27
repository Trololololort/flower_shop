from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .utils import create_order
class CreateOrder(LoginRequiredMixin,
                  View):

    def post(self, request):

        user = request.user
        password = request.POST.get("password")

        try:
            validate_password(password=password, user=user)
        except ValidationError:
            messages.add_message(request, messages.INFO, "Неверный пароль")
            return redirect("cart-detail", user.id)


        create_order(user)

        return redirect("home")


