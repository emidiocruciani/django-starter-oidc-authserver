from django.urls import path
from django.views.generic import TemplateView

from accounts.views import (
    ProfileView,
    LoginView,
    LogoutView,
    ActivationView,
    PasswordResetConfirmView,
    PasswordResetView,
    RegistrationView
)

urlpatterns = [
    path(
        'activation/<str:activation_key>/',
        ActivationView.as_view(),
        name='activation',
    ),
    path(
        'login/',
        LoginView.as_view(),
        name='login',
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout',
    ),
    path(
        'profile/',
        ProfileView.as_view(),
        name='profile',
    ),
    path(
        'registration/',
        RegistrationView.as_view(),
        name='registration',
    ),
    path(
        'registration/help/',
        TemplateView.as_view(template_name='accounts/page/registration_help.html'),
        name='registration_help',
    ),
    path(
        'reset/',
        PasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'reset/confirm/<str:uidb64>/<str:token>/',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
]
