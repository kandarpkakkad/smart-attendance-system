from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Professor, Student


class LoginForm(UserCreationForm):
    a = 10
