from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import validators


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput, validators=[validate_password])
    class Meta():
        model = User
        fields = ["username", "password", "email"]