from django.urls import path

from .views import SignUpView, PasswordValidationView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    # path("login/", ExtendedLoginView.as_view(), name="login"),
    path("validate-password/", PasswordValidationView.as_view(), name="validate-password"),
]