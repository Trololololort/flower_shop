from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic, View

from accounts.forms import LoginForm, PassvordValidationForm, RegistrationForm
from accounts.models import CustomUser

UserModel = get_user_model()


class SignUpView(generic.View):
    def get(self, request):
        context = {"form": RegistrationForm()}
        return render(request, template_name="registration/signup.html", context=context)

    def post(self, request):
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        partonymic = request.POST.get('partonymic')
        login = request.POST.get('login')
        password = request.POST.get('password')
        email = request.POST.get('email')
        rules = bool(request.POST.get('rules'))

        CustomUser.objects.create(last_name=surname,
                                  first_name=name,
                                  partonymic=partonymic,
                                  username=login,
                                  password=password,
                                  email=email,
                                  rules=rules)

        messages.add_message(request, messages.INFO, "Создан пользователь {}.".format(login))

        return redirect("home")


class ExtendedLoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"


class PasswordValidationView(LoginRequiredMixin, View):

    def get(self, request):
        context = {'form': PassvordValidationForm()}
        return render(request, "accounts/password_validation.html", context)

    def post(self, request):
        a = 0
