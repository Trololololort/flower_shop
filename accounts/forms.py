from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

UserModel = get_user_model()

FIELD_NAME_MAPPING = {
    'username': 'login',
}


class LoginForm(AuthenticationForm):

    def add_prefix(self, field_name):
        # look up field name; return original if not found
        field_name = FIELD_NAME_MAPPING.get(field_name, field_name)
        return super().add_prefix(field_name)


CYR_MESSAGE = "Допустимы кириллица, пробел и тире."
LAT_MESSAGE = "Допустимы латиница, цифры и тире."
GTE6_MESSAGE = "Не менее 6 символов."

VALIDATE_CYR = {"pattern": "^[А-Яа-яЁё\- ]+$", "required": True, "title": CYR_MESSAGE, }
VALIDATE_LAT = {"pattern": "^[A-Za-z0-9\-]*$", "required": True, "title": LAT_MESSAGE, }
VALIDATE_GTE6 = {"pattern": "^(.{6})(.*)$", "required": True, "title": GTE6_MESSAGE, }


class RegistrationForm(forms.Form):
    surname = forms.CharField(required=True, widget=forms.TextInput(attrs=VALIDATE_CYR, ),
                              label="Фамилия ({})".format(CYR_MESSAGE))
    name = forms.CharField(required=True, widget=forms.TextInput(attrs=VALIDATE_CYR, ),
                           label="Имя ({})".format(CYR_MESSAGE))
    partonymic = forms.CharField(required=True, widget=forms.TextInput(attrs=VALIDATE_CYR, ),
                                 label="Отчество ({})".format(CYR_MESSAGE))
    login = forms.CharField(required=True, widget=forms.TextInput(attrs=VALIDATE_LAT, ),
                            label="Логин ({})".format(LAT_MESSAGE))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs=VALIDATE_GTE6, ),
                               label="Пароль ({})".format(GTE6_MESSAGE))
    repeated_password = forms.CharField(widget=forms.PasswordInput(attrs=VALIDATE_GTE6, ), label="Повтор пароля")
    email = forms.EmailField(required=True, label="Электронная почта")
    rules = forms.BooleanField(required=True, label="Согласен с правилами регистрации")
