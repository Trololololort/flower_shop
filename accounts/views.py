# Avoid shadowing the login() and logout() views below.
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (

    UserCreationForm,
)
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import LoginForm

UserModel = get_user_model()


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ExtendedLoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"
