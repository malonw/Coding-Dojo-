from django import forms
from django.core.exceptions import DisallowedHost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class NewUserForm(UserCreationForm):
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)

    class Meta:
            model = User
            fields=("email", "password1","password2")

