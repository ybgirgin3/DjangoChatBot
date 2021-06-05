from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from uuid import uuid4
uid = uuid4()
uid = str(uid).split("-")[0]


class RegisterForm(UserCreationForm):
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    privateKey = forms.CharField(initial=uid, help_text="Lütfen Hesap Anahtarı Kaydediniz")

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'phone_number', 'password1', 'password2', 'privateKey')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Hesap Anahtarı / Kullanıcı Adı')
