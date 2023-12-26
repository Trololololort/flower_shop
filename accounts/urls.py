from django.urls import path

from .views import SignUpView, LoginView, ExtendedLoginView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", ExtendedLoginView.as_view(), name="login"),
]