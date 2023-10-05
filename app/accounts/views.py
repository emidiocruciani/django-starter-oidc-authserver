from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView as LoginViewBase,
    LogoutView as LogoutViewBase,
    PasswordResetView as PasswordResetViewBase,
    PasswordResetConfirmView as PasswordResetConfirmViewBase,
)
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django_registration.backends.activation.views import (
    ActivationView as ActivationViewBase,
    RegistrationView as RegistrationViewBase
)

from accounts.forms import RegistrationForm


class ActivationView(ActivationViewBase):
    success_url = reverse_lazy('login')
    template_name = 'accounts/page/activation_error.html'

    def activate(self, *args, **kwargs):
        result = super().activate(*args, **kwargs)
        messages.success(self.request, 'Your account has been activated')

        return result


class LoginView(LoginViewBase):
    initial = {'username': '', 'password': ''}
    template_name = 'accounts/page/login.html'


class LogoutView(LogoutViewBase):
    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        if not request.user.is_authenticated:
            messages.success(request, 'You have been logged out')

        return result


class PasswordResetConfirmView(PasswordResetConfirmViewBase):
    initial = {'new_password1': '', 'new_password2': ''}
    success_url = reverse_lazy('login')
    template_name = 'accounts/page/password_reset_confirm.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Password has been reset. You can now login')

        return response


class PasswordResetView(PasswordResetViewBase):
    email_template_name = 'accounts/email/password_reset_body.html'
    initial = {'email': ''}
    subject_template_name = 'accounts/email/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset')
    template_name = 'accounts/page/password_reset.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Password reset email sent')

        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/page/profile.html'


class RegistrationView(RegistrationViewBase):
    disallowed_url = reverse_lazy('registration_help')
    email_body_template = 'accounts/email/registration_body.html'
    email_subject_template = 'accounts/email/registration_subject.txt'
    form_class = RegistrationForm
    initial = {'username': '', 'email': '', 'password1': '', 'password2': ''}
    success_url = reverse_lazy('registration_help')
    template_name = 'accounts/page/registration.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, 'An email has been sent')

        return result
