from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic, View

from accounts.forms import LoginForm, RegistrationForm
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

        user = CustomUser.objects.create(last_name=surname,
                                  first_name=name,
                                  partonymic=partonymic,
                                  username=login,
                                  password=password,
                                  email=email,
                                  rules=rules)
        user.set_password(user.password) # Сохранить хэшированный пароль.
        user.save()



        messages.add_message(request, messages.INFO, "Создан пользователь {}.".format(login))

        return redirect("home")


class ExtendedLoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"


class IsLoginOccupiedView(View):

    def post(self, request):
        status_code = 204

        login = request.POST.get("login")

        occupied_login = CustomUser.objects.filter(username=login).first()

        if occupied_login:
            status_code = 403

        return HttpResponse(status=status_code)
