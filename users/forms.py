from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if '@' not in username:
            raise ValidationError(_("Електронна адреса має містити символ «@»"))
        return username

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if '@' not in username:
            raise ValidationError(_("Електронна адреса має містити символ «@»"))
        return username

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        )


class ProfileForm(UserChangeForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    user_name = forms.CharField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
        )
