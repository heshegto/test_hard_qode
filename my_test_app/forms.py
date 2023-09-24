# Форма для аутентификации пользователей
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from my_test_app.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ("username", 'password')
