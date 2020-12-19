from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserInfo

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateUserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['user', 'name', 'phone', 'gender', 'city', 'date_of_birth', 'interests']
