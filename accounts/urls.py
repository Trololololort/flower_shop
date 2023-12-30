from django.urls import path

from .views import ExtendedLoginView, IsLoginOccupiedView, SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", ExtendedLoginView.as_view(), name="login"),
    path("is-login-occupied/", IsLoginOccupiedView.as_view(), name="is_login_occupied"),
]
