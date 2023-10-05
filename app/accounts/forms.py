from django.contrib.auth import get_user_model
from django_registration.forms import RegistrationForm as RegistrationFormBase


class RegistrationForm(RegistrationFormBase):
    class Meta(RegistrationFormBase.Meta):
        model = get_user_model()
