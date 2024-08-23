from catalog.forms import StyleFormMixin
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django import forms


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class ResetPasswordForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
