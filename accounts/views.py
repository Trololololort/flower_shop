from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (

    UserCreationForm,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic, View

from accounts.forms import LoginForm, PassvordValidationForm

UserModel = get_user_model()


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ExtendedLoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"


class PasswordValidationView(LoginRequiredMixin, View):

    def get(self, request):
        context = {'form': PassvordValidationForm()}
        return render(request, "accounts/password_validation.html", context)
    def post(self, request):
        a = 0


