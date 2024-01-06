from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic, View

from accounts.forms import LoginForm, RegistrationForm
from accounts.models import CustomUser
from accounts.service import create_user, is_login_occupied

UserModel = get_user_model()


class SignUpView(generic.View):
    def get(self, request):
        context = {"form": RegistrationForm()}
        return render(request, template_name="registration/signup.html", context=context)

    def post(self, request):
        """
        Создать пользователя. После создания редирект на главную страницу.
        """

        surname = request.POST.get('surname')
        name = request.POST.get('name')
        partonymic = request.POST.get('partonymic')
        login = request.POST.get('login')
        password = request.POST.get('password')
        email = request.POST.get('email')
        rules = bool(request.POST.get('rules'))

        create_user(surname,
                    name,
                    partonymic,
                    login,
                    email,
                    rules,
                    password)
        messages.add_message(request, messages.INFO, "Создан пользователь {}.".format(login))

        return redirect("home")


class ExtendedLoginView(LoginView):
    """
    Вместо стандартной формы Django
    используем собственную форму.
    """

    form_class = LoginForm
    template_name = "accounts/login.html"


class IsLoginOccupiedView(View):

    def post(self, request):
        """

        @param request:
        @return:
        """
        login = request.POST.get("login")

        status = is_login_occupied(login)

        return HttpResponse(status["status"], message=status["message"])
