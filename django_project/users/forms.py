from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        """Meta class here gives nested namespace for configurations and keeps them in central location"""
        model = User
        fields = ['username', 'email', 'password1', 'password2']