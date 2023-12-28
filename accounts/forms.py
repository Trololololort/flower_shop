from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms

# UserModel = get_user_model()

# FIELD_NAME_MAPPING = {
#     'username': 'login',
# }
#
#
# class LoginForm(AuthenticationForm):
#
#     def add_prefix(self, field_name):
#         # look up field name; return original if not found
#         field_name = FIELD_NAME_MAPPING.get(field_name, field_name)
#         return super().add_prefix(field_name)


class PassvordValidationForm(forms.Form):
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
