# Inside your app's forms.py file
from django import forms
from django.db.models import fields
from django.forms.widgets import PasswordInput
from .models import User



class RegisterForm(forms.Form):
    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit = True):
        user = super(RegisterForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password=PasswordInput()
